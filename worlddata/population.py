import csv

def sort_key(item):
    return item.CountryCode + str(item.year)

class PopulationData:        
    def __init__(self, path):
        self.population = []
        csv_pops = open(path) 
        growth_pops = csv.DictReader(csv_pops)
        for country in growth_pops:
            for year in range(1960, 2019):
                self.population.append(Population(country["Country Code"], year, country[str(year)]))

    def get_all(self):
        return sorted(self.population, key=sort_key)

class Population:
    def __init__(self, CountryCode, year, population):        
        self.CountryCode = CountryCode
        self.year = year
        self.population = population
