from paver.easy import *
from paver.path import path
import os

@task
@cmdopts([
    ('format=', 'f', 'output format [silent, verbose, xunit]')
])
def test(options):
    format = options.test.format if 'format' in options.test else 'silent'
    opts = ['--with-doctest']
    if format == 'verbose': opts.append('--verbose')
    if format == 'xunit': opts.append('--with-xunit')

    files = path('python/mkakeibo').walk('*.py')
    sh('nosetests %s %s'%(' '.join(opts), ' '.join(files)))


@task
def start_fitnesse(options):
    os.chdir('test/fitnesse')
    sh('java -jar fitnesse.jar -e 0 -p 20942')

@task
def fitnesse(options):
    os.chdir('test/fitnesse')
    sh('java -jar fitnesse.jar -p 20942 -c "MkakeiboTop.AcceptanceTests?test&format=text"')

