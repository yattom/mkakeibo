from fabric.api import *
from fabric.contrib import files

@task
def deploy(build_id):
    env.filename = 'mkakeibo-%s.tar.gz'%(build_id)
    put(env.filename, env.filename)


@task
def create_environment():
    put('env/.profile', '.profile')
    run('mkdir -p work')
    with cd('work'):
        run('sudo apt-get install libssl-dev')
        _install_python()
        _install_python_packages()


@task
def clear_environment():
    run('rmdir -rf work bin lib shared include')


def _install_python():
    if files.exists('Python-2.7.3'):
        return
    run('wget http://www.python.org/ftp/python/2.7.3/Python-2.7.3.tgz')
    run('tar zxvf Python-2.7.3.tgz')
    with cd('Python-2.7.3'):
        run('./configure --prefix $HOME')
        run('make install')

def _install_python_packages():
    run('wget http://python-distribute.org/distribute_setup.py')
    run('python distribute_setup.py')
    run('easy_install pip')
