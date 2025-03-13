def famous_births(figures):
    """
    Sorts and displays historical figures by birth date.
    
    :param figures: Dictionary of historical figures with 'name' and 'date_of_birth' keys
    """
    sorted_figures = sorted(figures, key=lambda person: figures[person]["date_of_birth"])
    
    for person in sorted_figures:
        print(f"{figures[person]['name']} - Born on {figures[person]['date_of_birth']}")


if __name__ == "__main__":
    historical_figures = {
        "einstein": {"name": "Albert Einstein", "date_of_birth": "1879-03-14"},
        "newton": {"name": "Isaac Newton", "date_of_birth": "1643-01-04"},
        "curie": {"name": "Marie Curie", "date_of_birth": "1867-11-07"},
        "tesla": {"name": "Nikola Tesla", "date_of_birth": "1856-07-10"}
    }
    
    famous_births(historical_figures)