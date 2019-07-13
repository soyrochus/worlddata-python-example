import csv
import sqlite3

conn = sqlite3.connect('/home/iwk/src/worlddata-python-example/data/import/world-gdp.db')
c = conn.cursor()

with open("/home/iwk/src/worlddata-python-example/data/import/data.countries.csv", 'r', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data = row["CountryCode"], row["CountryName"], row["CountryCode2"], row["UNCode"] 
        print(data)
        conn.execute("INSERT INTO countries (CountryCode, CountryName, CountryCode2, UNCode) VALUES (?,?, ?, ?)", data)
    conn.commit()

conn.close()
