# 21/02/2024
# Day - 016

# Links:
# https://pypi.org/
# https://pypi.org/project/prettytable/
# https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki
# https://pokemondb.net/pokedex/game/x-y

# Terminal
# > pip install PrettyTable



##################################################
print("\n\n*** PrettyTable ***")

from prettytable import PrettyTable

table = PrettyTable()


table.field_names = ["Pokemon Name", "Type"]
table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"],
        ["Bulbasaur", "Plant"],
    ]
)


# left align
table.align = "l"

print(table)