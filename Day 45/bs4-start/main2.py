""" from bs4 import BeautifulSoup

import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article_tag = soup.find(name="a", class_="storylink")
article_text = article_tag.getText()
artcle_link = article_tag.get("href")
articl_upvote = soup.find(name="span", class_="score").getText()

print(article_text)
print(artcle_link)
print(articl_upvote) """

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

article_tag = soup.find(name="a", class_="sitebit comhead")

if article_tag is not None:
    article_text = article_tag.getText()
    article_link = article_tag.get("href")
    print(article_text)
    print(article_link)
else:
    print("Article not found")

article_upvote = soup.find(name="span", class_="score")

if article_upvote is not None:
    print(article_upvote.getText())
else:
    print("Upvote count not found")
