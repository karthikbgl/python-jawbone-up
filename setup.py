from setuptools import setup

setup(
    name="jawbone-up",
    version="0.1",
    install_requires=[
        "requests",
    ],

    description='Jawbone UP API python wrapper',
    url='https://github.com/karthikbgl/python-jawbone-up',
    author='Karthik Ravindra',
    author_email='karthikbgl@gmail.com',
    packages=['jawbone'],
    zip_safe=False
)
