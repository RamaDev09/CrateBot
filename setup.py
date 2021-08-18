from setuptools import setup
import os

here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "README.md"), encoding='utf-8') as f:
    long_description = f.read()

with open(os.path.join(here, "requirements.txt"), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if ('git+' not in x) and (
    not x.startswith('#')) and (not x.startswith('-'))]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs \
                    if 'git+' not in x]

setup(
    name="CrateBot",
    version="0.1.0",
    description="A tool to generate a discord bot project easy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/RamaDev09/CrateBot",
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        'License :: OSI Approved :: MIT License',
	'Operting System :: OS Independent'
    ],
    keywords=[''],
    packages=['bot'],
    include_package_data=True,
    author="RamaDev09",
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email='ramaabdiansyah03@gmail.com',
    entry_points = {
        "console_scripts": [
            "bot = bot.__main__:main"
        ]
    })
