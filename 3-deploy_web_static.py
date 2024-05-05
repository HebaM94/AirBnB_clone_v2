#!/usr/bin/python3
"""Fabric script that creates and distributes an archive to your
web servers, using the function deploy"""

from fabric.api import local, env, put, run, settings
from os.path import isdir, exists
from datetime import datetime


env.hosts = ['100.25.31.166', '54.175.6.240']


def do_pack():
    """Generate a .tgz archive from the contents of
    the web_static folder."""
    try:

        date = datetime.now().strftime('%Y%m%d%H%M%S')
        if isdir("versions") is False:
            local("mkdir -p versions")
        archive_path = "versions/web_static_{}.tgz".format(date)
        local("tar -czvf {} web_static".format(archive_path))
        return archive_path

    except Exception:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers.
    """
    if not exists(archive_path):
        return False

    try:
        archive_name = archive_path.split('/')[-1]
        archive_folder = archive_name.split('.')[0]
        pathname = "/data/web_static/releases/"

        put(archive_path, "/tmp/")
        run("mkdir -p {}{}/".format(pathname, archive_folder))
        run("tar -xzf /tmp/{} -C {}{}/"
            .format(archive_name, pathname, archive_folder))
        run("rm /tmp/{}".format(archive_name))
        return True

    except Exception as e:
        return False


def deploy():
    """
    Deploy the archive to the web servers.
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
