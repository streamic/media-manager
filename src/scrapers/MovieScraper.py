import os
from guessit import guessit
from .AbstractScraper import AbstractScraper


class MovieScraper(AbstractScraper):
    def scrape_file(self, file_path):
        filename_w_ext = os.path.basename(file_path)
        filename, file_extension = os.path.splitext(filename_w_ext)

        if file_extension in self.video_extensions:
            title = guessit(filename)['title']

            search = self.tmdb.Search()
            search.movie(query=title)

            return search.results[0]
