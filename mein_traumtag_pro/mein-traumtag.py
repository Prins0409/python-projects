import csv
from html.parser import HTMLParser
from itertools import count
from tkinter import N
from bs4 import BeautifulSoup
import requests
import json

def write_output(data):
	with open('mein-traumtag.csv', mode='w',newline="", encoding="utf-8") as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["name","category","streetNumber_streetName","postalCode","city","country","region","phone","web_url"])
		for row in data:
			writer.writerow(row)

def fetch_data():
    for i in range(1,37):
        data = "lang=&search_keywords=&search_location=&search_categories%5B%5D=77&filter_job_type%5B%5D=&per_page=10&orderby=featured&order=DESC&page="+str(i)+"&show_pagination=true&form_data=search_keywords%3D%26search_categories%255B%255D%3D77%26search_region%3D0%26filter_job_type%255B%255D%3D%26search_sort%3D"
        headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "content-length": "289",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "cookie": "complianz_policy_id=15; _ga=GA1.2.1369017176.1654280898; _gid=GA1.2.1173022467.1654280898; cmplz_event_0=deny; complianz_consent_status=allow; cmplz_marketing=allow; _gat_UA-17707767-2=1",
        "origin": "https://mein-traumtag.de",
        "referer": "https://mein-traumtag.de/partybands-hochzeitssaenger",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
        }
        url = "https://mein-traumtag.de/jm-ajax/get_listings/"
        daata = requests.post(url, headers=headers, data=data)
        json_data = json.loads(daata.text)
        for item in json_data['listings']:
            name = item['object']['post_title']
            category = item['categoryName']
            try:
                streetNumber_streetName = item['json_ld']['address']['streetAddress']
            except:
                streetNumber_streetName = ''
            try:
                postalCode = item['json_ld']['address']['postalCode']
            except:
                postalCode = ''
            try:
                city = item['json_ld']['address']['addressLocality']
            except:
                city = ''
            try:
                country = item['json_ld']['address']['addressCountry']
            except:
                country = ''
            try:
                region = item['json_ld']['address']['addressRegion']
            except:
                region = ''
            phone = item['telephone']
            web_url = item['permalink']
            store =[name,category,streetNumber_streetName,postalCode,city,country,region,phone,web_url]
            yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()