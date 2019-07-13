from worlddata import GdpData, Gdp

DB_PATH = 'data/world-gdp.db'

def test_gdp_instantiation():
    gdp = GdpData(DB_PATH)
    assert gdp is not None     

def test_gdp_get_countries():
    gdp = GdpData(DB_PATH)
    countries = gdp.get_countries()
    assert 264 == len(countries) # total number of countries
    assert 'ABW' == countries[0].CountryCode   # First item in list: Aruba
    assert 'ZWE' == countries[-1].CountryCode # Last item in list: Zimbabwe

def test_gdp_get_gdp():
    gdp = GdpData(DB_PATH)
    gdp = gdp.get_gdp()
    assert 15576 == len(gdp) # total number of countries
    
