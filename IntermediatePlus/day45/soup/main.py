from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

soup = BeautifulSoup(response.text, "html.parser")

article_texts = []
article_links = []
article_upvotes = []
articles = soup.find_all(name="a", class_="storylink")
for article_tag in articles:
    article_texts.append(article_tag.get_text())
    article_links.append(article_tag.get("href"))
    has_score = article_tag.parent.parent.next_sibling.contents[1].contents[1].string.split()[1] == "points"
    if has_score:
        score = int(article_tag.parent.parent.next_sibling.contents[1].contents[1].string.split()[0])
        article_upvotes.append(score)
    else:
        article_upvotes.append(0)

max_index = article_upvotes.index(max(article_upvotes))

most_upvoted = (article_texts[max_index], article_links[max_index], article_upvotes[max_index])

print(most_upvoted)
