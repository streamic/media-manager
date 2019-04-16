import os
from guessit import guessit
from .AbstractScraper import AbstractScraper


class ShowScraper(AbstractScraper):
    def scrape_file(self, file_path):
        filename_w_ext = os.path.basename(file_path)
        filename, file_extension = os.path.splitext(filename_w_ext)

        if file_extension in self.video_extensions:
            info = guessit(filename)

            show = self.tmdb.search_show(info['title'])  # TODO Get all information from this request
            episode = self.tmdb.get_episode(tv_id=show['id'], season_number=info['season'], episode_number=info['episode'])
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

                'episode': {
                    'episode_number': episode['episode_number'],
                    'name': episode['name'],
                    'overview': episode['overview'],
                    'season_number': episode['season_number'],
                    'still_path': episode['still_path'],
                    'vote_average': episode['vote_average'],
                    'air_date': episode['air_date']
                },
                'file_path': file_path
            }

            return result
