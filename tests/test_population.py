from worlddata import PopulationData, Population

DB_PATH = 'data/world-population.csv'

def test_population_instantiation():
    pops = PopulationData(DB_PATH)
    assert pops is not None     

def test_population_get_all():
    pops = PopulationData(DB_PATH)
    data = pops.get_all()
    assert 15576 == len(data) # total number of countries 
    assert str(14439018) == data[-1].population # Last item in list: Zimbabwe - 2018