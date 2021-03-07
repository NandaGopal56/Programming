from bs4 import BeautifulSoup
import requests

url = "https://www.imdb.com/list/ls009997493/"

page = requests.get(url)

soup = BeautifulSoup(page.content,'lxml')

#printing the title of the website
print(soup.title.text)

#getting the titles of the movies
movie_name = soup.findAll('h3',class_="lister-item-header")
movie_names = []
for movie in movie_name:
    #storing movie titles in the list
    movie_names.append(movie.a.text)

#getting the movie years
movie_year = soup.findAll('span',class_="lister-item-year text-muted unbold")
movie_years = []
for year in movie_year:
    #storing movie years in the list
    movie_years.append(year.text)

#getting the movie rating with "div" tag
movie_ratings = []
movie_rating = soup.findAll('div',class_="ipl-rating-star small")
for rating in movie_rating:

    #getting the movie rating of aspn tag from div tag 
    rating = rating.findAll('span',class_="ipl-rating-star__rating")
    
    for rating in rating:

        # storing the ratings in the list
        movie_ratings.append(rating.text)

for i in range(len(movie_names)):
    print(movie_names[i],movie_years[i],movie_ratings[i])
    print()

