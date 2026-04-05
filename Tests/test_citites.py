import pytest

from city_functions import city_country

#Tests city and country with no population
def test_city_country():
    result = city_country('santiago', 'chile')
    assert result == "Santiago, Chile"

#Tests city, country and population
def test_city_country_population():
    result = city_country('santiago', 'chile', population=5000000)
    assert result == "Santiago, Chile - population 5000000"