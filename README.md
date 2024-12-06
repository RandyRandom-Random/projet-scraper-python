# projet-scraper-python
# Scraper de Citations Web

## Description du Projet

Chttps://quotes.toscrape.com/)e script Python permet de scraper des citations à partir du site web "Quotes to Scrape" (. Il récupère les citations, leurs auteurs et leurs tags à travers plusieurs pages du site et les sauvegarde dans un fichier JSON.

## Prérequis

- Python 3.x
- Bibliothèques Python suivantes :
  - `requests`
  - `beautifulsoup4`
  - `html5lib`

## Installation des Dépendances

```bash
pip install requests beautifulsoup4 html5lib
cf requiement.txt
```

## Fonctionnalités

- Extraction des citations de plusieurs pages
- Récupération des informations suivantes pour chaque citation :
  - Texte de la citation
  - Nom de l'auteur
  - Tags associés
- Sauvegarde des données dans un fichier JSON

## Fonctionnement du Script

1. Le script commence par scraper la page principale du site de citations
2. Il parcourt ensuite toutes les pages disponibles (de la page 2 à 100)
3. Pour chaque page, il extrait :
   - Le texte de la citation
   - Le nom de l'auteur
   - Les tags associés
4. Les données sont consolidées dans une liste
5. La liste complète est sauvegardée dans un fichier JSON


Les pull requests sont les bienvenues. Pour des changements majeurs, ouvrez d'abord un ticket pour discuter des modifications proposées.
