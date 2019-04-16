import os
from guessit import guessit
from .AbstractScraper import AbstractScraper


class ShowScraper(AbstractScraper):
    def scrape_file(self, file_path):
        filename_w_ext = os.path.basename(file_path)
        filename, file_extension = os.path.splitext(filename_w_ext)

        if file_extension in self.video_extensions:
            info = guessit(filename)

            show = self.tmdb.search_show(info['title'])
            r = self.tmdb.get_episode(tv_id=show['id'], season_number=info['season'], episode_number=info['episode'])

            return r
