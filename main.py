import requests

from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

movies_webpage = response.text #the raw html text

soup = BeautifulSoup(movies_webpage, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1] #reverses the order uses slice syntax

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")



