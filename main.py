from bs4 import BeautifulSoup
import requests

# GET ALL ARTICLES AND THEIR INFO
response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text
# Make Soup
soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

# Get a list of all article upvotes
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
# Get the highest score
highest_score = max(article_upvotes)
# Get the index of highest score
index = article_upvotes.index(highest_score)

# Getting most upvoted article title, link, and score
top_title = article_texts[0]
top_link = article_links[0]
top_score = highest_score
print(f"The article with the most upvotes is '{top_title}' at {top_link} with a score of {top_score}!")

