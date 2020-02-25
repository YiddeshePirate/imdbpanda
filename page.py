import pickle

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
    helo = [x.text for x in helo][-1]
    title, year = helo.split("\xa0")
    year = year[1:-2]
    
    return {"title":title, "directors":director, "writers":writer, "stars": stars, "year":year}

ratings = getratings('tt1345836')
info = getinfo('tt1345836')
total = info.update(ratings)
print(total)
print(info)
# with open("imdbid.pkl", "rb") as f:
    # o = pickle.load(f)

# for i in o:
    # print(i)





# req = requests.get(url)
# soup = BeautifulSoup(req.text, "html.parser")

# helo = soup.findAll("div", class_="credit_summary_item")

# x = 0
# for i in helo:
#     x += 1
#     print(x)
#     print(i.text)
