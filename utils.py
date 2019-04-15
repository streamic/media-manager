import argparse


def cli():
    parser = argparse.ArgumentParser()

    parser.add_argument("-k", "--api-key", type=str, help="TheMovieDataBase api key", required=True)
    parser.add_argument("-f", "--folder", type=str, help="the folder to scrape data from", required=True)

    args = parser.parse_args()

    return args
