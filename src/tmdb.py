import requests


class TMDB:

    # image_url = 'https://image.tmdb.org/t/p/original'
    api = 'https://api.themoviedb.org/3'

    def __init__(self, api_key):
        self.api_key = api_key

    def search_movie(self, title):
        query = title.replace(' ', '%20')
        url = f'{self.api}/search/movie?api_key={self.api_key}&query={query}' \
            f'&include_adult=false&language=en-US&page=1'
        r = requests.get(url).json()['results'][0]  # Get first result

        return r

    def search_show(self, title):
        query = title.replace(' ', '%20')
        url = f'{self.api}/search/tv?api_key={self.api_key}&query={query}' \
            f'&include_adult=false&language=en-US&page=1'
        r = requests.get(url).json()['results'][0]  # Get first result

        return r

    def get_season(self, tv_id, season_number):
        url = f'{self.api}/tv/{tv_id}/season/{season_number}?api_key={self.api_key}' \
            f'&language=en-US'
        r = requests.get(url).json()

        return r

    def get_episode(self, tv_id, season_number, episode_number):
        url = f'{self.api}/tv/{tv_id}/season/{season_number}/episode/{episode_number}?api_key={self.api_key}' \
            f'&language=en-US'
        r = requests.get(url).json()

        return r
