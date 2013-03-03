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


FITNESSE_OPTS = [
    '-d %s'%(path('test/fitnesse').abspath()),
    '-p 20942'
]

@task
def start_fitnesse(options):
    sh('start-fitnesse ' + ' '.join(FITNESSE_OPTS))

@task
def stop_fitnesse(options):
    sh('stop-fitnesse ' + ' '.join(FITNESSE_OPTS))

@task
def fitnesse(options):
    sh('run-fitnesse ' + ' '.join(FITNESSE_OPTS) + ' -c "MkakeiboTop.AcceptanceTests?test&format=text"')

