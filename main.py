import art
import argparse
import test
import database
# Joli texte
text = "Back Market Scrapper"
ascii_art = art.text2art(text)
# Config des parametre du programme
parser = argparse.ArgumentParser(
    description="Back Market Scrapper, the information about this program you can read in README.md")
parser.add_argument("mode", nargs="?", choices=["scrap", "database"], help="Chose yor mode: scrap or database")
args = parser.parse_args()
# Run sans arguments
if args.mode is None:
    print(ascii_art)
    print("Hello, I have two arguments: 'scrap' and 'database'.")
    print("You can use one of them to run the program.")
    print("For example: \n\t - python main.py scrap \n\t - python main.py database")
else:
    print(ascii_art)
    x = input("Do you want to start? Y or N: ")
    if x == "Y" or x == "y" or x == "Yes" or x == "YES" or x == "yes":
        if args.mode == "scrap":
            print("I start a Scrapping...")
            # ICI ON DOIT METTRE LE SCRAPEUR QUI RETOURNE LES DONNES EN JSON, ET ON LA MIS ALLELUYA
            test.extract_data()
        elif args.mode == "database":

            print("I create for you a Database...")
            database.database_create()
    else:
        print("Ok, good luck man :# ")


# add SQL request fo user
# add csv
#