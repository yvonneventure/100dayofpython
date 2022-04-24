from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies = response.text

soup = BeautifulSoup(movies, "html.parser")

movie = soup.find_all(name="h3", class_="title")
movie_list=[]
for x in movie:
    title=x.getText()
    movie_list.insert(0,title)
text=""
for i in movie_list:
    text+=i+"\n"

with open(file="movies.txt", mode="w") as file:
    file.write(text)


