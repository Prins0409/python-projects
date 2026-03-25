import csv
import requests
import json
from bs4 import BeautifulSoup

def write_output(data):
	with open('hotwater.csv', mode='a',newline="", encoding="utf-8") as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["name","phone","email","website","city","state","zipcode","address1","address2"])
		for row in data:
			writer.writerow(row)
def fetch_data():
    for data1 in open("yelp_target_zip_codes.csv",'r',encoding='utf-8'):
        print(data1.strip())
        url = "https://www.whmaas.com/api/serviceprovider/1/"+str(data1.strip())+"?maxreturn=9&searchdistances=100"
        headers = {
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }
        response = requests.request("GET", url, headers=headers)
        status_code = response.status_code
        if status_code == 200:
            json_data = json.loads(response.text)
            if json_data['results'] == None:
                continue
            for data in json_data['results']['Data']['Companies']:
                name = data['CompanyName']
                phone = data['Phone']
                email = data['Email']
                website = data['Website']
                if website == None:
                    website = ''
                city = data['City']
                state = data['State']
                zipcode = data['PostalCode']
                address1 = data['AddressOne']
                address2 = data['AddressTwo']
                print(name)
                store =[name,phone,email,website,city,state,zipcode,address1,address2]
                yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()