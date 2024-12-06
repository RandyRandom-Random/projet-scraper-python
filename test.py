import requests
import os
import json

TotalPg = 0

def extract_data():

    maxPage = request_data(0)
    for i in range(1,maxPage):
        request_data(i)

def request_data(page):
    url = 'https://9x8zudunn9-dsn.algolia.net/1/indexes/prod_index_backbox_model_fr-fr/query?x-algolia-agent=Algolia%20for%20JavaScript%20(4.24.0)%3B%20Browser'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0',
        'Accept': '*/*',
        'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'x-algolia-api-key': "OGU0MzkxNGQ4YTA3NTk1YjcwOGIyMDMwOTgxNDMwM2YxOTMyMDVhODc2NTZkMjMxNjdmNDJkZTNhZDFlYTQ3OGF0dHJpYnV0ZXNUb1JldHJpZXZlPWJhY2tib3hfZ3JhZGVfbGFiZWwlMkNiYWNrYm94X2dyYWRlX3ZhbHVlJTJDYmFja21hcmtldElEJTJDYnJhbmQlMkNicmFuZF9jbGVhbiUyQ2NhbWVyYV9zY29yZSUyQ2NhdF9pZCUyQ2NhdGVnb3J5XzElMkNjYXRlZ29yeV8yJTJDY2F0ZWdvcnlfMyUyQ2NvbGxlY3Rpb25fYWklMkNjb2xvciUyQ2Nvbm5lY3RvciUyQ2N1cnJlbmN5JTJDZmFjZV9pZCUyQ2dsb2JhbF9zY29yZSUyQ2hkbWlfb3V0cHV0JTJDaWQlMkNpbWFnZTElMkNpcGFkX2Nvbm5lY3RvciUyQ2xpZmVfZXhwZWN0YW5jeV9zY29yZSUyQ2xpbmtfZ3JhZGVfdjIlMkNsaXN0X3ZpZXclMkNsaXN0aW5nSUQlMkNtZXJjaGFudF9pZCUyQ21vZGVsJTJDbW9kZWxfY2xlYW4lMkNtdWx0aW1lZGlhX3Njb3JlJTJDb2JqZWN0SUQlMkNwZXJmb3JtYW5jZXNfc2NvcmUlMkNwcmljZSUyQ3ByaWNlX25ldyUyQ3ByaWNlX3dpdGhfY3VycmVuY3klMkNwcmljZV9uZXdfd2l0aF9jdXJyZW5jeSUyQ3JlZmVyZW5jZVByaWNlJTJDcmV2aWV3UmF0aW5nJTJDc2NyZWVuX3F1YWxpdHlfc2NvcmUlMkNzaW1fbG9jayUyQ3NwZWNpYWxfb2ZmZXJfdHlwZSUyQ3N0b2NrUmF3JTJDc3ViX3RpdGxlX2VsZW1lbnRzJTJDdGl0bGUlMkN0aXRsZV9tb2RlbCUyQ3RvdWNoX2JhciUyQ3RvdWNoX2lkJTJDdmFyaWFudF9maWVsZHMlMkN3YXJyYW50eSZmaWx0ZXJzPU5PVCtiYWNrYm94X2dyYWRlX3ZhbHVlJTNEOSZyZXN0cmljdEluZGljZXM9cHJvZF8lMkE=",
        'x-algolia-application-id': '9X8ZUDUNN9',
        'content-type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.backmarket.fr',
        'Connection': 'keep-alive',
        'Referer': 'https://www.backmarket.fr/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site'
    }

    data = {
        "query": "",
        "distinct": 1,
        "clickAnalytics": True,
        "filters": "(cat_id:\"2\") AND (os:\"Android\") AND special_offer_type=0",
        "facets": [
            "price", "page", "q", "sort", "brand", "serie", "model", "year_date_release", "storage", "color", "network",
            "real_screen_size",
            "sim_lock", "double_sim", "real_screen_size", "backbox_grade", "payment_methods", "shipping_delay",
            "price_ranges.sm-1",
            "price_ranges.sm-2", "price_ranges.md-1", "price_ranges.md-1b", "price_ranges.md-1c", "price_ranges.md-2",
            "price_ranges.lg-1",
            "price_ranges.lg-2", "price_ranges.lg-3"
        ],
        "numericFilters": ["price>=0", "price<=2000"],
        "page": page,
        "hitsPerPage": 30
    }

    response = requests.post(url, headers=headers, json=data)
    file_path = f'C:/Users/projet-scraper-python/Scrapper/extract_data_{page+1}.json'  # Chemain
    file_path2 = f'C:/Users/projet-scraper-python/Scrapper/data_{page+1}.json'  # Chemain

    os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Faire le dossier
    datass = response.json()
    datass["facets"] = ""
    datass["facets_stats"] = ""

    new_list = []
    for data in datass['hits']:
        entry = {}
        entry['title_model'] = data['title_model']
        entry['brand'] = data['brand']
        entry['model'] = data['model']
        entry['price'] = data['price']
        entry['currency'] = data['currency']
        entry['href'] = data['link_grade_v2']['href']
        new_list.append(entry)

    with open(file_path, 'w') as f:  # extraction des donnée sous formas JSON
        json.dump(datass, f, indent=4)
    with open(file_path2, 'w') as f:  # extraction des donnée sous formas JSON
        json.dump(new_list, f, indent=4)
    return datass['nbPages']