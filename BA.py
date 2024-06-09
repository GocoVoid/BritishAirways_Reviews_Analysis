import pandas as pd
from bs4 import BeautifulSoup
import requests

passenger = []
date = []
ratings = []
comments = []

for pages in range(1,11):
    f = requests.get('https://www.airlinequality.com/airline-reviews/british-airways/page/'+str(pages))
    soup = BeautifulSoup(f.text)
    for i in soup.findAll("div",{"class":"body"}):
        comments.append((i.find("div",{"class":"text_content"})).text)

    for j in soup.findAll("div",{"class":"body"}):
        passenger.append((j.find("span",{"itemprop":"name"})).text)

    for k in soup.findAll("div",{"itemprop":"reviewRating"}):
        ratings.append((k.find("span",{"itemprop":"ratingValue"})).text)

    for l in soup.findAll("div",{"class":"body"}):
        date.append((l.find("time",{"itemprop":"datePublished"})).text)

finaldf = pd.DataFrame(
    {'Passenger':passenger,
     'Date of Publication':date,
     'Ratings':ratings,
     'Feedback':comments
    })

finaldf.to_csv('BA_Reviews.csv',index=False)
