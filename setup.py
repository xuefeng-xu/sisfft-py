try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

CLASSIFIERS = [
    'License :: OSI Approved :: MIT License',
    'Topic :: Scientific/Engineering :: Bio-Informatics',
    'Topic :: Scientific/Engineering :: Mathematics',
]
config = {
    'name': 'sisfft',
    'version': '0.3.0',
    'test_suite': 'tests',
    'keywords': ['convolution', 'p-value', 'relative accuracy', 'log space'],
    'author': 'Huon Wilson',
    'author_email': 'huonw@maths.usyd.edu.au',
    'url': 'https://github.com/huonw/sisfft-py',
    'packages': ['sisfft'],
    'install_requires': ['numpy', 'scipy'],
    'classifiers': CLASSIFIERS,
    'description': 'Algorithms for convolutions and p-values (tail sums) that have '
     + 'guaranteed relative error, even for very small values.'
}

setup(**config)
