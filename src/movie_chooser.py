import asyncio
import json
from random import randint
import aiohttp


class Movie:
    global headers

    def BASE_URL(
        movie_id): return f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwZGNmOTUzZmRhZDIxZTlkNmNmZWQxODdhODc2OWIyZCIsInN1YiI6IjY1NTk0ODVmYzQ5MDQ4MDExZDBmMWQxMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.EXiLARnv71YZZy4FBBmIKY1b5S5X6CIJQLJTAvEpZIw"
    }

    # async def check_ids():
    #     ids = randint(1, 500000)
    #     async with aiohttp.ClientSession() as session:
    #         async with session.get(url_2(ids), headers=headers) as response:
    #             if response.status == 404:
    #                 await check_ids()
    #             else:
    #                 return ids

    async def main():
        ids = randint(1, 500000)
        async with aiohttp.ClientSession() as session:
            async with session.get(Movie.BASE_URL(ids), headers=headers) as response:
                if response.status == 200:
                    film_info = json.loads(await response.content.read())
                    with open("film_info.json", "w") as f:
                        json.dump(film_info, f, indent=2)
                    return [film_info['title'], film_info['overview'], film_info['release_date'], film_info['genres'], film_info['production_companies'], film_info['id']]
                else:
                    return await Movie.main()


a = asyncio.run(Movie.main())
print(a)
