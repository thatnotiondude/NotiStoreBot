import os
import requests

GUMROAD_API_URL = 'https://api.gumroad.com/v2/products'
ACCESS_TOKEN = os.getenv('GUMROAD_ACCESS_TOKEN')

def fetch_products():
    response = requests.get(GUMROAD_API_URL, params={'access_token': ACCESS_TOKEN})
    if response.status_code == 200:
        return response.json().get('products', [])
    else:
        return []

def search_templates(keyword):
    products = fetch_products()
    return [product for product in products if keyword.lower() in product['name'].lower()]
