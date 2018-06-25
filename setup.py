from setuptools import setup,find_packages
import cricket_rankings as cr
import pypandoc

with open('requirements.txt') as f:
    requirements = f.readlines()

long_description = pypandoc.convert('README.md', 'rst')

setup(
        name=cr.__name__,
        version=cr.__version__,
        author=cr.__author__,
        author_email='umangahuja1@gmail.com',
        url='http://github.com/umangahuja1/cricket_rankings',
        description='Cricket rankings of teams and players across all the formats for both men and women',
        long_description=long_description,
        long_description_content_type="text/markdown",
        license='MIT',
        packages=find_packages(),
        classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ),
        keywords='package cricket cricket-rankings cricket_rankings',
        install_requires=requirements,
        zip_safe=False
)
