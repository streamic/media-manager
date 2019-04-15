import os
from guessit import guessit
from .AbstractScraper import AbstractScraper


class ShowScraper(AbstractScraper):
    def scrape_file(self, file_path):
        raise NotImplemented  # TODO: Implement search for TV Show *episode*, can't do it with tmdbsimple
        # filename_w_ext = os.path.basename(file_path)
        # filename, file_extension = os.path.splitext(filename_w_ext)
        #
        # if file_extension in self.video_extensions:
        #     title = guessit(filename)['title']
        #
        #     search = self.tmdb.Search()
        #     search.tv(query=title)
        #
        #     yield search.results[0])
