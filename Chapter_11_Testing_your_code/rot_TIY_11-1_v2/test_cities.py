import pytest
import city_functions


def test_city_country():
    assert city_functions.city_country("santiago", "chile") == "Santiago, Chile"
    assert city_functions.city_country("Fort Wayne", "United States") == "Fort Wayne, United States"
