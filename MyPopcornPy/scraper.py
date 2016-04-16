#!/bin/env python3
import requests
import re
from bs4 import BeautifulSoup


class GSC_Scraper(object):
    def __init__(self, url):
        '''
        This scrapers is designed for the GSC cinemas website
        A load more loop is implemented for the "Load more" AJAX button
        This scraper uses the lxml parser, so install it or use another parser
        '''
        self.url = url
        # Gets the initial page
        page = requests.get(self.url)
        # You can change the parser used here
        self.page_tree = BeautifulSoup(page.content, 'lxml')

        # Gets the expected number of movies
        total = self.get_total()

        # This is to prevent an infinite loop
        timeout = 0

        # The loop to simulate the "Load more" button click
        while not len(self.get_titles()) == total:
            if timeout >= 20:
                print('[!] Unable to scrape all titles, continuing anyways')
                break
            self.load_more()
            timeout += 1
        # Got em titles
        self.titles = self.get_titles()

    def get_titles(self):
        '''
        Scrapes the movie titles in the page
        '''
        titles = []
        # The move titles are found in div tags with the class "Title Transition02a"
        sections = self.page_tree.find_all('div', {'class': 'Title Transition02a'})

        # Adds them to the list
        for section in sections:
            titles.append(section.text)
        return titles

    def get_total(self):
        '''
        Scrapes the "[total] movies now showing" into an int
        '''
        # The string is conveniently stored in a span tag with id: LblTotal
        total_string = str(self.page_tree.find('span', {'id': 'LblTotal'}))
        # Using regular expressions to get the digits
        total = re.findall(r'\d+', total_string)[0]
        return int(total)

    def load_more(self):
        '''
        Simulates the "Load more" buttton click through AJAX
        Parameters for the POST data are scraped from hidden form fields
        '''
        params = self.page_tree.find_all('input', {'type': 'hidden'})

        # This POST data to be used
        payload = {'rdList': '1', 'btnProNext': 'Load+More'}

        # Put the parameters into the dictionary
        for param in params:
            payload[param.get('name')] = param.get('value')
        # Performs the post request and updates the page
        page = requests.post(self.url, data=payload)
        self.page_tree = BeautifulSoup(page.content, 'lxml')
