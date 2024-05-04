#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers,
using the function do_deploy"""


from fabric.api import env, put, run
import os
from datetime import datetime


env.hosts = ['100.25.31.166', '54.175.6.240']
env.user = 'ubuntu'
env.key_filename = '/path/to/your/ssh/private/key'


def do_deploy(archive_path):
    """Distributes an archive to web servers and deploys it"""

    if not os.path.exists(archive_path):
        return False

    archive_filename = archive_path.split('/')[-1]
    release_folder = '/data/web_static/releases/{}'.format(
            archive_filename.split('.')[0])
    file = "/tmp/" + archive_filename
    try:
        put(archive_path, '/tmp/')

        
        run('mkdir -p {}'.format(release_folder))
        
        run('tar -xzf /tmp/{} -C {}'.format(file, release_folder))

        run('rm /tmp/{}'.format(file))

        run('mv {}/web_static/* {}'.format(release_folder, release_folder))

        run('rm -rf {}/web_static'.format(release_folder))

        run('rm -rf /data/web_static/current')

        run('ln -s {} /data/web_static/current'.format(release_folder))

        return True
    except:
        return False
