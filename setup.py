from setuptools import setup

setup(
    name='kitsu-wrapper',
    author='Naegin',
    url='https://github.com/DiscoMusic/kitsu-wrapper',
    version='0.1.2',
    packages=['kitsu'],
    install_requires=['aiohttp'],
    description='A simple wrapper for the Kitsu.io API.',
    license='MIT License'
)
