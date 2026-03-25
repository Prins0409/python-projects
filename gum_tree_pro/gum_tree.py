from bs4 import BeautifulSoup
import requests
import csv, json
import urllib.request
import bs4 as bs

def write_output(data):
	with open('gum_tree.csv', mode='a', newline="", encoding='utf-8') as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["title","property_dataa","address","latitude","longitude","currency","category","sub_category","description","sku_id","images","phone_no","property_type","seller_type","country","area","seller","seller_reply_phone","seller_user_id","seller_email","seller_website_url","seller_website_name","posted","page_url"])
		for row in data:
			writer.writerow(row)

def fetch_data():
    for i in range(1,51):
        print(i)
        try:
            url = "https://www.gumtree.com/flats-houses/uk"
        except:
            url = "https://www.gumtree.com/flats-houses/uk/page" + str(i)
        headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "cookie": "eCG_eh=ec=ResultsBrowse:ea=NavL1CategoryHoover:el=; gt_appBanner=; gt_adconsent=; gt_ab=ln:MjE0N3o=; gt_p=id:ZjU1ZjViMjctY2E5OS00OTU3LThlN2EtOGZlZjQ3MGIwYjhl; GCLB=CJKFivCx7OTzYA; gcl_au=1.1.2042384970.1671432143; ga=GA1.2.1354137800.1671432144; gid=GA1.2.128164431.1671432144; rbzid=YCep6X6u3emknWCcH/E54cvjn0VP2BdmGkqqGoBWTsNxhkZcS/qETi46KwULLM9pYfW0jGzYFX1GM0Tx6WAMtafjW9T8GQxINKL5GzNGH8M64oa3CpxpFUG4nOrlvTujIUlWNEC+asWy76LtD+LBYprnjPY3GCEt61K0Bz8t2d9SHTqm85ItWWu7L9SNU4yvde35C3mC1QA3MqQRio1CZoplEo7fK7whWUiliJfbU+EJi7X0lvMwEVonhFccZH5+5VUYYf5ZFkRRSiMffSuWnoaQtoIqJTBRn4n9YeGqg2Y=; rbzsessionid=05d5e23dbe344e3fba55557823c28b8b; OptanonAlertBoxClosed=2022-12-19T06:42:28.639Z; permutive-id=716314c1-d73d-4f88-8446-7f4566978171; pbjs_userid_consent_data=6810739461401722; pubcid=d7986dcb-f0f7-49e3-be47-9a672ad19298; eupubconsent-v2=CPkQE4gPkQE4gAcABBENCvCsAP_AAH_AAChQJMNf_X__b2_r-_5_f_t0eY1P9_7__-0zjhfdl-8N3f_X_L8X52M7vF36tq4KuR4ku3LBIUdlHOHcTUmw6okVryPsbk2cr7NKJ7PEmnMbOydYGH9_n1_z-ZKY7___f_7z_v-v________7-3f3__5___-__e_V__9zfn9_____9vP___9v-_9__________3_7997_HwSYAJMNW4gC7EscCbaMIoEQIwrCQ6gUAFFAMLRAYQOrgp2VwE-sIEACAUARgRAhwBRgwCAAACAJCIgJAjwQCAAiAQAAgAVCIQAEbAIKACwMAgAFANCxRigCECQgyICIpTAgIkSCgnsqEEoP9DTCEOssAKDR_xUICJQAhWBEJCwchwRICXiyQLMUb5ACMEKAUSoVqCT0gAA.f_gAD_gAAAAA; _gads=ID=8818d0c8aae62181:T=1671432150:S=ALNI_Mb8RgIamLSmfe3cv1AQtKlLGOVyhQ; _gpi=UID=00000b9357bd3621:T=1671432150:RT=1671432150:S=ALNI_MaGWCvWY0MbXEhnMbJX_rcU5Cy1Sw; cc_id=994771fdee48fb067b7282f40c123070; panoramaId_expiry=1671518551399; lr_env_src_ats=false; gt_userPref=isSearchOpen:dHJ1ZQ==|recentAdsOne:Y2Fycy12YW5zLW1vdG9yYmlrZXM=|cookiePolicy:dHJ1ZQ==|recentAdsTwo:Zm9yLXNhbGU=|location:dWs=; clck=n18pxo|1|f7j|0; fbp=fb.1.1671432258736.82198033; ki_r=; lux_uid=167144033649231061; lr_retry_request=true; OptanonConsent=isIABGlobal=false&datestamp=Mon+Dec+19+2022+14%3A44%3A00+GMT%2B0530+(India+Standard+Time)&version=6.10.0&hosts=&landingPath=NotLandingPage&groups=FACEB%3A1%2CLIVER%3A1%2CSTACK42%3A1%2CGOOGL%3A1%2CC0026%3A1%2CC0028%3A1%2CC0029%3A1%2CMICRO%3A1%2CC0023%3A1%2CGATPS%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0001%3A1&geolocation=IN%3BGJ&AwaitingReconsent=false; cto_bundle=OCnHpl9PT29keWxBUHNiNUplbFAlMkZQdWFvMyUyQkVuWnIzZlA5THlQWll1ZXBXMmNoaVRiRUZ4enpoTlRjN2ZlOG4lMkJhMTF1clZUT3RGZTJpcXdmQzlOcWdoYndTRXpNNzI0OXB3U3QlMkYlMkJkM3FnWSUyQm5FMHBBazRJZWFCWm81dlkxWmprWVFmSk1TMmtsSTJvZ2szam9XRGhKY0pVN3clM0QlM0Q; clsk=mdjghs|1671441241358|14|0|n.clarity.ms/collect; tq_id.TV-45818190-1.7ba1=5da98ed5b8b007b7.1671432420.0.1671441243..; ki_t=1671432418912%3B1671432418912%3B1671441242676%3B1%3B32; gt_s=sc:MTAyMDE=|ar:aHR0cDovL3d3dy5ndW10cmVlLmNvbS9mbGF0cy1ob3VzZXMvY3JpdGljYWwuY3NzLm1hcA==|st:MTY3MTQ0MTI2Mjg4Mw==|clicksource_featured:|sk:|bci:MEEwMkIwNjAxOTlCNkQ0ODNFRjVBMjFCMTg5RDZDMEQ=|clicksource_nearby:|id:bm9kZTAxa281Z3Ztcmh1ODl1MXMyY2kxa2plYml6MzM1MzYw|clicksource_natural:; gt_userIntr=cnt:MjM=",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }
        response = requests.request("GET", url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        for data in soup.find_all("a",{"class":"listing-link"}):
            urls = "https://www.gumtree.com" + data["href"]
            print(urls)
            response1 = requests.request("GET", urls, headers=headers)
            soup1 = BeautifulSoup(response1.text, 'html.parser')
            source = urllib.request.urlopen(urls).read()
            data1 = str(soup1.find_all("script",{"type":"application/ld+json"})[1]).replace('<script type="application/ld+json">',"").replace('</script>',"")
            json_data = json.loads(data1)
            property_datas = []
            for datas in json_data["itemListElement"]:
                property_data = datas["item"]["name"]
                property_datas.append(property_data)
            property_dataa = ", ".join(property_datas)
            soup2 = bs.BeautifulSoup(source, 'html.parser')
            data2 = []
            for daataa in soup2.find("body",{"data-q":"vip"}).find_all("script"):
                if "window.clientData =" in str(daataa):
                    lat_long = str(daataa).replace("<script>window.clientData = ","").replace(";</script>","")
                    data2.append(lat_long)
            data3 = "".join(data2)
            json_data1 = json.loads(data3)
            title = json_data1["page"]["title"].split("|")[0].strip()
            address = json_data1["page"]["title"].split("|")[1].split("|")[0].replace("in","").strip()
            latitude = json_data1["partnerships"]["latitude"]
            longitude = json_data1["partnerships"]["longitude"]
            try:
                price = json_data1["adDetails"]["price"]
            except:
                price = ''
            if price != '':
                currencies = price
            new_one = [word[0] for word in currencies.split()]
            currency = "".join(new_one)
            try:
                category = json_data1["adDetails"]["l1CategorySeoName"]
            except:
                category = ''
            try:
                sub_category = json_data1["adDetails"]["seoL1Category"] + ": " + json_data1["adDetails"]["seoL2Category"]
            except:
                sub_category = ''
            try:
                description = str(json_data1["adDetails"]["description"]).replace('[',"").replace(']',"").replace("'","").replace('\\r',"").strip().replace(", ,",",").replace(','," ")
            except:
                description = ''
            try:
                sku_id = json_data1["adDetails"]["id"]
            except:
                sku_id = ''
            try:
                images = str(json_data1["images"]).replace('[',"").replace(']',"").replace("'","")
            except:
                images = ''
            try:
                phone_no = json_data1["sellerContactDetails"]["replyPhone"]
            except:
                phone_no = ''
            try:
                property_type = json_data1["displayAds"]["config"]["targeting"]["property_type"]
            except:
                property_type = ''
            try:
                seller_type = json_data1["displayAds"]["config"]["targeting"]["seller_type"]
            except:
                seller_type = ''
            try:
                country = json_data1["displayAds"]["config"]["targeting"]["country"]
            except:
                country = ''
            try:
                area = json_data1["displayAds"]["config"]["targeting"]["area"]
            except:
                area = ''
            try:
                seller = json_data1["sellerContactDetails"]["contactName"]
            except:
                seller = ''
            try:
                seller_reply_phone = json_data1["sellerContactDetails"]["replyPhone"]
            except:
                seller_reply_phone = ''
            try:
                seller_user_id = json_data1["sellerContactDetails"]["sellerUserId"]
            except:
                seller_user_id = ''
            try:
                seller_email = json_data1["sellerContactDetails"]["replyEmail"]
            except:
                seller_email = ''
            try:
                seller_website_url = json_data1["sellerContactDetails"]["websiteUrl"]
            except:
                seller_website_url = ''
            try:
                seller_website_name = json_data1["sellerContactDetails"]["websiteName"]
            except:
                seller_website_name = ''
            try:
                posted = json_data1["adDetails"]["attributes"][0]["value"]
            except:
                posted = ''
            page_url = urls

            store =[title,property_dataa,address,latitude,longitude,currency,category,sub_category,description,sku_id,images,phone_no,property_type,seller_type,country,area,seller,seller_reply_phone,seller_user_id,seller_email,seller_website_url,seller_website_name,posted,page_url]
            yield store

def scrape():
    data = fetch_data()
    write_output(data)
scrape()
