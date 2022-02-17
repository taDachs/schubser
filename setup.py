from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name="schubser",
    version="0.1.0",
    license="MIT",
    author="Max Schik",
    author_email="max.schik@googlemail.com",
    url='https://github.com/taDachs/nort',
    description='Module and script for sending messages using Pushover.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=["schubser"],
    scripts=["scripts/schubser"],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
