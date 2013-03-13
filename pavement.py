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
@cmdopts([
    ('build-id=', 'b', '')
])
def build(options):
    if path('build').exists():
        sh('rm -rf build')
    sh('mkdir -p build/python')
    sh('paver sdist', cwd='python')
    sh('cp python/dist/* build/python')

    sh('mkdir -p dist')
    sh('tar cvfz dist/mkakeibo.b%(build_id)s.tar.gz -C build .'%options.build)


FITNESSE_OPTS = [
    '-p 20942'
]
FITNESSE_RUNNING_OPTS = FITNESSE_OPTS + [
    '-d %s'%(path('test/fitnesse').abspath()),
]

@task
def start_fitnesse(options):
    sh('start-fitnesse ' + ' '.join(FITNESSE_RUNNING_OPTS))

@task
def stop_fitnesse(options):
    sh('stop-fitnesse ' + ' '.join(FITNESSE_OPTS))

@task
def fitnesse(options):
    sh('run-fitnesse ' + ' '.join(FITNESSE_RUNNING_OPTS) + ' -c "MkakeiboTop.AcceptanceTests?test&format=xml" | awk "/^<\?xml/{out=1}/^<\/testResults>/{print;out=0}out==1{print}" > fitnesse-result.xml')

