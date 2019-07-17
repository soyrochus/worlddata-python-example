from worlddata import FaoData, GdpData

FAO_DB_PATH = 'data/world-fao-production.json'
DB_PATH = 'data/world-gdp.db'

def test_fao_instantiation():
    
    gdpdata = GdpData(DB_PATH)
    faodata = FaoData(FAO_DB_PATH, gdpdata)
    assert faodata is not None     

def test_fao_get_all():
    
    gdpdata = GdpData(DB_PATH)
    faodata = FaoData(FAO_DB_PATH, gdpdata)
    data = faodata.get_all()
    assert  174 == len(data) # total number of countries 
    #some data points
    assert 31 == data["NLD"]["2805"]["1961"]


def test_fao_filter_data():
    gdpdata = GdpData(DB_PATH)
    faodata = FaoData(FAO_DB_PATH, gdpdata)
    data = faodata.get_range(('NLD',), ("2805",), range(1961, 1962))
    
    assert  1 == len(data["NLD"]) # total number of items  
    
    #some data points
    assert 31 == data["NLD"]["2805"]["1961"]

def test_fao_filter_mixmaxmean():
    gdpdata = GdpData(DB_PATH)
    faodata = FaoData(FAO_DB_PATH, gdpdata)
    
    data = faodata.get_range_max(('NLD',), ("2805",), range(1961, 2013))
    assert ('NLD', '2805', '1996', 101) == data	
   
    data = faodata.get_range_min(('NLD',), ("2805",), range(1961, 2013))
    assert ('NLD', '2805', '1982', 24) == data	
   
    data = faodata.get_range_mean(('NLD',), ("2805",), range(1961, 2013))
    assert 42.40384615384615 == data	
   

    #data = pops.get_range_min(('NLD', 'ESP'), range(1990, 1992))
    #assert ('NLD', '1990', '14951510') == data	
   
    #data = pops.get_range_mean(('NLD', 'ESP'), range(1990, 1992))
    #assert 26963751.5 == data
    