# 18/07/2024
# Day - 045

# https://news.ycombinator.com/news


from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
# print(response.text)

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")



print("\nOne Liners:")

article_text = soup.find(name="span", class_="titleline").getText()
article_link = soup.find(name="span", class_="titleline").find(name="a").get("href")
article_upvote = soup.find(name="span", class_="score").getText()

print(article_text)
print(article_link)
print(article_upvote)



print("\nAll Title Lines:")

titlelines = soup.find_all(name="span", class_="titleline")

# print(enumerate(titlelines))

for i, titleline in enumerate(titlelines):
    print(i, titleline.getText())



print("\nComplete list:")

articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []

# For loop
for article_tag in articles:
    article_texts.append(article_tag.getText())
    article_links.append(article_tag.find(name="a").get("href"))

# Another way: List Comprehension
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(len(article_texts)) == 30

for i in range(len(article_texts)-1):
    print(i, "-", article_texts[i], "| Upvotes:", article_upvotes[i])
    print("URL:", article_links[i])
    print("________________________")



print("\nArticle with the highest number of points")
index = article_upvotes.index(max(article_upvotes))

print(article_texts[index], "| Upvotes:", article_upvotes[index])
print("URL:", article_links[index])