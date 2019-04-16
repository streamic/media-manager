import os
from guessit import guessit
from .AbstractScraper import AbstractScraper


class ShowScraper(AbstractScraper):
    def scrape_file(self, file_path):
        filename_w_ext = os.path.basename(file_path)
        filename, file_extension = os.path.splitext(filename_w_ext)

        if file_extension in self.video_extensions:
            info = guessit(filename)
            episode_number = info['episode']

            show = self.tmdb.search_show(info['title'])  # TODO Get all information from this request
            season = self.tmdb.get_season(tv_id=show['id'], season_number=info['season'])
            # Season returns all episode information
            episode = {}
            for ep in season['episodes']:
                if ep['episode_number'] == episode_number:
                    episode = ep

            result = {
                'show': {
                    'original_name': show['original_name'],
                    'id': show['id'],
                    'vote_average': show['vote_average'],
                    'poster_path': show['poster_path'],
                    'genre_ids': show['genre_ids'],
                    'backdrop_path': show['backdrop_path'],
                    'overview': show['overview'],
                    'origin_country': show['origin_country']
                },

                'season': {
                    'air_date': season['air_date'],
                    'name': season['name'],
                    'overview': season['overview'],
                    'poster_path': season['poster_path'],
                    'season_number': season['season_number']
                },

                'episode': {
                    'episode_number': episode['episode_number'],
                    'name': episode['name'],
                    'overview': episode['overview'],
                    'season_number': episode['season_number'],  # TODO is this necessary?
                    'still_path': episode['still_path'],
                    'vote_average': episode['vote_average'],
                    'air_date': episode['air_date']
                },

                'file_path': file_path
            }

            return result
