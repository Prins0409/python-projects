import csv
import requests
import json
from bs4 import BeautifulSoup

def write_output(data):
	with open('heil_hvac.csv', mode='w',newline="", encoding="utf-8") as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["name","address","city","state","zipcode","country","phone","fax"])
		for row in data:
			writer.writerow(row)
def fetch_data():
    for data1 in open("yelp_target_zip_codes.csv",'r',encoding='utf-8'):
        print(data1.strip())
        url = "https://www.heil-hvac.com/en/us/ICPDealerLocator/FindDealers/"
        payload = '{"txtZipCodeOrCityState":"'+str(data1.strip())+'","searchRadius":"25"}'
        headers = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5,gu;q=0.4,de;q=0.3",
        "content-length": "53",
        "content-type": "application/json",
        "cookie": "heil_Language=en; heil_Location=us; heil_Parent=; heil_en_us_IsVisited=True; TAFSessionId=tridion_5499be16-c2df-477c-b441-454259839351; ASP.NET_SessionId=ctee1qoqe0h5mdgbdh11boqp; _gcl_au=1.1.156410338.1670650222; notice_preferences=0:; notice_gdpr_prefs=0:; cmapi_gtm_bl=ga-ms-ua-ta-asp-bzi-sp-awct-cts-csm-img-flc-fls-mpm-mpr-m6d-tc-tdc; cmapi_cookie_privacy=permit 1 required; heil_Zipcode=10001; heil_State=NY; heil_City=Manhattan; _ga_1BFPS3YXP0=GS1.1.1670670038.2.0.1670670038.0.0.0; notice_behavior=implied,us; _gid=GA1.2.1173303103.1670826567; _ga=GA1.2.1323565684.1670650223; _gat_UA-21736805-10=1; _ga_VYNSL2WTH6=GS1.1.1670841514.4.1.1670842797.0.0.0",
        "origin": "https://www.heil-hvac.com",
        "referer": "https://www.heil-hvac.com/en/us/find-a-dealer/",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        json_data = json.loads(response.text)
        for item in json_data['DealerList']:
            name = item['dealerName']
            address = item['address']
            city = item['city']
            state = item['stateProv']
            zipcode = item['postalCode']
            country = item['country']
            phone = item['phone']
            fax = item['fax']
            print(name)
            store =[name,address,city,state,zipcode,country,phone,fax]
            yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()