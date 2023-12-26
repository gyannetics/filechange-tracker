from setuptools import setup, find_packages

setup(
    name='filechange_tracker',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'watchdog',
    ],
    author='Santosh KV',
    author_email='gyannetics@gmail.com',
    description='A package to track file changes and create markers.',
    keywords='file tracking change monitor',
)
    