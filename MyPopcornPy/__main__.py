#!/bin/env python3
import finder
import scraper


def init():
    '''
    The function to be called when the script initializes
    This handles the flow of the script
    '''
    print('[*] Scraping local cinema websites for movies')
    # This scraper is written for GSC Cinemas and will spit out the titles of Now Showing movies in a list
    titles = scraper.GSC_Scraper('http://gsc.com.my/html/movieNowShowing.aspx').titles

    # Makes sure movies are found
    if len(titles) == 0:
        print('No movies found!')
        exit()

    # This calls the finder to process the list of movies found
    print('[*] Looking up IMDB ratings for cinema movies')
    titles = finder.process(titles)

    # Prints out movies with IMDB rating 8 or higher in a pretty manner
    dump_movies(get_good_ones(titles))


def get_good_ones(batch):
    '''
    Takes in a a list of movie dictionaries and extracts the ones with IMDB rating 8 or higher
    '''
    good_ones = []

    # Iterates through the movies
    for item in batch:
        # Sometimes the movie will not have a IMDB rating
        if item is False or item['imdbRating'].lower() == 'n/a':
            pass
        elif float(item['imdbRating']) >= 8:
            good_ones.append(item)
    return good_ones


def dump_movies(movies):
    '''
    Prints the movies in a formatted manner
    With attributes on the right and value on the left
    '''
    for movie in movies:
        try:
            # I don't really need these information
            movie.pop('Poster')
            movie.pop('Writer')
            movie.pop('Type')
        except KeyError:
            pass
        # A neat line <3
        print('-' * 50)

        # Prints the title first
        print('{}: {}'.format('Title', movie['Title']))
        for key in sorted(movie.keys()):
            # We don't need to print the title again
            if key != 'Title':
                print('{0}:{1} |{2}'.format(key, tab_align(key), movie[key]))


def tab_align(string):
    '''
    This function is just a quick and dirty
    method to set the alignment for the printing
    '''
    multiplier = 1
    if len(string) < 7:
        multiplier = 2
    return ('\t' * multiplier)

# Calls the init() function if this is run as a script
if __name__ == '__main__':
    init()
