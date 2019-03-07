from pathlib import Path
from setuptools import setup, find_packages

README = (Path(__file__).parent / "README.md").read_text()

setup(
    name='pyflashcards',
    version='0.1',
    description="A simple way to log and study python tidbits",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    author="Chris Luedtke",
)
