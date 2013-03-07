from fabric.api import *

def deploy(build_id):
    env.filename = 'mkakeibo-%s.tar.gz'%(build_id)
    put(env.filename, env.filename)
