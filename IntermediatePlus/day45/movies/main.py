from bs4 import BeautifulSoup
import requests

res = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(res.text, "html.parser")
# print(soup.prettify())

titles = list(reversed([img.get('alt').title()
                        for img
                        in soup.find_all(name="img", class_="jsx-952983560")
                        if img.get("alt") != '']))

titles = list(dict.fromkeys(titles))

with open(file="movies.txt", mode="w") as file:
    count = 1
    for title in titles:
        file.write(f"{count}) {title}\n")
        count += 1



