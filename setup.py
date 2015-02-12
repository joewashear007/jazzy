try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'jazzy - jaz language interpreter',
    'author': 'Joseph Livecchi, Antohny Bier, ',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'joewashear007@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['jazzy'],
    'scripts': [],
    'name': 'jazzy'
}

setup(**config)
