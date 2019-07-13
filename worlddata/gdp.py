from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric
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

    def get_gdp(self):
        session = self.Session()
        query = session.query(Gdp).order_by(Gdp.CountryCode.asc())
        gdp = query.all()
        session.close()
        return gdp

class Country(Base):
    
    __tablename__ = 'countries'

    CountryCode = Column(String, primary_key=True)
    CountryName = Column(String)
    
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
