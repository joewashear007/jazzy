try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'jazzy - jaz language interpreter',
    'author': 'Joseph Livecchi, Antohny Bier, ',
    'url': 'https://github.com/joewashear007/jazzy',
    'download_url': 'https://github.com/joewashear007/jazzy/archive/master.zip',
    'author_email': 'joewashear007@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['jazzy', 'jazzy.functions'],
    'package_dir' : {'jazzy': 'jazzy'},
    'name': 'jazzy',
    'entry_points':{
        'console_scripts': [
            'jazzy = jazzy.module:main',
        ],
    },
}

setup(**config)
