import requests
from bs4 import BeautifulSoup
import re
# url = "https://www.imdb.com/title/tt7286456/ratings"





def getratings(idnum):
    url = f"https://www.imdb.com/title/{idnum}/ratings"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    helo = soup.findAll("div", {"class": "leftAligned"})
    helo = helo[1:-3]
    ratings = [int(x.text.replace(",", "")) for x in helo]
    ott = range(10, 0, -1)
    temp = zip(ott, ratings)
    findict = {x:y for x, y in temp}
    return findict



def getinfo(idnum):
    url = f"https://www.imdb.com/title/{idnum}/"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    helo = soup.find_all("div", class_="credit_summary_item")
    director, writer, stars = [x.text for x in helo]
    director = director.split(":")[1:]
    director = [x.strip('\n') for x in director]
    director = [x.strip(' ') for x in director]
    writer = re.split(r'\||:', writer)[1]
    writer = [x.strip('\n') for x in writer.split(",")]
    writer = [x.strip(' ') for x in writer]
    stars = re.split(r'\||:', stars)[1]
    stars = stars.split(",")
    stars = [x.strip('\n') for x in stars]
    stars = [x.strip(" ") for x in stars]
    helo = soup.find_all("h1")
    year = helo.split(" ")[-1][1:-1]

    return {"directors":director, "writers":writer, "stars": stars}

    



print(getinfo("tt2584384"))

# req = requests.get(url)
# soup = BeautifulSoup(req.text, "html.parser")

# helo = soup.findAll("div", class_="credit_summary_item")

# x = 0
# for i in helo:
#     x += 1
#     print(x)
#     print(i.text)
