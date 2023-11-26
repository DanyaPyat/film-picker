import asyncio
import json
from random import randint
import aiohttp


class Movie:
    global headers 
    global genre_id 
    global params
    global release_year
    global params_1

    genre_id = 28
    release_year = 2022

    def BASE_URL(
        movie_id): return f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    def GENRE_URL (): return f"https://api.themoviedb.org/3/discover/movie"
    def YEAR_URL (): return f"https://api.themoviedb.org/3/discover/movie"

    params_1 = {
        'api_key': '0dcf953fdad21e9d6cfed187a8769b2d',
        'primary_release_year': release_year,
        'page': randint(1,10)
    }
    params = {
        'api_key': '0dcf953fdad21e9d6cfed187a8769b2d',
        'with_genres': genre_id,
        'page': randint(1,10)
    }
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwZGNmOTUzZmRhZDIxZTlkNmNmZWQxODdhODc2OWIyZCIsInN1YiI6IjY1NTk0ODVmYzQ5MDQ4MDExZDBmMWQxMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.EXiLARnv71YZZy4FBBmIKY1b5S5X6CIJQLJTAvEpZIw"
    }


    async def genres_convert(genre_ids) -> list:
        genre_names = []
        with open("genre_info_en.json", "r") as g:
            data = json.load(g)
            genres = data['genres']
            for genre_id in genre_ids:
                for genre in genres:
                    if genre['id'] == genre_id:
                        genre_names.append(genre['name'])
                        break
            return genre_names

    async def film_pick() -> list: 
        ids = randint(1, 500000)
        async with aiohttp.ClientSession() as session:
            async with session.get(Movie.BASE_URL(ids), headers = headers) as response:
                if response.status == 200:
                    film_info = json.loads(await response.content.read())
                    return [film_info['title'], film_info['overview'], film_info['release_date'], film_info['genres'], film_info['id']]
                else:
                    return await Movie.film_pick()
                
    async def film_picker_genre(genre_id) -> list:
        async with aiohttp.ClientSession() as session:
            async with session.get(Movie.GENRE_URL(), params=params) as response:
                if response.status == 200:
                    data = json.loads(await response.content.read())
                    if 'results' in data and data['results']:
                        movie = data['results'][randint(0,len(data))]
                        genre_ids = movie.get('genre_ids',[])
                        genre_names = await Movie.genres_convert(genre_ids)
                        return [movie['title'], movie['overview'], movie['release_date'], movie['id'], genre_names]
                    else:
                        return None
                else:
                    return None
                
    async def film_picker_year(release_year)-> list:
        async with aiohttp.ClientSession() as session:
            async with session.get(Movie.YEAR_URL(),  params = params_1) as response:
                if response.status == 200:
                    year = json.loads(await response.content.read())
                    if 'results' in year and year['results']:
                        movie = year['results'][randint(0,len(year))]
                        genre_ids = movie.get('genre_ids',[])
                        genre_names = await Movie.genres_convert(genre_ids)
                        return [movie['title'], movie['overview'], movie['release_date'], movie['id'], genre_names]
                    else:
                        return None
                else:
                    return None
                    
                    



async def main():
    result = await Movie.film_picker_genre(genre_id)
    film = await Movie.film_pick()
    year_film = await Movie.film_picker_year(release_year)
    print(result)
    print(film)
    print(year_film)


asyncio.get_event_loop().run_until_complete(main())
