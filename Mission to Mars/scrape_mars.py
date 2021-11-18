from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import pandas as pd
import time
import pymongo
from webdriver_manager.chrome import ChromeDriverManager


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    url = 'http://redplanetscience.com/'
    browser.visit(url)

    time.sleep(1)
    html = browser.html
    soup = bs(html, 'html.parser')


    news_title = soup.find('div', class_="content_title").text
    
    news_p = soup.find('div', class_="article_teaser_body").text

    mars = {
        "news_title": news_title,
        "news_p": news_p
    }
 

# JPL Mars Space Images - Featured Image

    url = 'https://spaceimages-mars.com/'
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    soup = bs(html, 'html.parser')

    featured_image = soup.find('img', class_="headerimage fade-in")
    featured_image_url = url + featured_image['src']
    #print(featured_image_url)

    url = 'https://galaxyfacts-mars.com/'

    tables = pd.read_html(url)
    tables

    tables_df = tables[1]
    tables_df.columns=['description', 'value']
    tables_df = tables_df.reset_index(drop=True)
    tables_df.head()

    html_table = tables_df.to_html()
    html_table

    # html_table.replace('\n', '')

    # tables_df.to_html('table.html')


# Mars Hemispheres

    url = 'https://marshemispheres.com/'
    browser.visit(url)


    images = browser.find_by_css('.thumb')

    
    for i in images:
        # print (i)   


        browser.visit(url)
        html = browser.html
        soup = bs(html, 'html.parser')
        time.sleep(2)

        images = browser.find_by_css('.collapsible results')

        # for i in images:
        soup.find("thumb")
        # print (soup.find("thumb"))

        hemisphere_links = soup.find_all("a", {"class":"itemLink product-item"})
        # print (hemisphere_links)

    links = []


    for a in hemisphere_links:
        a["href"]
        links.append(a["href"])


    links = list(dict.fromkeys(links))
        # print(links)
    links.remove("#")
        # print(links)

    links = []


    for a in hemisphere_links:
        a["href"]
        links.append(a["href"])


    links = list(dict.fromkeys(links))
        # print(links)
    links.remove("#")
        # print(links)
    
    hemispheres_url = []
    img_url= []
    titles = []

    for hemisphere in range(4):
        
        browser.visit(f"https://marshemispheres.com/{i}")
        # print(f"https://marshemispheres.com/{i}")
        time.sleep(1)
        html = browser.html
        # print (html)
        soup = bs(html, 'html.parser')
        hemispheres = {}
        hemispheres['img_url'] = url + soup.find("img", class_ = "wide-image")["src"]
        hemispheres['titles'] = soup.find("h2", class_="title").text
        hemispheres_url.append(hemispheres)
        # img_url.append(hemispheres['img_url'])
        # titles.append(hemispheres['titles'])
        # print(hemispheres)
        browser.back()

    mars = {"news_title": news_title,
        "news_p":news_p,
        "featured_image": featured_image_url,
        "tables_df": html_table,
        "hemispheres_images": hemispheres_url, 
        "titles":titles
}
        #Close the browser after scraping F
    browser.quit()

    #Return results
    return img_url

