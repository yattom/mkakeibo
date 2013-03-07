from paver.easy import *
import paver.doctools
from paver.setuputils import setup

import re

setup(
    name='mkakeibo',
    version='0.0',
    description='mobile kakeibo',
    author='Yattom',
    author_email='tsutomu.yasui@gmail.com',
    packages=['mkakeibo'],
    py_modules=['setup'],
    data_files=[('', ['paver-minilib.zip'])],
    requires=[re.sub('^([^=<>]*)([<>=]+[0-9\.]+)\n', '\\1(\\2)', n) for n in open('requirements.txt').readlines()]
)


@task
@needs('generate_setup', 'minilib', 'setuptools.command.sdist')
def sdist():
    pass
