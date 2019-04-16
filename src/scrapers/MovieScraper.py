import os
from guessit import guessit
from .AbstractScraper import AbstractScraper


class MovieScraper(AbstractScraper):
    def scrape_file(self, file_path):
        filename_w_ext = os.path.basename(file_path)
        filename, file_extension = os.path.splitext(filename_w_ext)

        if file_extension in self.video_extensions:
            title = guessit(filename)['title']

            movie = self.tmdb.search_movie(title)

            result = {
                'id': movie['id'],
                'vote_average': movie['vote_average'],
                'poster_path': movie['poster_path'],
                'original_title': movie['original_title'],
                'genre_ids': movie['genre_ids'],
                'backdrop_path': movie['backdrop_path'],
                'overview': movie['overview'],
                'release_date': movie['release_date'],
                'file_path': file_path
            }

            return result
