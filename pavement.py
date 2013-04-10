from paver.easy import *
from paver.path import path
import os

project_root = os.path.abspath(os.path.dirname(__file__))

@task
@cmdopts([
    ('format=', 'f', 'output format [silent, verbose, xunit]')
])
def test(options):
    format = options.test.format if 'format' in options.test else 'silent'
    opts = ['--format=%s'%(format)]
    os.chdir('python')
    sh('paver test ' + ' '.join(opts))


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

FITNESSE_SERVER_PORT = 20942
FITNESSE_ONESHOT_PORT = 20942

def fitnesse_opts(port):
    opts= [
        '-p %d'%(port),
    ]
    return opts


@task
def start_fitnesse(options):
    os.chdir('test/fitnesse')
    cmd = 'java -jar fitnesse.jar ' + ' '.join(fitnesse_opts(FITNESSE_SERVER_PORT))
    if os.name == 'nt':
        sh('start ' + cmd)
    else:
        sh(cmd + ' &')

@task
def stop_fitnesse(options):
    sh('java -cp fitnesse.jar fitnesse.Shutdown -p %d'%(FITNESSE_SERVER_PORT))

@task
def fitnesse(options):
    sh('run-fitnesse ' + ' '.join(fitnesse_opts(FITNESSE_ONESHOT_PORT)) + ' -c "MkakeiboTop.AcceptanceTests?suite&format=xml" | awk "/^<\?xml/{out=1}/^<\/testResults>/{print;out=0}out==1{print}" > fitnesse-result.xml')

