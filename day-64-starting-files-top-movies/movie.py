import requests

MOVIE_ENDPOINT= "https://api.themoviedb.org/3/search/movie"

HEADER = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyY2U0MWI1Y2Y2ZDczZDg5OWI4YWYxNjFlOWE1ZDdmNyIsInN1YiI6IjY1NDhmYzJmNmJlYWVhMDE0YjY5MWRhOSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.g69PyrrWoyfKtloqxDSpYBXiPYeVcJqL0tgN6V2ovQ8"
}


movie_data= requests.get(url=f"{MOVIE_ENDPOINT}?query=Matrix&include_adult=false&language=en-US&page=1",headers=HEADER).json()["results"]


print(movie_data[2])

