import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
top_movies_page = response.text

soup = BeautifulSoup(top_movies_page, "html.parser")



articles = soup.find_all(name="h3", class_="title")

movies = [" ".join(movie.get_text().split()[1:])   for movie in articles ]

#[::-1] using this slice means start from the end, go backwards step by step.

new_movies_list = []
counter = 0
for movie in movies[::-1]:
    counter +=1
    number_and_movie_title = f"{counter}.{movie}"
    new_movies_list.append(number_and_movie_title)

    try:  # see if movies.txt is existing
        with open("movies.txt", encoding="utf-8") as file:
            contents = file.read()

    except FileNotFoundError:#If the file does not exist
        with open("movies.txt", "w", encoding="utf-8") as file:
            file.write(number_and_movie_title)
    else:
        with open("movies.txt", mode="a", encoding="utf-8") as file:
            file.write(f"\n{number_and_movie_title}")


