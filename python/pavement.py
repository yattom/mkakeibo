from paver.easy import *
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
    data_files=[('', ['paver-minilib.zip', 'requirements.txt'])],
    requires=[re.sub('^([^=<>]*)([<>=]+[0-9\.]+)\n', '\\1(\\2)', n) for n in open('requirements.txt').readlines()]
)


@task
@needs('generate_setup', 'minilib', 'setuptools.command.sdist')
def sdist():
    pass


@task
def start():
    sh('python mkakeibo/web_main.py 8081 >> web.log 2>&1 &')

@task
def stop():
    ps = paver.easy.sh('ps -o pid,cmd -u `id -u`', capture=True)
    print 'DEBUG: '
    print ps
    for pid, cmd in [p.split(' ', 1) for p in ps.split('\n') if len(p) > 0]:
        if re.search('^python mkakeibo/web_main.py', cmd):
            sh('kill %s'%(pid))

@task
@cmdopts([
    ('format=', 'f', 'output format [silent, verbose, xunit]'),
    ('verbose', 'v', 'verbose and stdout (nosetests -v -s)')
])
def test(options):
    format = options.test.format if 'format' in options.test else 'silent'
    opts = ['--with-doctest']
    if format == 'verbose': opts.append('--verbose')
    if format == 'xunit': opts.append('--with-xunit')

    if 'verbose' in options.test:
        opts.append('-v -s')

    files = path('mkakeibo').walk('*.py')
    sh('nosetests %s %s'%(' '.join(opts), ' '.join(files)))

