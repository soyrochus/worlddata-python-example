import csv
import sqlite3

conn = sqlite3.connect('/home/iwk/src/data-pack/world-gdp.db')
c = conn.cursor()

csv_growth = open("/home/iwk/src/data-pack/data.gdp.1.csv") 
csv_gdp = open("/home/iwk/src/data-pack/data.gdp.2.csv") 

growth_reader = csv.DictReader(csv_growth)
gdp_reader = csv.DictReader(csv_gdp)

growth = {  e["Country Code"] : e for e in growth_reader }
gdp = {  e["Country Code"] : e for e in gdp_reader }

for country in growth:
    
    growth_item = growth[country]
    gdp_item = gdp[country]

    for i in range(1960, 2019):
        year = str(i)
        data = country, year, gdp_item[year], growth_item[year]
        conn.execute("INSERT INTO gdp (CountryCode, Year, gdp, growth) VALUES (?, ?,?,?)", data)    
        print(country, year, data)

csv_gdp.close()
csv_growth.close()

conn.commit()
conn.close()
