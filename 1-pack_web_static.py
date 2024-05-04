#!/usr/bin/python3
"""Fabric script that generates a .tgz archive
from the contents of the web_static folder of your
AirBnB Clone repo, using the function do_pack"""


from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    try:
        local("sudo mkdir -p versions").strftime("%Y%m%d%H%M%S")

        date = datetime.now()
        file_name = "web_static_{}.tgz".format(date)

        final = local("tar -cvzf versions/{} web_static".format(file_name))

        return "versions/{}".format(file_name)
    except Exception:
        return None
