# SCRAPPER-FOR-BACKMARKET




## Description of Project
This program can be run in the console (example: main.py), you just need to use two arguments: 'scrap' or 'database'.
If you choose "scrap" - the program will start scraping all Android smartphones from backmarket.fr.
If you choose "database" - the program will create a database with data from Backmarket where you can run your SQL queries.


## Requirements
- be Optimus Prime
- See requirements.txt

## How to install a requirements (for beginners like me)

```bash
pip install requests os argparse sqlite3 json
cf requiement.txt
```

## Functionality

- Extract all pages of Android smartphones from Backmarket
- Create a database
- Use SQL queries in the database
- Make you smile

## How it works
1. We start in the main file with an explanation of the program
2. In test.py, we have the logic for scraping, and this file gives you all pages in JSON format.
3. In database.py, we have a function that offers a menu, and this function creates a database. On Monday, I need to add the possibility to run SQL queries in the menu function.



You can modify this program if James opens this repository.