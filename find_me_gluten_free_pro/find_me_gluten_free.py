import csv
from html.parser import HTMLParser
from itertools import count
from tkinter import N
from bs4 import BeautifulSoup
from numpy import empty
import requests
def write_output(data):
	with open('findmeglutenfree_page_21.csv', mode='w',newline="", encoding="utf-8") as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["restaurant_name","restaurant_addrs","restaurant_phone_no","restaurant_website","free_menu","restaurant_category","page_url"])
		for row in data:
			writer.writerow(row)
def fetch_data():
    url ="https://www.findmeglutenfree.com/sitemaps/21"
    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')
    for links in soup.find_all('loc'):
        link = links.text
        if link == 'https://www.findmeglutenfree.com/biz/garçons-/6133877075345408' or link == 'https://www.findmeglutenfree.com/biz/abhiruchi/6132731004715008':
            continue
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "max-age=0",
            "cookie": "_ga=GA1.2.543498385.1655902663; _gid=GA1.2.1241568782.1655902663; JSESSIONID=kKW_K8Z4RyELvZ1ClCFzHw; numUses=53; _gat_gtag_UA_19654560_1=1",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
        }
        response = requests.request("GET", link, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            restaurant_name = soup.find('div',{"class":"col-md-6 col-lg-7 col-xl-8"}).find('h1').text.replace('garçons-','garcons')
            print(restaurant_name)
        except:
            restaurant_name = ''
        try:
            restaurant_addrs = soup.find('div',{"style":"font-size:0.9rem;whitespace:pre-wrap;"}).text.strip()
        except:
            restaurant_addrs = ''
        try:
            restaurant_phone_no = soup.find_all('div',{"class":"mr-4"})[1].find('a').text
        except:
            restaurant_phone_no = ''
        if restaurant_phone_no != '':
            try:
                restaurant_website = soup.find_all('div',{"class":"mr-4"})[2].find('a').text
            except:
                restaurant_website = ''
        try:
            free_menu = soup.find_all('div',{"class":"col-md-6"})[2].text.replace('Gluten-Free Features','').strip()
        except:
            free_menu = ''
        try:
            restaurant_category = soup.find_all('div',{"class":"col-md-6"})[3].text.replace('Categories','').strip()
        except:
            restaurant_category = ''
        try:
            page_url = links.text.replace('https://www.findmeglutenfree.com/biz/garçons-/6133877075345408','https://www.findmeglutenfree.com/biz/garcons/6133877075345408')
        except:
            page_url = ''
        store =[restaurant_name,restaurant_addrs,restaurant_phone_no,restaurant_website,free_menu,restaurant_category,page_url]
        yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()