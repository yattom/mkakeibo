from fabric.api import *

def deploy(build_id):
    env.filename = 'mkakeibo-%s.tar.gz'%(build_id)
    put(env.filename, env.filename)


def create_environment():
    put('env/.profile', '.profile')
    run('mkdir -p work')
    with cd('work'):
        install_python()


def install_python():
    run('wget http://www.python.org/ftp/python/2.7.3/Python-2.7.3.tgz')
    run('tar zxvf Python-2.7.3.tgz')
    with cd('Python-2.7.3'):
        run('./configure --prefix $HOME')
        run('make install')
