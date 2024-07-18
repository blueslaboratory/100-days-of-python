# 18/07/2024
# Day - 045

# https://www.empireonline.com/movies/features/best-movies-2/

##################################################
# DAY 45 PROJECT: 100 Movies That you must watch

print("\n*** Welcome to the Web Scrapping of the Best 100 Movies! ***")

from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

titles = soup.find_all(name="h3")

text = ""


for i in range(len(titles)-1, -1, -1):
    title = titles[i].getText()
    print(title)
    text += title + "\n"
    

# Write it into a file
with open(".\\045 - Beautiful Soup Scraping\\3. PJ Best 100 Movies\\100_movies.txt", mode="w") as file:
    file.write(text)
    # closes automatically