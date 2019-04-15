import os
from abc import ABC, abstractmethod


class AbstractScraper(ABC):
    video_extensions = ['.mkv', '.avi', '.mp4', '.mov', '.mpg']

    def __init__(self, tmdb):
        self.tmdb = tmdb

    def scrape_folder(self, folder_path):
        result = {}
        for subdir, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(subdir, file)
                yield self.scrape_file(file_path)

    @abstractmethod
    def scrape_file(self, file_path):
        pass
