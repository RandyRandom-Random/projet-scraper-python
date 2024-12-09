import os
import sqlite3
import helper_database



def database_create():
    db_path = 'Database/smartphones.db'

    if not os.path.exists('Database'):
        os.makedirs('Database')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('PRAGMA foreign_keys = ON;')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS PROPOSE (
        FK_Name TEXT,
        FK_title_model TEXT,
        price REAL,
        url_anonce TEXT,
        url_image TEXT,
        FOREIGN KEY(FK_title_model) REFERENCES SMARTPHONES(PK_title_model),
        FOREIGN KEY(FK_Name) REFERENCES VENDOR(PK_Name)
        )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS VENDOR (
        PK_Name TEXT PRIMARY KEY,
        url_vendor TEXT,
        currency TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS SMARTPHONES (
        PK_title_model TEXT PRIMARY KEY,
        brand TEXT,
        memory TEXT,
        color TEXT
    )
    ''')

    conn.commit()
    conn.close()
    menu()
    print("Database created successfully")


def menu():
    while True:
        print("\nMenu:")
        print("Eboyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
        print("2. Extract Data")
        print("3. Execute SQL Query")
        print("4. Exit")

        choice = input("Select an option (2 or 3 or 4): ")


        if choice == '2':
            print("Starting data extraction...")
            helper_database.extract_data()
            print("Data extraction complete.")

        elif choice == '3':
            helper_database.queries_SQL()


        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice, please select again.")


