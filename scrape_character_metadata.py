from bs4 import BeautifulSoup as bs
import pandas as pd
import requests as req
from splinter import Browser

top_50_characters = pd.read_csv("top_50.csv", header=None)

for x in range(0, len(top_50_characters[0])):
    top_50_characters[0][x] = top_50_characters[0][x].replace(" ", "_")

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
	browser = init_browser()
	
	name_list = []
	gender_list = []
	age_list = []
	occupation = []
	first_appearance_list = []

	base_url = 'https://simpsonswiki.com/wiki/'
	character_name = top_50_characters[0][0]
	response = req.get(base_url + character_name)
	soup = bs(response.text, 'html.parser')

	#title_section = soup.find('div', class_='content_title')
	#mars_dict["news_title"] = title_section.find('a').text.strip()
	#mars_dict["news_p"] = soup.find('div', class_='rollover_description_inner').text.strip()

	#url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
	#browser.visit(url)
	#browser.click_link_by_partial_text('FULL IMAGE')

	#html = browser.html
	#soup = bs(html, 'html.parser')

	#featured_image_medium = soup.find('a', class_='button fancybox')
	#featured_image_link = featured_image_medium['data-link']
	#featured_image_link_url = 'https://www.jpl.nasa.gov' + featured_image_link

	#browser.visit(featured_image_link_url)
	#html = browser.html
	#soup = bs(html, 'html.parser')

	#featured_image_large = soup.find('figure', class_='lede')
	#featured_image_endpoint = featured_image_large.find('img')['src']
	#mars_dict["featured_image_url"] = 'https://www.jpl.nasa.gov' + featured_image_endpoint

	#url = 'https://twitter.com/marswxreport?lang=en'
	#response = req.get(url)
	#soup = bs(response.text, 'html.parser')
	#mars_dict["mars_weather"] = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text

	#url = 'http://space-facts.com/mars/'
	#tables = pd.read_html(url)
	#df = tables[0]
	#df.columns = ['description', 'value']
	#df.set_index('description', inplace=True)
	#html_table = df.to_html()
	#mars_dict["html_table"] = html_table.replace('\n', '')

	#url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
	#browser.visit(url)

	#html = browser.html
	#soup = bs(html, 'html.parser')

	#title_list = []
	#url_list = []
	#item_list = soup.find_all('div', class_ = 'item')

	#for x in range (0, len(item_list)):
		#title = item_list[x].find('h3').text
		#title = title.rsplit(' ', 1)[0]
		#title_list.append(title)
		    
		#link_endpoint = item_list[x].find('a', class_ = 'itemLink product-item')['href']
		#hemisphere_link = 'https://astrogeology.usgs.gov' + link_endpoint
		    
		#browser.visit(hemisphere_link)
		#html = browser.html
		#soup = bs(html, 'html.parser')
		#link_div = soup.find('div', class_ = 'downloads')
		#full_image_link = link_div.find('a')['href']
		#url_list.append(full_image_link)

	#hemisphere_image_urls = []

	#for x in range (0, len(title_list)):
		#hemisphere_dict = {"title": title_list[x], "img_url": url_list[x]}
		#hemisphere_image_urls.append(hemisphere_dict)

	#mars_dict["hemisphere_image_urls"] = hemisphere_image_urls

	return mars_dict