from fabric.api import *

def archive(build_id):
    env.filename = 'mkakeibo-%s.tar.gz'%(build_id)
    local('tar cvfz %s ./python'%(env.filename))

def deploy(build_id):
    archive(build_id)
    put(env.filename, env.filename)
