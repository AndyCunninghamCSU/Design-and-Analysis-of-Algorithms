# Andrew Cunningham
# CSC506 Critical Thinking Assignment 1
# Linear Search

# implements a linear search
# utilizes a GUI interface and a sqlite3 database

import sqlite3
import os

import tkinter as tk
from gui import gui

'''
# database creation code, no longer used.
# now I throw an exception if the database is unaccessible
os.makedirs("data", exist_ok=True)

conn = sqlite3.connect("data/marketplace.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        transaction_id INTEGER PRIMARY KEY,
        date TEXT,
        product_category TEXT,
        product_name TEXT,
        units_sold INTEGER,
        unit_price REAL,
        total_revenue REAL,
        region TEXT,
        payment_method TEXT
)
""")

conn.commit()
conn.close()
'''
categories = [
    "transaction_id", 
    "date", "product_category", 
    "product_name", "units_sold", 
    "unit_price", "total_revenue", 
    "region", "payment_method"
]

# throw an exception if the database is not available
if not os.path.exists("data/marketplace.db"):
    raise FileNotFoundError("Database not found.")

def handle_gui_callback(category, query):
    '''recieves the inputs from the gui, performs the search, and calls the gui to display'''
    print(f"Category: {category}")
    print(f"Query: {query}")


    # implementation one: linear search
    # selects everything from the database and iterates through the rows looking
    # for the desired results

    # connect to the database
    conn = sqlite3.connect("data/marketplace.db")
    cursor = conn.cursor()

    sql_command = f"SELECT * FROM sales"
    cursor.execute(sql_command)
    sql_results = cursor.fetchall()

    col_index = categories.index(category)

    matches = []
    for row in sql_results:
        if str(row[col_index]) == query:
            matches.append(row)

    app.update_results(matches)

    # implementation two
    # Although this is technically the correct way to do this, the assignment demands
    # an implementation of linear search.  This code will remain, commented out, to
    # demonstrate the more technically correct way
    '''
    # connect to the database
    conn = sqlite3.connect("data/marketplace.db")
    cursor = conn.cursor()

    sql_command = f"SELECT * FROM sales WHERE {category} LIKE ?"

    # add a wildcard to prevent SQL injection
    cursor.execute(sql_command, ("%" +  query + "%",))

    sql_results = cursor.fetchall()

    conn.close()

    app.update_results(sql_results)'
    '''

def main():
    '''creates and runs the gui'''
    root = tk.Tk()
    global app 
    app = gui(root, handle_gui_callback, categories)
    root.mainloop()

if __name__ == "__main__":
    main()
