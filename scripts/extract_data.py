import pandas as pd
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")
url = 'https://api.themoviedb.org/3/discover/movie'
params = {
    'api_key': API_KEY,
    'primary_release_date.gte': '2010-01-01',
    'primary_release_date.lte': '2020-12-31',
    'sort_by': 'popularity.desc',
    'page': 1
}

response = requests.get(url, params=params)
data = response.json()
for movie in data['results']:
    print(movie['title'], movie['release_date'], movie['vote_average'])

all_movies = []
for page in range(1, 11):
    params['page'] = page
    response = requests.get(url, params=params)
    data = response.json()
    all_movies.extend(data['results'])

df = pd.DataFrame(all_movies)
df.to_csv('../data/tmdb_movies_2010_2020.csv', index=False)
