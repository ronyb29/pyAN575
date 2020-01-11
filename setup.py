from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pyAN575',
    packages=['pyAN575'],
    version='0.1.2',
    description="Converts between Microchip's an575 float format and IEEE-754.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Rony Batista',
    author_email='rony.batista29@gmail.com',
    url='https://github.com/ronyb29/pyAN575',
    keywords=["float", "ieee754", "AN575"],
    classifiers=["Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent"],
)
