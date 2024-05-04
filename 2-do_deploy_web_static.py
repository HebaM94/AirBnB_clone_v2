#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers,
using the function do_deploy"""


from fabric.api import env, put, run
import os
from datetime import datetime


env.hosts = ['100.25.31.166', '54.175.6.240']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Distributes an archive to web servers and deploys it"""

    if not os.path.exists(archive_path):
        return False

    try:
        for host in env.hosts:
            print("[{}] Executing task 'do_deploy'".format(host))

        put(archive_path, '/tmp/')

        archive_filename = os.path.basename(archive_path)
        release_folder = '/data/web_static/releases/{}'.format(
            archive_filename[:-4])
        run('mkdir -p {}'.format(release_folder))
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_folder))

        run('rm /tmp/{}'.format(archive_filename))

        run('mv {}/web_static/* {}'.format(release_folder, release_folder))

        run('rm -rf {}/web_static'.format(release_folder))

        run('rm -rf /data/web_static/current')

        run('ln -s {} /data/web_static/current'.format(release_folder))

        print("New version deployed!")
        
        return True
    except Exception as e:
        print(e)
        return False
