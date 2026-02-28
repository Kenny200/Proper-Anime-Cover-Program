from bs4 import BeautifulSoup
import requests
pageToScrape = requests.get("https://myanimelist.net/animelist/username")
soup = BeautifulSoup(pageToScrape.text, "html.parser")
animeTitles = soup.find_all("a", attrs={"class": "animetitle"})

file = open(r"\animelist.txt", "w", encoding="utf-8")
for animeTitle in animeTitles:
    file.write(animeTitle.text + "\n")

file.close()
