from fabric.api import *
from fabric.contrib import files

@task
def deploy(build_id):
    undeploy()
    env.filename = 'mkakeibo.b%s.tar.gz'%(build_id)
    put('dist/' + env.filename)
    run('mkdir mkakeibo')
    run('tar zxvf %s -C mkakeibo'%(env.filename))

    _deploy_python()

def _deploy_python():
    run('tar zxvf mkakeibo/python/mkakeibo-0.0.tar.gz --strip-components=1 -C mkakeibo/python')
    with cd('mkakeibo/python'):
        run('pip install -r requirements.txt')
        run('paver start', pty=False) # pty=False is required to run as a daemon


@task
def undeploy():
    if files.exists('mkakeibo'):
        with cd('mkakeibo/python'):
            run('paver stop')
        run('rm -rf mkakeibo')


@task
def create_environment():
    put('env/.profile', '.profile')
    run('mkdir -p work')
    with cd('work'):
        # TODO: do something for tasks require root privilege
        #run('sudo apt-get install libssl-dev')
        _install_python()
        _install_python_packages()


@task
def clear_environment():
    run('rm -rf work bin lib share include')


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
