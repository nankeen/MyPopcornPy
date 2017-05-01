#!/bin/env python3
import requests
from . import logger


def find(title, api='https://omdbapi.com/'):
    payload = {'t': title}
    try:
        response = requests.get(api, params=payload).json()
        if response['Response'] == 'True':
            return response
        else:
            return False
    except requests.HTTPError:
        logger.error('Unable to communicate with API provider, please check your parameters.')
        return False
    except requests.ConnectionError:
        logger.error('Unable to connect to API provider, please check your connection.')
        return False


def process(titles):
    movies = []
    for title in titles:
        info_found = find(title)
        if info_found is False:
            movies.append(False)
        else:
            movies.append(info_found)
    return movies
