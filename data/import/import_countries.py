import csv
import sqlite3

conn = sqlite3.connect('/home/iwk/src/data-pack/world-gdp.db')
c = conn.cursor()

with open("/home/iwk/src/data-pack/data.gdp.1.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data = row["Country Code"], row['\ufeff"Country Name"'] 
        print(data)
        conn.execute("INSERT INTO countries (CountryCode, CountryName) VALUES (?,?)", data)
    conn.commit()

conn.close()
