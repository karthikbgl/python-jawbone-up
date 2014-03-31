from setuptools import setup

setup(
    name="jawbone-up",
    version="0.1",
    install_requires=[
        "requests",
    ],

    description='Jawbone UP API python wrapper',
    url='http://github.com/storborg/funniest',
    author='Karthik Ravindra',
    author_email='karthikbgl@gmail.com',
    packages=['jawbone-up'],
    zip_safe=False
)
