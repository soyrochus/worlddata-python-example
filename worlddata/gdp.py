from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric
from statistics import mean
import csv

Base = declarative_base()

SQLITE_MEMORY_PATH = 'sqlite:///:memory:'
SQLITE_PATH_MASK = 'sqlite:///{}' 

def get_sqlite_resource(path):
    return SQLITE_PATH_MASK.format(path)


class GdpData:
    def __init__(self, path): 
        
        if path:
            self.engine = create_engine(get_sqlite_resource(path), echo=True)
        else:
            self.engine = create_engine(SQLITE_MEMORY_PATH)
        
        self.Session = sessionmaker(bind=self.engine)

    def get_countries(self):
        
        session = self.Session()
        query = session.query(Country).order_by(Country.CountryCode.asc())
        countries = query.all()
        session.close()
        return countries

    def get_all(self):
        session = self.Session()
        query = session.query(Gdp).order_by(Gdp.CountryCode.asc())
        data = query.all()
        session.close()
        selected = {}
        for e in data:
            country = selected.get(e.CountryCode, {})
            year = country.get(e.Year, {})
            year["gdp"] = e.gdp
            year["growth"] = e.growth
            country[e.Year] = year
            selected[e.CountryCode] = country
        return selected

    def get_range(self, sel_countries, sel_years=range(1960, 2019)):
        data = self.get_all()
        selected = {}
        for sel_country in sel_countries:
            selected[sel_country]= _select_years(data[sel_country], sel_years)
        return selected    

    def get_range_max(self, sel_countries, sel_years=range(1960, 2019), prop="gdp"):
        selected = self._get_countries_tuples(sel_countries, sel_years)
        return max(selected, key=lambda item: int(item[2][prop]))

    def get_range_min(self, sel_countries, sel_years=range(1960, 2019), prop="gdp"):
        selected = self._get_countries_tuples(sel_countries, sel_years)
        return min(selected, key=lambda item: int(item[2][prop]))

    def get_range_mean(self, sel_countries, sel_years=range(1960, 2019), prop="gdp"):
        selected = [int(e[2][prop]) for e in self._get_countries_tuples(sel_countries, sel_years)]
        return mean(selected)


    def _get_countries_tuples(self, sel_countries, sel_years):
        selected = self.get_range(sel_countries, sel_years)
        res = []
        for country in selected.keys():
            for year, value in selected[country].items():
                res.append((country, year, value))
        return res

def _select_years(years, sel_years):
        selected = {}
        for year in sel_years:
            selected[str(year)] = years[str(year)]
        return selected

class Country(Base):
    
    __tablename__ = 'countries'

    CountryCode = Column(String, primary_key=True)
    CountryName = Column(String)
    CountryCode2 = Column(String)
    UNCode = Column(String)
    
    def __repr__(self):
        return "<Country(CountryCode='%s', CountryName='%s')>" % (self.CountryCode, self.CountryName)

class Gdp(Base):
    __tablename__ = 'gdp'

    id = Column(Integer, primary_key=True)
    CountryCode = Column(String)
    Year = Column(String)
    gdp = Column(String)
    growth = Column(String)

    def __repr__(self):
        return "<Gdp(id='%s',CountryCode='%s', Year='%s', gdp='%s', growth='%s')>" \
            % (self.id, self.CountryCode, self.Year, self.gdp, self.growth)
