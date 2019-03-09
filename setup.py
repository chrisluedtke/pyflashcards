from pathlib import Path
from setuptools import setup, find_packages

README = (Path(__file__).parent / "README.md").read_text()

setup(
    name='pyflashcards',
    version='0.2',
    description="A simple way to log and study python tidbits",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    license='MIT',
    include_package_data=True,
    author="Chris Luedtke, Chris Louie",
    keywords=[
        'pyflashcards'
    ],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    entry_points=[
        'pyflashcards = pyflashcards.cli:main',
    ]
)
