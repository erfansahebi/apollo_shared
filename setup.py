from setuptools import setup, find_packages

setup(
    name='apollo_shared',
    version='0.0.17',
    description='Apollo Shared Library',
    author='Erfan Sahebi',
    packages=find_packages(),
    install_requires=[
        'nameko==3.0.0rc11',
        'marshmallow==3.20.1',
        "SQLAlchemy==2.0.22",
        "psycopg2-binary==2.9.9",
    ]
)
