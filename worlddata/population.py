import csv
from statistics import mean

class PopulationData:        
    def __init__(self, path):
        self.countries = {}
        with open(path) as csv_population: 
            population = csv.DictReader(csv_population)
            for country in population:
                years = {}
                self.countries[country["Country Code"]] = years
                for year in range(1960, 2019):
                    years[str(year)] = country[str(year)]

    def get_all(self):
        return self.countries

    def get_range(self, sel_countries, sel_years=range(1960, 2019)):
        selected = {}
        for sel_country in sel_countries:
            selected[sel_country]= _select_years(self.countries[sel_country], sel_years)
        return selected    

    def _get_countries_tuples(self, sel_countries, sel_years):
        selected = self.get_range(sel_countries, sel_years)
        print(selected)
        res = []
        for country in selected.keys():
            for year, value in selected[country].items():
                res.append((country, year, value))
        return res

    def get_range_max(self, sel_countries, sel_years=range(1960, 2019)):
        selected = self._get_countries_tuples(sel_countries, sel_years)
        return max(selected, key=lambda item: int(item[2]))
    
    def get_range_min(self, sel_countries, sel_years=range(1960, 2019)):
        selected = self._get_countries_tuples(sel_countries, sel_years)
        return min(selected, key=lambda item: int(item[2]))

    def get_range_mean(self, sel_countries, sel_years=range(1960, 2019)):
        selected = [int(e[2]) for e in self._get_countries_tuples(sel_countries, sel_years)]
        return mean(selected)
        
def _select_years(years, sel_years):
        selected = {}
        for year in sel_years:
            selected[str(year)] = years[str(year)]
        return selected