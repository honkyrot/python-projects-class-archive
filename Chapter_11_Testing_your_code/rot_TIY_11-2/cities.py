# Making a city

def make_city(city, country, population=None):
    """Make a city with a assigned country."""
    if population:
        return f"{city}, {country} - Population: {population}"
    return f"{city}, {country}"
