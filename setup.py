# coding: utf-8

import os
import sys
from shutil import copy

if sys.version_info.major < 3:
    raise RuntimeError('Need Python 3 (or later) for rawzica!')

from setuptools import setup, find_packages
from rawzica import __version__


setup(
    name='rawzica',
    py_modules=['rawzica'],
    version=__version__,
    install_requires=(
    ),
    entry_points={
        'console_scripts': (
            'rawzica=rawzica:main'
        ),
    },
    data_files=(
        ('/etc/cron.daily/', ['rawzica']),
        ('/etc/', ['rawzica.conf']),
    ),
)
ETC_FILE = 'rawzica.conf'
if not os.path.exists('/etc/' + ETC_FILE):
    copy(os.path.join(__file__, ETC_FILE), '/etc/')
