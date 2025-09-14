import city_functions


def test_city_country_population():
    city = city_functions.city_country_population("Fort Wayne", "United States", 265974)
    assert city == "Fort Wayne, United States - Population: 265974"


def test_city_country_no_population():
    city = city_functions.city_country_population("London", "United Kingdom")
    assert city == "London, United Kingdom"
