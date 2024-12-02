import requests
from bs4 import BeautifulSoup
import json
import os
import html5lib

page = requests.get("https://quotes.toscrape.com/")

def extract_data(div_citations): #div_citation semble illogique mais il sert a stocker plus de variable comme author,tags et citation
    citation = div_citations.find('span',{'class':'text'}).get_text()
    author = div_citations.find('small',{'class':'author'}).get_text()
    tags = []
    for tag in div_citations.find_all('a',{'class':'tag'}):
        tags.append(tag.get_text())
    data = {
        'citation': citation,
        'author': author,
        'tags': tags, 
    }

    return data #les datas est sous forme de dictionnaire et sous forme de text (j'ai du préciseer sinon ca ne marche pas a cause des balise HTML)
    
def getquotes(pageUrl): #je crée une nouvelle variable pageUrl car je veux l'utiliser dans une boucle car j'en ai besoin pour y parcourir
    page = requests.get(pageUrl)
    parsedPage = BeautifulSoup(page.content, "html5lib")
    citations = parsedPage.find_all('div',{'class':'quote'})
    if len(citations)> 0:
        citations_list = []
        for citation in citations:
            citations_list.append(extract_data(citation))
        return citations_list
    else:
        return None
    
data = getquotes("https://quotes.toscrape.com/")
for i in range(2,100): #j'invente une liste imaginaire qui est va de 2 a 100
    #print(i) je teste le diffilement
    page_url = f'https://quotes.toscrape.com/page/{i}/'
    current_page_quotes = getquotes(page_url)
    if current_page_quotes is not None:
        data = data + current_page_quotes #liste de data de la première page puis avec uune nouvel page de data avec des maj plus complete qui l'écrase
    else:
        break
file_path = 'C:/Users/projet-scraper-python/data/scraper_exctract_infos.json' # Chemain
os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Faire le dossier

with open(file_path, 'w') as f: # extraction des donnée sous formas JSON
    json.dump(data, f)
    print("Download succesfully")
                                                                                                # f c'est la valeur de "with open('/home/turpin/Documents/Python/logique python/scraper_exctract_infos.json','w'"
                                                                                                    
#infos complémentaire :

"""
    current_page_quotes = getquotes(page_url)
    if current_page_quotes is not None:
        data = data + current_page_quotes

c'est comme cette exemple :

somme = 0
while True:  
    somme += 1 
    if somme == 10: 
        break  
"""
