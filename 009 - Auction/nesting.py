# 12/02/2024
# Day - 009



##################################################
print("\n\n*** Nesting ***")
print("""{
      key: [List],
      key2: {Dict},
}""")

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a list in a dictionary
travel_log_0 = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting a dictionary in a dictionary
travel_log_1 = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"],
               "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
               "total_visits": 5},
}

# Nesting a dictionary in a list
travel_log_2 = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
]