import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"



html_data= requests.get(URL).text
soup= BeautifulSoup(html_data,"html.parser")

movie_list= soup.find_all(name="h3",class_="title")

for movie_name in reversed(movie_list):
    movie_data= open("day 46- Beautiful Soup/Starting Code - 100 movies to watch start/movies.txt","a")
    movie_data.write(movie_name.getText()+"\n")

# Write your code below this line 👇


