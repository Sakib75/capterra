from bs4 import BeautifulSoup
import requests
import json

headers={
    "accept": '*/*',
    "origin": "https://www.capterra.com",
    "referer": "https://www.capterra.com/",
    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
    }

def Product_info(product):
    product_name=product['product_name']
    product_url=product['product_url']
    rating=product['rating'] 
    s_description=product['short_desc']
    upc=product['upc_product_uuid']
    return [product_name, product_url, rating, s_description, upc]

res=requests.get('https://www.capterra.com/directoryPage/rest/v1/category?htmlName=ab-testing-software&rbr=false&countryCode=BD', headers=headers)
data = json.loads(res.text)
products = data['pageData']['categoryData']['products']

Records=[]
for product in products:
    Records.append(Product_info(product))

print(Records)

# soup=BeautifulSoup(response.text,"lxml")
# string=json.loads(str(soup.find_all('script')[11].contents[0]).split('window[\'SSR_BRIDGE_DATA\'] = ')[-1])
# products=string['pageData']['categoryData']['products']
# Records=[]
# for product in products:
#     Records.append(Product_info(product))


