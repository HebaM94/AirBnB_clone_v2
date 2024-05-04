#!/usr/bin/python3
"""Fabric script that creates and distributes an archive to your
web servers, using the function deploy"""

from fabric.api import local, env, put, run
from os import path
from datetime import datetime

env.hosts = ['100.25.31.166', '54.175.6.240']


def do_pack():
    """Generate a .tgz archive from the contents of 
    the web_static folder."""
    try:
        current_time = datetime.now().strftime('%Y%m%d%H%M%S')
        archive_path = "versions/web_static_{}.tgz".format(current_time)
        local("mkdir -p versions")
        local("tar -czvf {} web_static".format(archive_path))
        return archive_path
    except:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers.
    """
    if not path.exists(archive_path):
        return False

    try:
        archive_name = archive_path.split('/')[-1]
        archive_folder = archive_name.split('.')[0]

        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(archive_folder))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(archive_name, archive_folder))
        run("rm /tmp/{}".format(archive_name))
        run("mv /data/web_static/releases/{}/web_static/*"
            " /data/web_static/releases/{}/"
            .format(archive_folder, archive_folder))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(archive_folder))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(archive_folder))
        return True
    except:
        return False


def deploy():
    """
    Deploy the archive to the web servers.
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
