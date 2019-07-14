from worlddata import PopulationData
from functools import reduce

POPS_DB_PATH = 'data/world-population.csv'

def test_population_instantiation():
    
    pops = PopulationData(POPS_DB_PATH)
    assert pops is not None     

def test_population_get_all():
    
    pops = PopulationData(POPS_DB_PATH)
    data = pops.get_all_countries()
    
    assert 264 == len(data.keys()) # total number of countries
    
    total = 0
    for e in data.values():
        total += len(e.values()) 
    assert 15576 == total

    #assert 15576 == reduce(lambda total, e: total + len(e.values()), data.values())
    
def test_population_filter_data():
    pops = PopulationData(POPS_DB_PATH)
    data = pops.get_countries(('NLD', 'ESP'), range(1990, 1992))
    assert '14951510' == data['NLD']['1990']	
    assert '15069798' == data['NLD']['1991']	
    assert '38867322' == data['ESP']['1990']	
    assert '38966376' == data['ESP']['1991']	

def test_population_filter_mixmax():
    pops = PopulationData(POPS_DB_PATH)
    data = pops.get_countries_max(('NLD', 'ESP'), range(1990, 1992))
    assert ('ESP', '1991', '38966376') == data	
   

