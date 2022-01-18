from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_data= mongo.db.mars.find_one()

    # Return template and data
    return render_template("index.html", hemispheres=mars_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def mars_data():

    # Run the scrape function
    mars_scrape = scrape_mars.scrape()

  
    mongo.db.mars.update_one({}, {"$set": mars_scrape}, upsert=True)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)



