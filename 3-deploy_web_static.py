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

        date = datetime.now().strftime('%Y%m%d%H%M%S')
        if not path.isdir("versions"):
            local("sudo mkdir -p versions")
        archive_path = "versions/web_static_{}.tgz".format(date)
        size = os.path.getsize(archive_path)
        print("Packing web_static to {}".format(archive_path))
        final = local("tar -czvf {} web_static".format(archive_path))
        print("web_static packed: {} -> {}Bytes".format(archive_path, size))
        return archive_path

    except Exception as e:
        print(e)
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
        pathname = "/data/web_static/releases/"

        put(archive_path, "/tmp/")
        run("mkdir -p {}{}/".format(pathname, archive_folder))
        run("tar -xzf /tmp/{} -C {}{}/"
            .format(archive_name, pathname, archive_folder))
        run("rm /tmp/{}".format(archive_name))
        run("mv {}{}/web_static/*"
            " {}{}/"
            .format(pathname,archive_folder, pathname, archive_folder))
        run("rm -rf {}{}/web_static"
            .format(pathname, archive_folder))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current"
            .format(pathname, archive_folder))
        print("New version deployed!")

        return True

    except Exception as e:
        print(e)
        return False


def deploy():
    """
    Deploy the archive to the web servers.
    """
    archive_path = do_pack()
    if path.exists(archive_path) is False:
        return False
    return do_deploy(archive_path)
