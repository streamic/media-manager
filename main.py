import tmdbsimple as tmdb
from src.scrapers.MovieScraper import MovieScraper
from utils import cli
from pprint import pprint


def main():
    args = cli()
    api_key = args.api_key
    folder = args.folder

    tmdb.API_KEY = api_key
    movie_scraper = MovieScraper(tmdb)

    for movie in movie_scraper.scrape_folder(folder):
        # TODO inject to database
        pprint(movie)


if __name__ == '__main__':
    main()
