import csv
from bs4 import BeautifulSoup
import requests
import re
import json
def write_output(data):
	with open('eventLocation.csv', mode='w',newline="", encoding="utf-8") as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["name","area","city_country","email","phone_number","web_url"])
		for row in data:
			writer.writerow(row)
def fetch_data():
    for i in range(0,1000):
        headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "en-US,en;q=0.9",
        "cookie": "PHPSESSID=5jvn650qpndprb91eeqceprvl4; uniqueId=695234c64963d996996cf2edf7697b17; cookieOK=1; _gcl_au=1.1.923668858.1654504164; _ga=GA1.2.1720061697.1654504164; _gid=GA1.2.57140228.1654504164; _dc_gtm_UA-58879794-2=1",
        "referer": "https://hochzeitshero.de/hochzeitslocations/muenchen?page=3",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
        }
        headers2 = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "max-age=0",
        "cookie": "PHPSESSID=5jvn650qpndprb91eeqceprvl4; uniqueId=695234c64963d996996cf2edf7697b17; cookieOK=1; _gcl_au=1.1.923668858.1654504164; _ga=GA1.2.1720061697.1654504164; _gid=GA1.2.57140228.1654504164",
        "referer": "https://hochzeitshero.de/hochzeitslocations/muenchen",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
        }
        url = "https://hochzeitshero.de/hochzeitsauto/muenchen?page="+str(i)+""
        response = requests.request("GET", url, headers=headers)
        soup = BeautifulSoup(response.text,'lxml')
    
        for link1 in soup.find_all('figure', {"class":"card-image"}):
            web_url = link1.find('a')['href']
            url2 = web_url
            response2 = requests.request("GET", url2, headers=headers2)
            soup2 = BeautifulSoup(response2.text,'lxml')
            name = soup2.find('h1', {"class":"title is-size-3 has-text-weight-bold has-text-dark is-inline-block"}).text
            try:
                addr1 = soup2.find('li', {"class":"provider-details__item-column fit-content"})
                area = addr1.find_all('p')[1].text
            except:
                area = ''
            try:
                data = soup2.find('ul',{"class":"provider-details"})
                x = data.find('p').text
                y = x.replace("\n",'').strip().split()
                city_country = " ".join(y)
            except:
                city_country = ''
            try:
                email1 = soup2.find_all('li', {"class":"provider-details__item-column fit-content"})[1]
                email = email1.find('p').next_element.next_element.text
            except:
                email = ''
            try:
                phone_number = soup2.find('span', {"class":"hidden-phone"}).next_element.next_element['phone']
            except:
                phone_number = ''
            store =[name, area, city_country, email, phone_number, web_url]
            yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()