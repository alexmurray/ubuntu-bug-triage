"""Setup.py file."""

import os
from setuptools import find_packages, setup

PWD = os.path.abspath(os.path.dirname(__name__))
REQUIREMENTS_FILE = os.path.join(PWD, 'requirements.txt')
REQUIREMENTS = []
with open(REQUIREMENTS_FILE, 'r') as req_file:
    REQUIREMENTS = req_file.read().splitlines()

README_FILE = os.path.join(PWD, 'README.md')
with open(README_FILE, 'r') as readme:
    README_TEXT = readme.read()

setup(
    name='ubuntu-triage',
    version='18.3',
    description='Recently updated Launchpad bugs for triage',
    long_description=README_TEXT,
    long_description_content_type='text/markdown',
    author='Joshua Powers',
    author_email='josh.powers@canonical.com',
    url='https://github.com/powersj/ubuntu-triage',
    download_url=(
        'https://github.com/powersj/ubuntu-triage/tarball/master'
    ),
    install_requires=REQUIREMENTS,
    python_requires='>=3.4',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later"
        " (GPLv3+)",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Testing",
    ],
    keywords=['ubuntu', 'launchpad', 'triage', 'bugs'],
    packages=find_packages(),
    entry_points={
        'console_scripts':
            ['ubuntu-triage=ubuntu_triage.__main__:launch']
    },
    zip_safe=True
)
