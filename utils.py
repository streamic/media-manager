import argparse


def cli():
    parser = argparse.ArgumentParser()

    parser.add_argument("-k", "--api-key", type=str, help="TheMovieDataBase api key", required=True)
    parser.add_argument("-f", "--folder", type=str, help="the folder to scrape data from", required=True)

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-m', '--movie', action='store_true')
    group.add_argument('-s', '--show', action='store_false')

    args = parser.parse_args()

    return args
