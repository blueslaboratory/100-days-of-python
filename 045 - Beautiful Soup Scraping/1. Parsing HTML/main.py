# 18/07/2024
# Day - 045

# pip install bs4
# pip install lxml

from bs4 import BeautifulSoup
# import lxml


with open(".\\045 - Beautiful Soup Scraping\\1. Parsing HTML\\website.html") as file:
    contents = file.read()
    # print(contents)
    # closes automatically


# This line of code does our parsing  
soup = BeautifulSoup(contents, "html.parser")


print("\n*** SOUP LOCAL WEBSITE ***")
# print(soup)
print(soup.prettify())


print("\n*** SOUP BY DATA ***")
print(soup.title)
print(soup.title.name)
print(soup.title.string)


print("\n*** SOUP BY DATA: 1st anchor tag, li, p ***")
print(soup.a)
print(soup.li)
print(soup.p)


print("\n*** SOUP BY DATA: find_all ***")
all_anchor_tags = soup.find_all(name="a")
print("all_anchor_tags:")
print(all_anchor_tags)
print()

all_paragraph_tags = soup.find_all(name="p")
print("all_paragraph_tags:")
print(all_paragraph_tags)
print()

for tag in all_anchor_tags:
    print("text:", tag.getText())
    print("href:", tag.get("href"))
    
    
heading = soup.find(name="h1", id="name")
print("\nheading:", heading)

section_heading = soup.find(name="h3", class_="heading")
print("Section heading class:", section_heading.get("class"))
print("Section heading text:", section_heading.getText())
print()

# CSS selector: selector="p a"
company_url = soup.select_one(selector="p a")
print(company_url)

# CSS selector: selector="#name"
name = soup.select_one(selector="#name")
print(name)

# CSS selector: selector=".heading"
headings = soup.select(".heading")
print(headings)