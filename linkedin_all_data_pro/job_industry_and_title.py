import csv
from html.parser import HTMLParser
from itertools import count
from tkinter import N
from bs4 import BeautifulSoup
from numpy import empty
import requests
import json
from pymongo import MongoClient
from bson.json_util import dumps

# 0 to 25... job_industry_and_title.csv
# 26, 27 & 29 to 67... job_industry_and_title.csv

def write_output(data):
	with open('job_industry_and_title.csv', mode='a',newline="", encoding="utf-8") as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["full_name","phone_numbers","mobile_phone","personal_email","professional_email","industry","job_company_name","job_title","work_email","location_country","full_address","linkedin_url"])
		for row in data:
			writer.writerow(row)
            
CONNECTION_STRING = "mongodb://localhost:27017"
client = MongoClient(CONNECTION_STRING)
dbname = client['admin']
collection_name = dbname["67"]

def fetch_data():
    item_details = json.loads(dumps(list(collection_name.find({},{"full_name":1,"phone_numbers":1,"mobile_phone":1,"emails":1,"personal_email":1,"professional_email":1,"industry":1,"job_company_name":1,"job_title":1,"work_email":1,"location_country":1,"full_address":1,"location_street_address":1,"location_locality":1,"location_region":1,"location_postal_code":1,"linkedin_url":1}))))
    for item in item_details:
        if item['location_country'] != None:
            if "switzerland" in item['location_country'].lower() or "CH" == item['location_country'].lower() or "ch" == item['location_country'].lower():
                if item['industry'] != None:
                    if "insurance" in item['industry'].lower() or "hospital" in item['industry'].lower() or "health care" in item['industry'].lower() or "biotechnology" in item['industry'].lower() or "banking" in item['industry'].lower() or "hospitality" in item['industry'].lower() or "pharmaceuticals" in item['industry'].lower() or "education management" in item['industry'].lower() or "staffing" in item['industry'].lower() or "recruiting" in item['industry'].lower() or "automotive" in item['industry'].lower() or "information technology" in item['industry'].lower() or "fitness" in item['industry'].lower() or "health" in item['industry'].lower() or "wellness" in item['industry'].lower() or "restaurants" in item['industry'].lower() or "financial services" in item['industry'].lower() or "law practice" in item['industry'].lower() or "oil" in item['industry'].lower() or "energy" in item['industry'].lower() or "management consulting" in item['industry'].lower() or "telecommunications" in item['industry'].lower() or "internet" in item['industry'].lower() or "government administration" in item['industry'].lower() or "electrical manufacturing" in item['industry'].lower() or "electronic manufacturing" in item['industry'].lower() or "defense" in item['industry'].lower() or "space" in item['industry'].lower() or "mining" in item['industry'].lower() or "metals" in item['industry'].lower() or "computer software" in item['industry'].lower() or "public relations" in item['industry'].lower() or "public communications" in item['industry'].lower() or "retail" in item['industry'].lower() or "package delivery" in item['industry'].lower() or "freight delivery" in item['industry'].lower() or "computer hardware" in item['industry'].lower() or "airlines/aviation" in item['industry'].lower() or "consumer electronics" in item['industry'].lower() or "military" in item['industry'].lower() or "airlines" in item['industry'].lower() or "aviation" in item['industry'].lower() or "logistics" in item['industry'].lower() or "supply chain" in item['industry'].lower() or "mental health care" in item['industry'].lower() or "consumer goods" in item['industry'].lower() or "computer" in item['industry'].lower() or "network security" in item['industry'].lower() or "tourism" in item['industry'].lower() or "travel" in item['industry'].lower() or "leisure" in item['industry'].lower() or "casinos" in item['industry'].lower() or "gambling" in item['industry'].lower() or "aerospace" in item['industry'].lower() or "aviation" in item['industry'].lower() or "online media" in item['industry'].lower() or "commercial real estate" in item['industry'].lower() or "wholesale" in item['industry'].lower() or "mechanical engineering" in item['industry'].lower() or "industrial engineering" in item['industry'].lower() or "architecture" in item['industry'].lower() or "planning" in item['industry'].lower() or "investment banking" in item['industry'].lower() or "semiconductors" in item['industry'].lower() or "investment management" in item['industry'].lower() or "building materials" in item['industry'].lower() or "political organization" in item['industry'].lower() or "computer networking" in item['industry'].lower() or "industrial automation" in item['industry'].lower() or "film" in item['industry'].lower() or "motion pictures" in item['industry'].lower() or "services" in item['industry'].lower() or "information services" in item['industry'].lower() or "import" in item['industry'].lower() or "export" in item['industry'].lower() or "warehousing" in item['industry'].lower() or "nanotechnology" in item['industry'].lower() or "executive office" in item['industry'].lower() or "railroad manufacture" in item['industry'].lower() or "venture capital" in item['industry'].lower() or "private equity" in item['industry'].lower() or "animation" in item['industry'].lower() or "fund-raising" in item['industry'].lower() or "markets" in item['industry'].lower() or "capital" in item['industry'].lower() or "capital markets" in item['industry'].lower():           
                        if item['job_title'] != None:
                            if "manager" in item['job_title'].lower() or "real estate" in item['job_title'].lower() or "director" in item['job_title'].lower() or "senior" in item['job_title'].lower() or "owner" in item['job_title'].lower() or "cxo" in item['job_title'].lower() or "manager,senior" in item['job_title'].lower() or "owner,cxo" in item['job_title'].lower() or "partner" in item['job_title'].lower() or "manager,cxo" in item['job_title'].lower() or "manager,vp" in item['job_title'].lower() or "vp" in item['job_title'].lower() or "manager,owner" in item['job_title'].lower() or "vp,cxo" in item['job_title'].lower() or "cxo,partner" in item['job_title'].lower() or "owner,partner" in item['job_title'].lower() or "director,owner" in item['job_title'].lower() or "director,cxo" in item['job_title'].lower() or "senior,vp" in item['job_title'].lower() or "senior,director" in item['job_title'].lower() or "manager,director" in item['job_title'].lower() or "manager,senior,vp" in item['job_title'].lower() or "senior,vp,cxo" in item['job_title'].lower() or "manager,senior,partner" in item['job_title'].lower() or "director,senior,vp" in item['job_title'].lower() or "manager,owner,partner" in item['job_title'].lower() or "senior,partner" in item['job_title'].lower() or "senior,owner" in item['job_title'].lower() or "senior,cxo" in item['job_title'].lower() or "vp,owner" in item['job_title'].lower() or "vp,partner" in item['job_title'].lower() or "senior,entry" in item['job_title'].lower() or "director,partner" in item['job_title'].lower() or "manager,owner,cxo" in item['job_title'].lower() or "director,entry" in item['job_title'].lower() or "director,vp" in item['job_title'].lower() or "manager,director,owner" in item['job_title'].lower() or "manager,unpaid" in item['job_title'].lower() or "manager,senior,director" in item['job_title'].lower() or "manager,partner" in item['job_title'].lower() or "manager,cxo,partner" in item['job_title'].lower() or "manager,senior,cxo" in item['job_title'].lower() or "director,owner,cxo" in item['job_title'].lower() or "senior,owner,cxo" in item['job_title'].lower() or "manager,senior,owner" in item['job_title'].lower() or "senior,director,partner" in item['job_title'].lower() or "vp,owner,cxo" in item['job_title'].lower() or "senior,cxo,partner" in item['job_title'].lower() or "director,owner,partner" in item['job_title'].lower() or "owner,cxo,partner" in item['job_title'].lower() or "manager,unpaid,owner" in item['job_title'].lower() or "manager,senior,director,partner" in item['job_title'].lower() or "senior,owner,partner" in item['job_title'].lower() or "senior,vp,partner" in item['job_title'].lower() or "senior,director,cxo" in item['job_title'].lower() or "manager,senior,training" in item['job_title'].lower() or "director,training" in item['job_title'].lower():
                                location_street_address = ''
                                if item['location_street_address'] != None:
                                    location_street_address = str(item['location_street_address']).replace("None",'')
                                location_locality = ''
                                if item['location_locality']:
                                    if len(location_street_address) == 0:
                                        location_locality = str(item['location_locality']).replace("None",'')
                                    else:
                                        location_locality = ', '+ str(item['location_locality']).replace("None",'')
                                location_region = ''
                                if item['location_region']:
                                    if len(location_locality) == 0 and len(location_locality) == 0:
                                        location_region = str(item['location_region']).replace("None",'')
                                    else:
                                        location_region = ", "+str(item['location_region']).replace("None",'')
                                location_postal_code = ''
                                if item['location_postal_code']:
                                    if str(len(location_street_address)) == 0 and len(location_locality) == 0 and len(location_locality)==0:
                                        location_postal_code =  str(item['location_postal_code']).replace("None",'')
                                    else:
                                        location_postal_code = ', '+ str(item['location_postal_code']).replace("None",'')
                                full_address =   location_street_address + location_locality +location_region + location_postal_code
                                full_name = str(item['full_name']).replace("None",'')
                                phone_numbers = str(item['phone_numbers']).replace("None",'')
                                phone_no = item['phone_numbers']
                                if phone_no == str([]):
                                    continue
                                all_phone_no = []
                                for phone_number in phone_no:
                                    all_phone_no.append(phone_number)
                                phone_numbers = ",".join(all_phone_no)
                                mobile_phone = str(item['mobile_phone']).replace("None",'')
                                emails = item['emails']
                                if emails == str([]):
                                    continue
                                personal_email2 = []
                                professional_email2 = []
                                for email in emails:
                                    if email['type'] == None or email['type'] == 'personal':
                                        personal_email1 = email['address']
                                        personal_email2.append(personal_email1)
                                    elif email['type'] == 'professional' or email['type'] == 'current_professional':
                                        professional_email1 = email['address']
                                        professional_email2.append(professional_email1)
                                personal_email = ",".join(personal_email2)
                                professional_email = ",".join(professional_email2)
                                industry = str(item['industry']).replace("None",'')
                                job_company_name = str(item['job_company_name']).replace("None",'')
                                job_title = str(item['job_title']).replace("None",'')
                                work_email = str(item['work_email']).replace("None",'')
                                location_country = str(item['location_country']).replace("None",'')
                                linkedin_url = str(item['linkedin_url']).replace("None",'')
                                print(full_name)
                                store =[full_name,phone_numbers,mobile_phone,personal_email,professional_email,industry,job_company_name,job_title,work_email,location_country,full_address.strip(),linkedin_url]
                                yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()