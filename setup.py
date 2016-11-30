try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

'''
This setup script does nothing for now as I have no idea how to work this lol
Will implement this as soon as I have time figure it out
'''

config = {
    'description': 'A script to get movies from local cinemas that has an IMDB rating of 8 or more',
    'author': 'NaNkeen',
    'url': '',
    'download_url': '',
    'version': '0.1',
    'install_requires': ['bs4', 'requests'],
    'packages': ['MyPopcornPy']
    'scripts': ['__main__', 'finder', 'scraper'],
    'name': ''
}

setup(**config)
