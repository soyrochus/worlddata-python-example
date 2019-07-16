from worlddata import GdpData, Gdp

DB_PATH = 'data/world-gdp.db'

def test_gdp_instantiation():
    gdp = GdpData(DB_PATH)
    assert gdp is not None     

def test_gdp_get_countries():
    gdp = GdpData(DB_PATH)
    countries = gdp.get_countries()
    assert 247 == len(countries) # total number of countries
    assert 'ABW' == countries[0].CountryCode   # First item in list: Aruba
    assert 'Aruba' == countries[0].CountryName
    assert 'AW' == countries[0].CountryCode2
    assert '533' == countries[0].UNCode
    assert 'ZWE' == countries[-1].CountryCode # Last item in list: Zimbabwe

def test_gdp_get_all():
    gdp = GdpData(DB_PATH)
    data = gdp.get_all()

    assert 264 == len(data.keys()) # total number of countries
    
    total = 0
    for e in data.values():
        total += len(e.values()) 
    assert 15576 == total


def test_gdp_filter_data():
    gdp = GdpData(DB_PATH)
    data = gdp.get_range(('NLD', 'ESP'), range(1990, 1992))
             
    {'gdp': 318330511920.61, 'growth': 4.18322281189747} == data['NLD']['1990']	
    {'gdp': 327500328264.969, 'growth': 2.43913450352082} == data['NLD']['1991']	

    {'gdp': 535101248775.71, 'growth': 3.78139346477435} == data['ESP']['1990']	
    {'gdp': 575598537069.656, 'growth': 2.54600056787201} == data['ESP']['1991']	
    