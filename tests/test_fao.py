from worlddata import FaoData, Fao, GdpData

FAO_DB_PATH = 'data/world-fao-production.json'
DB_PATH = 'data/world-gdp.db'

def test_fao_instantiation():
    
    gdpdata = GdpData(DB_PATH)
    faodata = FaoData(FAO_DB_PATH, gdpdata)
    assert faodata is not None     

def test_fao_get_items():
    
    gdpdata = GdpData(DB_PATH)
    faodata = FaoData(FAO_DB_PATH, gdpdata)
    data = faodata.get_fao_items()
    assert  21477 == len(data) # total number of items 
    #assert str(14439018) == data[-1].population # Last item in list: Zimbabwe - 2018