"""
merrick wedding
"""
from setuptools import setup, find_packages

setup(
    name='merrick_weeding',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'sqlalchemy',
        'docker',
        'flask-sqlalchemy',
        'psycopg2',
        'passlib',
        'sqlalchemy_utils'
    ],
    test_require=[
        'pytest',
        'pytest-cov',
    ]
)
