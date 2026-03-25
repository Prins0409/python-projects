import requests
from bs4 import BeautifulSoup
import json, csv

def write_output(data):
	with open('local_surveyers_direct.csv', mode='a',newline="", encoding="utf-8") as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["company_name","contact_details","phone_number","company_website","address","service_provider","contact_position","page_url"])
		for row in data:
			writer.writerow(row)
def fetch_data():
	url = "https://www.localsurveyorsdirect.co.uk/directory-of-members"
	headers = {
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5,gu;q=0.4,de;q=0.3',
	'cookie': '_gid=GA1.3.176330442.1665060224; _gat_UA-20155413-1=1; _uetsid=839fa230457411ed9a1a8d093d38fc09; _uetvid=83a01cf0457411edbcf289a6c684eb5f; _ga_H0BTT1BQ7S=GS1.1.1665060224.1.1.1665060774.0.0.0; _ga=GA1.1.2144290711.1665060224',
	'if-none-match': '"1665038507-1"',
	'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': '"Windows"',
	'sec-fetch-dest': 'document',
	'sec-fetch-mode': 'navigate',
	'sec-fetch-site': 'none',
	'sec-fetch-user': '?1',
	'upgrade-insecure-requests': '1',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
	}
	response = requests.request("GET", url, headers=headers)
	soup = BeautifulSoup(response.text, 'html.parser')
	data = soup.find("ul",{"class":"views-summary"})
	for sub_url in data.find_all("li"):
		url_end_point = sub_url.text.strip()
		urls = "https://www.localsurveyorsdirect.co.uk/directory-of-members/" + url_end_point
		headers1 = {
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5,gu;q=0.4,de;q=0.3',
		'cookie': '_gid=GA1.3.176330442.1665060224; _gat_UA-20155413-1=1; _ga_H0BTT1BQ7S=GS1.1.1665060224.1.1.1665061410.0.0.0; _uetsid=839fa230457411ed9a1a8d093d38fc09; _uetvid=83a01cf0457411edbcf289a6c684eb5f; _ga=GA1.1.2144290711.1665060224',
		'if-none-match': '"1665060268-1"',
		'referer': 'https://www.localsurveyorsdirect.co.uk/directory-of-members',
		'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'same-origin',
		'upgrade-insecure-requests': '1',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
		}
		response1 = requests.request("GET", urls, headers=headers1)
		soup1 = BeautifulSoup(response1.text, 'html.parser')
		for data in soup1.find_all("h2",{"class":"directory__title"}):
			url = data.find("a")["href"]
			page_url = "https://www.localsurveyorsdirect.co.uk" + url
			print(page_url)
			headers2 = {
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5,gu;q=0.4,de;q=0.3',
			'cookie': '_gid=GA1.3.176330442.1665060224; _gat_UA-20155413-1=1; _ga_H0BTT1BQ7S=GS1.1.1665060224.1.1.1665061800.0.0.0; _uetsid=839fa230457411ed9a1a8d093d38fc09; _uetvid=83a01cf0457411edbcf289a6c684eb5f; _ga=GA1.1.2144290711.1665060224',
			'if-none-match': '"1665060494-1"',
			'referer': 'https://www.localsurveyorsdirect.co.uk/directory-of-members/0',
			'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
			'sec-ch-ua-mobile': '?0',
			'sec-ch-ua-platform': '"Windows"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'same-origin',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
			}
			response2 = requests.request("GET", page_url, headers=headers2)
			soup2 = BeautifulSoup(response2.text, 'html.parser')
			company_name = soup2.find("h1",{"class":"main__page-title page-title"}).text.strip().replace("You are here: ","").replace("1787326444","KHA Architectural Design").replace('"99:40"',"'99:40'")
			all_data = soup2.find("div",{"class":"directory__contact-details"})
			datas = str(all_data).split("</h3>")[1].split("<h3>")[0].strip()
			soup3 = BeautifulSoup(datas, 'html.parser')
			try:
				phone_number = soup3.find_all("p")[1].text.split("http")[0].strip()
			except:
				phone_number = ''
			try:
				if "http" in soup3.find_all("p")[1].text:
					try:
						for_company_website = soup3.find_all("p")[1].text.split("http")[1].strip()
						if ":" in for_company_website:
							company_website = "http" + for_company_website
					except:
						company_website = ''
				elif "http" in soup3.find_all("p")[2].text:
					try:
						for_company_website = soup3.find_all("p")[2].text.split("http")[1].strip()
						if ":" in for_company_website:
							company_website = "http" + for_company_website
					except:
						company_website = ''
				else:
					company_website = ''
			except:
				company_website = ''
			all_data1 = soup2.find("div",{"class":"directory__contact-details"}).text
			address = all_data1.split("Address")[1].split("Services provided")[0].strip()
			service_provider = all_data1.split("and/or contact details")[1].strip()
			all_data2 = soup2.find("div",{"class":"directory__contact-details"}).find("p")
			contact_details = all_data2.text.split("0")[0].split("1")[0].split("2")[0].split("3")[0].split("4")[0].split("5")[0].split("6")[0].split("7")[0].split("8")[0].split("9")[0].strip()
			try:
				contact_position = all_data2.text.split(",")[1].strip()
			except:
				contact_position = ''
			store =[company_name,contact_details,phone_number,company_website,address,service_provider,contact_position,page_url]
			yield store
def scrape():
	data = fetch_data()
	write_output(data)
scrape()


