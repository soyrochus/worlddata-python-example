import json
from statistics import mean

class FaoData:
    
    def __init__(self, path, db):

        mapping3, mapping2 = db.get_countries_mapping()

        self.countries = {}
        with open(path, "r") as read_file:
            items = json.load(read_file)
            for item in items:
                countrycode = mapping2[item["Area Abbreviation"]].CountryCode
                country = self.countries.get(countrycode, {})
                product = {}
                product["ItemCode"] =  item["Item Code"]
                product["Item"] = item["Item"]
                product["ElementCode"] = item ["Element Code"]
                product["Element"] = item["Element"] 
                product["Unit"] = item["Unit"] 
                for year in range(1961, 2014):
                    product[str(year)] = item["Y" + str(year)]

                country[str(item["Item Code"])] = product
                self.countries[countrycode] = country

    def get_all(self):
        return self.countries

    def get_range(self, sel_countries, sel_item_codes, sel_years=range(1961, 2014)):
        selected = {}
        for sel_country in sel_countries:
            selected[sel_country]= _select_items(self.countries[sel_country], sel_item_codes, sel_years)
        return selected    

    def _get_countries_tuples(self, sel_countries, sel_item_codes, sel_years):
        selected = self.get_range(sel_countries, sel_item_codes, sel_years)
    
        res = []
        for country in selected.keys():
            for item_code in selected[country].keys():
                for year in sel_years:
                    value = selected[country][item_code][str(year)]
                    res.append((country, item_code, str(year), value))

        return res

    def get_range_max(self, sel_countries, sel_item_codes, sel_years=range(1961, 2014)):
        selected = self._get_countries_tuples(sel_countries, sel_item_codes, sel_years)
        return max(selected, key=lambda item: int(item[3]))

    def get_range_min(self, sel_countries, sel_item_codes, sel_years=range(1961, 2014)):
        selected = self._get_countries_tuples(sel_countries, sel_item_codes, sel_years)
        return min(selected, key=lambda item: int(item[3]))

    def get_range_mean(self, sel_countries, sel_item_codes, sel_years=range(1961, 2014)):
        selected = [int(e[3]) for e in self._get_countries_tuples(sel_countries, sel_item_codes, sel_years)]
        return mean(selected)


def _select_items(country, sel_item_codes, sel_years):
        selected = {}
        for item_code in sel_item_codes:
            item_data = country[item_code]
            new_item = {}
            new_item["ItemCode"] =  item_data["ItemCode"]
            new_item["Item"] = item_data["Item"]
            new_item["ElementCode"] = item_data["ElementCode"]
            new_item["Element"] = item_data["Element"] 
            new_item["Unit"] = item_data["Unit"] 

            for year in sel_years:
                new_item[str(year)] = item_data[str(year)]

            selected[item_code] = new_item
        return selected