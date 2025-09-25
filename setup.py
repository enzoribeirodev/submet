from os import path
from setuptools import setup, find_packages
import sys
import versioneer


# NOTE: This file must remain Python 2 compatible for the foreseeable future,
# to ensure that we error out properly for people with outdated setuptools
# and/or pip.
min_version = (3, 6)
if sys.version_info < min_version:
    error = """
submet does not support Python {0}.{1}.
Python {2}.{3} and above is required. Check your Python version like so:

python3 --version

This may be due to an out-of-date pip. Make sure you have pip >= 9.0.1.
Upgrade pip like so:

pip install --upgrade pip
""".format(*(sys.version_info[:2] + min_version))
    sys.exit(error)

here = path.abspath(path.dirname(__file__))

try:
    with open(path.join(here, 'README.rst'), encoding='utf-8') as readme_file:
        readme = readme_file.read()
except FileNotFoundError:
    with open(path.join(here, 'README.md'), encoding='utf-8') as readme_file:
        readme = readme_file.read()

with open(path.join(here, 'requirements.txt')) as requirements_file:
    # Parse requirements.txt, ignoring any commented-out lines.
    requirements = [line for line in requirements_file.read().splitlines()
                    if not line.startswith('#')]


setup(
    name='submet',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Package to compute the distance between equi-dimensional subspaces.  Implements a variety of metrics.",
    long_description=readme,
    author="Kristian M. Eschenburg",
    author_email='keschenb@uw.edu',
    url='https://github.com/kristianeschenburg/submet',
    python_requires='>={}'.format('.'.join(str(n) for n in min_version)),
    packages=find_packages(exclude=['docs', 'submet/tests']),
    entry_points={
        'console_scripts': [
            # 'command = some.module:some_function',
        ],
    },
    include_package_data=True,
    package_data={
        'submet': [
            # When adding files here, remember to update MANIFEST.in as well,
            # or else they will not be included in the distribution on PyPI!
            # 'path/to/data_file',
        ]
    },
    install_requires=requirements,
    license="BSD (3-clause)",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
)