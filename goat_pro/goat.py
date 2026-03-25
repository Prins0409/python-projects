import requests
import csv
from bs4 import BeautifulSoup
import json

def write_output(data):
	with open('goat.csv', mode='a', newline="", encoding='utf-8') as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["title","available_or_not","data_id","sku","slug","color","category","image_url","release_date","product_type","release_date_year","variation_id","product_condition","count_for_product_condition","gp_lowest_price_cents_3","retail_price_cents","lowest_price_cents","instant_ship_lowest_price_cents","retail_price_cents_cad","retail_price_cents_aud","retail_price_cents_hkd","retail_price_cents_gbp","retail_price_cents_jpy","retail_price_cents_eur","retail_price_cents_twd","retail_price_cents_krw","retail_price_cents_myr","retail_price_cents_cny","retail_price_cents_sgd","lowest_price_cents_cad","lowest_price_cents_aud","lowest_price_cents_hkd","lowest_price_cents_gbp","lowest_price_cents_jpy","lowest_price_cents_eur","lowest_price_cents_twd","lowest_price_cents_krw","lowest_price_cents_myr","lowest_price_cents_cny","lowest_price_cents_sgd","instant_ship_lowest_price_cents_cad","instant_ship_lowest_price_cents_aud","instant_ship_lowest_price_cents_hkd","instant_ship_lowest_price_cents_gbp","instant_ship_lowest_price_cents_jpy","instant_ship_lowest_price_cents_eur","instant_ship_lowest_price_cents_twd","instant_ship_lowest_price_cents_krw","instant_ship_lowest_price_cents_myr","instant_ship_lowest_price_cents_cny","instant_ship_lowest_price_cents_sgd","page_url"])
		for row in data:
			writer.writerow(row)

# 417/418 something pages...

def fetch_data():
    count = 1
    while True:
        print(count)
        url = "https://ac.cnstrc.com/browse/group_id/sneakers?c=ciojs-client-2.29.12&key=key_XT7bjdbvjgECO5d8&i=c3beb311-5411-4c78-9d75-cfc911102c6b&s=2&page="+str(count)+"&num_results_per_page=24&fmt_options%5Bhidden_fields%5D=gp_lowest_price_cents_3&fmt_options%5Bhidden_fields%5D=gp_instant_ship_lowest_price_cents_3&fmt_options%5Bhidden_facets%5D=gp_lowest_price_cents_3&fmt_options%5Bhidden_facets%5D=gp_instant_ship_lowest_price_cents_3&_dt=1672036515242"
        headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        }
        count += 1
        response = requests.request("GET", url, headers=headers)
        if response.status_code != 200:
            break
        json_data = json.loads(response.text)

        for datas in json_data["response"]["results"]:
            title = datas["value"]
            print(title)
            available_or_not = str(datas["is_slotted"])
            if available_or_not == "True":
                available_or_not = "Yes"
            elif available_or_not == "False":
                available_or_not = "No"
            else:
                available_or_not = available_or_not
            data_id = datas["data"]["id"]
            sku = datas["data"]["sku"]
            slug = datas["data"]["slug"]
            color = datas["data"]["color"]
            category = datas["data"]["category"]
            image_url = datas["data"]["image_url"]
            try:
                release_date = datas["data"]["release_date"]
            except:
                release_date = ''
            product_type = datas["data"]["product_type"]
            try:
                release_date_year = datas["data"]["release_date_year"]
            except:
                release_date_year = ''
            variation_id = datas["data"]["variation_id"]
            try:
                product_condition = datas["data"]["product_condition"]
            except:
                product_condition = ''
            try:
                count_for_product_condition = datas["data"]["count_for_product_condition"]
            except:
                count_for_product_condition = ''
            try:
                gp_lowest_price_cents_3	= datas["data"]["gp_lowest_price_cents_3"]
            except:
                gp_lowest_price_cents_3 = ''
            try:
                retail_price_cents = datas["data"]["retail_price_cents"]
            except:
                retail_price_cents = ''
            try:
                lowest_price_cents = datas["data"]["lowest_price_cents"]
            except:
                lowest_price_cents = ''
            try:
                instant_ship_lowest_price_cents = datas["data"]["instant_ship_lowest_price_cents"]
            except:
                instant_ship_lowest_price_cents = ''
            try:
                retail_price_cents_cad = datas["data"]["retail_price_cents_cad"]
            except:
                retail_price_cents_cad = ''
            try:
                retail_price_cents_aud = datas["data"]["retail_price_cents_aud"]
            except:
                retail_price_cents_aud = ''
            try:
                retail_price_cents_hkd = datas["data"]["retail_price_cents_hkd"]
            except:
                retail_price_cents_hkd = ''
            try:
                retail_price_cents_gbp = datas["data"]["retail_price_cents_gbp"]
            except:
                retail_price_cents_gbp = ''
            try:
                retail_price_cents_jpy = datas["data"]["retail_price_cents_jpy"]
            except:
                retail_price_cents_jpy = ''
            try:
                retail_price_cents_eur = datas["data"]["retail_price_cents_eur"]
            except:
                retail_price_cents_eur = ''
            try:
                retail_price_cents_twd = datas["data"]["retail_price_cents_twd"]
            except:
                retail_price_cents_twd = ''
            try:
                retail_price_cents_krw = datas["data"]["retail_price_cents_krw"]
            except:
                retail_price_cents_krw = ''
            try:
                retail_price_cents_myr = datas["data"]["retail_price_cents_myr"]
            except:
                retail_price_cents_myr = ''
            try:
                retail_price_cents_cny = datas["data"]["retail_price_cents_cny"]
            except:
                retail_price_cents_cny = ''
            try:
                retail_price_cents_sgd = datas["data"]["retail_price_cents_sgd"]
            except:
                retail_price_cents_sgd = '' 
            try:
                lowest_price_cents_cad = datas["data"]["lowest_price_cents_cad"]
            except:
                lowest_price_cents_cad = ''
            try:
                lowest_price_cents_aud = datas["data"]["lowest_price_cents_aud"]
            except:
                lowest_price_cents_aud = ''
            try:
                lowest_price_cents_hkd = datas["data"]["lowest_price_cents_hkd"]
            except:
                lowest_price_cents_hkd = ''
            try:
                lowest_price_cents_gbp = datas["data"]["lowest_price_cents_gbp"]
            except:
                lowest_price_cents_gbp = ''
            try:
                lowest_price_cents_jpy = datas["data"]["lowest_price_cents_jpy"]
            except:
                lowest_price_cents_jpy = ''
            try:
                lowest_price_cents_eur = datas["data"]["lowest_price_cents_eur"]
            except:
                lowest_price_cents_eur = ''
            try:
                lowest_price_cents_twd = datas["data"]["lowest_price_cents_twd"]
            except:
                lowest_price_cents_twd = ''
            try:
                lowest_price_cents_krw = datas["data"]["lowest_price_cents_krw"]
            except:
                lowest_price_cents_krw = ''
            try:
                lowest_price_cents_myr = datas["data"]["lowest_price_cents_myr"]
            except:
                lowest_price_cents_myr = ''
            try:
                lowest_price_cents_cny = datas["data"]["lowest_price_cents_cny"]
            except:
                lowest_price_cents_cny = ''
            try:
                lowest_price_cents_sgd = datas["data"]["lowest_price_cents_sgd"]
            except:
                lowest_price_cents_sgd = ''
            try:
                instant_ship_lowest_price_cents_cad = datas["data"]["instant_ship_lowest_price_cents_cad"]
            except:
                instant_ship_lowest_price_cents_cad = ''
            try:
                instant_ship_lowest_price_cents_aud = datas["data"]["instant_ship_lowest_price_cents_aud"]
            except:
                instant_ship_lowest_price_cents_aud = ''
            try:
                instant_ship_lowest_price_cents_hkd = datas["data"]["instant_ship_lowest_price_cents_hkd"]
            except:
                instant_ship_lowest_price_cents_hkd = ''
            try:
                instant_ship_lowest_price_cents_gbp = datas["data"]["instant_ship_lowest_price_cents_gbp"]
            except:
                instant_ship_lowest_price_cents_gbp = ''
            try:
                instant_ship_lowest_price_cents_jpy = datas["data"]["instant_ship_lowest_price_cents_jpy"]
            except:
                instant_ship_lowest_price_cents_jpy = ''
            try:
                instant_ship_lowest_price_cents_eur = datas["data"]["instant_ship_lowest_price_cents_eur"]
            except:
                instant_ship_lowest_price_cents_eur = ''
            try:
                instant_ship_lowest_price_cents_twd = datas["data"]["instant_ship_lowest_price_cents_twd"]
            except:
                instant_ship_lowest_price_cents_twd = ''
            try:
                instant_ship_lowest_price_cents_krw = datas["data"]["instant_ship_lowest_price_cents_krw"]
            except:
                instant_ship_lowest_price_cents_krw = ''
            try:
                instant_ship_lowest_price_cents_myr = datas["data"]["instant_ship_lowest_price_cents_myr"]
            except:
                instant_ship_lowest_price_cents_myr = ''
            try:
                instant_ship_lowest_price_cents_cny = datas["data"]["instant_ship_lowest_price_cents_cny"]
            except:
                instant_ship_lowest_price_cents_cny = ''
            try:
                instant_ship_lowest_price_cents_sgd = datas["data"]["instant_ship_lowest_price_cents_sgd"]
            except:
                instant_ship_lowest_price_cents_sgd = ''
            page_url = "https://www.goat.com/sneakers" + slug
            print(page_url)

            store = [title,available_or_not,data_id,sku,slug,color,category,image_url,release_date,product_type,release_date_year,variation_id,product_condition,count_for_product_condition,gp_lowest_price_cents_3,retail_price_cents,lowest_price_cents,instant_ship_lowest_price_cents,retail_price_cents_cad,retail_price_cents_aud,retail_price_cents_hkd,retail_price_cents_gbp,retail_price_cents_jpy,retail_price_cents_eur,retail_price_cents_twd,retail_price_cents_krw,retail_price_cents_myr,retail_price_cents_cny,retail_price_cents_sgd,lowest_price_cents_cad,lowest_price_cents_aud,lowest_price_cents_hkd,lowest_price_cents_gbp,lowest_price_cents_jpy,lowest_price_cents_eur,lowest_price_cents_twd,lowest_price_cents_krw,lowest_price_cents_myr,lowest_price_cents_cny,lowest_price_cents_sgd,instant_ship_lowest_price_cents_cad,instant_ship_lowest_price_cents_aud,instant_ship_lowest_price_cents_hkd,instant_ship_lowest_price_cents_gbp,instant_ship_lowest_price_cents_jpy,instant_ship_lowest_price_cents_eur,instant_ship_lowest_price_cents_twd,instant_ship_lowest_price_cents_krw,instant_ship_lowest_price_cents_myr,instant_ship_lowest_price_cents_cny,instant_ship_lowest_price_cents_sgd,page_url]
            yield store
            
def scrape():
    data = fetch_data()
    write_output(data)
scrape()
