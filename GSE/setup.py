try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Carter Pedrsen',
    'url': 'N/A',
    'download_url': 'N/A',
    'author_email': 'carter.e.pedersen@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': ''
}
