from setuptools import setup

import kitsu

setup(
    name='kitsu-wrapper',
    author='Naegin',
    url='https://github.com/DiscoMusic/kitsu-wrapper',
    version=kitsu.__version__,
    packages=['kitsu'],
    install_requires=['aiohttp'],
    description='A simple wrapper for the Kitsu.io API.',
    license='MIT License'
)
