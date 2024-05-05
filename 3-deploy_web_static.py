#!/usr/bin/python3
"""Fabric script that creates and distributes an archive to your
web servers, using the function deploy"""

from fabric.api import local, env, put, run
from os.path import basename, exists, isdir
from datetime import datetime


env.hosts = ['100.25.31.166', '54.175.6.240']


def do_pack():
    """Generate a .tgz archive from the contents of
    the web_static folder."""
    try:
        
        if isdir("versions") is False:
            local("sudo mkdir -p versions")

        date = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(date)

        local("tar -cvzf {} web_static".format(file_name))

        return file_name

    except Exception:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers.
    """
    if not exists(archive_path):
        return False

    try:

        file_name = archive_path.split("/")[-1]
        extract_folder = file_name.replace('.tgz', "")
        file_path = "/data/web_static/releases/"

        put(archive_path, '/tmp/')

        run('mkdir -p {}{}/'.format(file_path, extract_folder))

        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, file_path, extract_folder))

        run('rm /tmp/{}'.format(file_name))

        run('mv {0}{1}/web_static/* {0}{1}/'.format(file_path, extract_folder))

        run('rm -rf {}{}/web_static'.format(file_path, extract_folder))

        run('rm -rf /data/web_static/current')

        run('ln -s {}{}/ /data/web_static/current'.format(file_path, extract_folder))
        return True
    except Exception as e:
        print(e)
        return False


def deploy():
    """
    Deploy the archive to the web servers.
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
