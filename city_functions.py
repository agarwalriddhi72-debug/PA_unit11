def city_country(city, country, population = None):
    """Returns a formatted string"""

    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"
