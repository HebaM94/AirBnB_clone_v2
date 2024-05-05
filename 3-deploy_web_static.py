#!/usr/bin/python3
"""Fabric script that creates and distributes an archive to your
web servers, using the function deploy"""

from fabric.api import local, env, put, run
from os.path import basename, exists, isdir, join
from datetime import datetime


env.hosts = ['100.25.31.166', '54.175.6.240']


def do_pack():
    """Generate a .tgz archive from the contents of
    the web_static folder."""
    try:
        if not exists("web_static"):
            return None

        if isdir("versions") is False:
            local("sudo mkdir -p versions")

        date = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "web_static_{}.tgz".format(date)

        local("tar -cvzf versions/{} web_static".format(file_name))

        return "versions/{}".format(file_name)
    except Exception:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers.
    """
    if not exists(archive_path):
        return False

    try:

        put(archive_path, '/tmp/')

        archive_filename = basename(archive_path)
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


def deploy():
    """
    Deploy the archive to the web servers.
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
