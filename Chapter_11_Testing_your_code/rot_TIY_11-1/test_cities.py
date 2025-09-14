import cities


def test_city_country():
    """Make a city, such as Fort Wayne in the US."""
    city = cities.make_city("Fort Wayne", "United States")
    assert city == "Fort Wayne, United States"
