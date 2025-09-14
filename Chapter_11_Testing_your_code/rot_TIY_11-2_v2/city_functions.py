def city_country_population(city, country, population=None):
    city = city.title()
    country = country.title()
    if population:
        return f"{city}, {country} - Population: {population}"
    return f"{city}, {country}"
