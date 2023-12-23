from setuptools import setup, find_packages

setup(
    name='filechange_tracker',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'watchdog',
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A package to track file changes and create markers.',
    keywords='file tracking change monitor',
)
    