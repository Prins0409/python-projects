import requests
import csv
from bs4 import BeautifulSoup
from encodings.utf_8 import encode
import json

def write_output(data):
	with open('government_job.csv', mode='a', newline="", encoding='utf-8') as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["job_Title","job_Address","job_Category","job_Department","job_Agency","job_Salary_min_to_max_per_hour","job_Number","job_Closing_Date","link_Announcement_page_url","page_url"])
		for row in data:
			writer.writerow(row)
def fetch_data():
    for i in range(1,4902):
        url = "https://www.governmentjobs.com/jobs?page="+str(i)+"&isTransfer=False&isPromotional=False"
        print(i)
        response = requests.request("GET", url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for links in soup.find_all("div",{"class":"share-button-group addthis_toolbox addthis_default_style sharethis-button-group hide"}):
            link = links.find("button")["data-url"]
            id = soup.find("ul",{"class":"unstyled job-listing-container"})
            for ids in id.find_all("li"):
                job__id = str(ids["data-job-id"])
                if job__id in link:
                    urls = (link.split(job__id)[0] + link.split("/")[4] + "?isFeatured=False").replace("https://www.governmentjobs.com/jobs","https://www.governmentjobs.com/jobInfo/jobDetails")
                    print(urls)
                    headers = {
                        'Accept': '*/*',
                        'ADRUM': 'isAjax:true',
                        'Connection': 'keep-alive',
                        'Cookie': 'ASP.NET_SessionId=33um2uy1w1mlvwwci3fsysru; __RequestVerificationToken=thK0V1HFf7YdEQzhtwp3YD0lZFmfBNjXApqj9UsSTHK-7HOW1rMcXtO2nDq1thlWuPSBNju4344tbk1wvdjef0HSVao1; fpestid=-mMoIrWxQ1B2RiRDfHYAPyN26cNdsDNQ7cyMncoEu2MIgNXDoykV-vk2tiaUgCX3K4Df5w; _ga=GA1.2.1823517637.1662642233; _gid=GA1.2.2097481894.1662642233; OptanonAlertBoxClosed=2022-09-08T13:03:55.723Z; _RCRTX03=f2fbae5a2f7611ed923d9b62d622d3a85d125635363f43f8a2a229880c878516; _RCRTX03-samesite=f2fbae5a2f7611ed923d9b62d622d3a85d125635363f43f8a2a229880c878516; __gsas=ID=b30f515955d6efd8:T=1662642346:S=ALNI_MZg-gUX4mHou1lnG3sm6fJDB4R5iQ; __gads=ID=45f460527b12c332-22482f4546d6000d:T=1662642346:RT=1662642346:S=ALNI_Ma7EjXfA6yjm7lmGVBTjRPQr-mQDg; __gpi=UID=0000099898ef9a3c:T=1662642346:RT=1662642346:S=ALNI_MaQWOnisUSI56kbLUFgn8JwBI4ljg; rx_jobid_a40f2b4c-d9f2-11e7-8bfd-cf0059c1cdfc=3569106; job-referrer=referrerUrl=https%3a%2f%2fwww.governmentjobs.com%2f&referrerDomain=; ADRUM=s=1662660266287&r=https%3A%2F%2Fwww.governmentjobs.com%2Fjobs%2F3569106-0%2Fspecial-education-assistant-2225%3Fhash%3D-504755526; ADRUM_BTa=R:31|g:9c1c74eb-ca04-40e7-9338-d1f22ae9e3fd|n:neogov_698146b0-2502-4182-8f0e-5f1fccb51173; SameSite=None; ADRUM_BT1=R:31|i:672520|e:175; __atuvc=13%7C36; __atuvs=631a243c5c477191003; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Sep+08+2022+23%3A34%3A31+GMT%2B0530+(India+Standard+Time)&version=6.26.0&isIABGlobal=false&hosts=&consentId=3e6820e7-299b-467c-9de8-ff2c14a5fd69&interactionCount=1&landingPath=NotLandingPage&groups=C0003%3A1%2CC0001%3A1%2CC0002%3A1%2CC0004%3A1&geolocation=IN%3BGJ&AwaitingReconsent=false; ASP.NET_SessionId=vdqqzaa2a43335t0hfpmbgd4; __RequestVerificationToken=sYZHbwBN8Nlu0o5-xHwNw6-Dbyp33MEGEtP4ef6-ttmeB4Tn2azLkB_lgnDTDeMwHViMEnorB4C3BXT8f31KuPuge_U1',
                        'Host': 'www.governmentjobs.com',
                        'Referer': 'https://www.governmentjobs.com/jobs/3569106-0/special-education-assistant-2225?keyword=&location=&pagetype=searchPage',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'Sec-Fetch-Dest': 'empty',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Site': 'same-origin',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
                        'X-Requested-With': 'XMLHttpRequest'
                        }
                    response1 = requests.request("GET", urls, headers=headers)
                    soup1 = BeautifulSoup(response1.text, 'html.parser')
                    data1 = soup1.find("script",{"type":"application/ld+json"}).next_element.split('"description"')[0].replace("\p","").replace("\r","").replace("\t","").replace("\n","")
                    data2 = soup1.find("script",{"type":"application/ld+json"}).next_element.split('"datePosted"')[1].replace("\p","").replace("\r","").replace("\t","").replace("\n","")
                    data = data1 + '"datePosted"' + data2
                    json_data = json.loads(data)
                    job_Title = json_data['title']
                    job_Address = json_data['jobLocation']['address']['addressLocality']
                    try:
                        job_Category = json_data['employmentType']
                    except:
                        job_Category = ''
                    try:
                        job_Department = soup1.find("div",{"class":"term-container"}).find_all("div",{"class":"term-block term-block-right"})[1].find("div",{"class":"span8"}).text.strip()
                    except:
                        job_Department = ''
                    try:
                        job_Agency = json_data['hiringOrganization']['name']
                    except:
                        job_Agency = ''
                    try:
                        job_Salary_min_to_max_per_hour = str(json_data['baseSalary']['value']['minValue']) + '$-' + str(json_data['baseSalary']['value']['maxValue']) + '$/' + json_data['baseSalary']['value']['unitText']
                    except:
                        job_Salary_min_to_max_per_hour = ''
                    try:
                        if soup1.find_all("div",{"class":"term-block term-block-left"})[2].find("div",{"class":"span4"}).text.strip() == "Job Number":
                            job_Number = soup1.find_all("div",{"class":"term-block term-block-left"})[2].find("div",{"class":"span8"}).text.strip()
                        else:
                            job_Number = ''
                    except:
                        job_Number = ''
                    try:
                        if soup1.find_all("div",{"class":"term-block term-block-left"})[2].find("div",{"class":"span4"}).text.strip() == "Closing date and time":
                            job_Closing_Date = soup1.find_all("div",{"class":"term-block term-block-left"})[2].find("div",{"class":"span8"}).text.strip()
                        elif soup1.find_all("div",{"class":"term-block term-block-left"})[2].find("div",{"class":"span4"}).text.strip() == "Job Number":
                            try:
                                if soup1.find_all("div",{"class":"term-block term-block-left"})[3].find("div",{"class":"span4"}).text.strip() == "Closing date and time":
                                    job_Closing_Date = soup1.find_all("div",{"class":"term-block term-block-left"})[3].find("div",{"class":"span8"}).text.strip()
                            except:
                                job_Closing_Date = ''
                        else:
                            job_Closing_Date = ''
                    except:
                        job_Closing_Date = ''
                    try:
                        link_Announcement_page_url = json_data['hiringOrganization']['sameAs']
                    except:
                        link_Announcement_page_url = ''
                    page_url = urls
                    store = [job_Title,job_Address,job_Category,job_Department,job_Agency,job_Salary_min_to_max_per_hour,job_Number,job_Closing_Date,link_Announcement_page_url,page_url]
                    yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()