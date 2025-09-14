import cities


def test_city_country_population():
    """Make a city, such as Fort Wayne in the US with the population included."""
    city = cities.make_city("Fort Wayne", "United States", 265974)
    assert city == "Fort Wayne, United States - Population: 265974"


def test_city_country_no_population():
    """Make the city London in the United Kingdom; without population."""
    city = cities.make_city("London", "United Kingdom")
    assert city == "London, United Kingdom"
