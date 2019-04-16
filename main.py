from src.scrapers.MovieScraper import MovieScraper
from src.scrapers.ShowScraper import ShowScraper
from utils import cli
from pprint import pprint
from src.tmdb import TMDB


def main():
    args = cli()
    api_key = args.api_key
    folder = args.folder
    ismovie = args.movie

    tmdb = TMDB(api_key)

    if ismovie:
        movie_scraper = MovieScraper(tmdb)
        for movie in movie_scraper.scrape_folder(folder):
            # TODO inject to database
            pprint(movie)
    else:
        show_scraper = ShowScraper(tmdb)
        for episode in show_scraper.scrape_folder(folder):
            # TODO inject to database
            pprint(episode)


if __name__ == '__main__':
    main()
