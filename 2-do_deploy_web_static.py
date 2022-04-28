#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy.
"""


from fabric.api import local
from fabric.api import run
from fabric.api import put
from fabric.api import env
import os.path
from os import path

env.hosts = ['34.74.115.199', '34.74.58.247']


def do_pack():
    """Function that does a pack with the files of the folder web_static."""
    if path.exists('versions/') is False:
        local("mkdir versions/")
    filename = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        stf("%Y"),
        stf("%m"),
        stf("%d"),
        stf("%H"),
        stf("%M"),
        stf("%S"))
    a = local("tar -cvzf {} web_static".format(filename))
    if a.failed is True:
        return None
    return filename


def do_deploy(archive_path):
    """ Function that deploys archive path. """
    if path.exists(archive_path) is False:
        return False

    no_ver = archive_path.split("/")
    no_ext = no_ver[1].split(".")
    p = "/data/web_static/releases"

    a = put("versions/{}".format(no_ver[1]), "/tmp/{}".format(no_ver[1]))
    if a.failed is True:
        return False
    a = run("mkdir -p /data/web_static/releases/{}".format(no_ext[0]))
    if a.failed is True:
        return False
    a = run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(
        no_ver[1], no_ext[0]))
    if a.failed is True:
        return False
    a = run("rm /tmp/{}".format(no_ver[1]))
    if a.failed is True:
        return False
    a = run("mv {}/{}/web_static/* {}/{}/"
            .format(p, no_ext[0], p, no_ext[0]))
    if a.failed is True:
        return False
    a = run("rm -rf /data/web_static/releases/{}/web_static"
            .format(no_ext[0]))
    if a.failed is True:
        return False
    a = run("rm -rf /data/web_static/current")
    if a.failed is True:
        return False
    a = run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(no_ext[0]))
    if a.failed is True:
        return False
    print("New version deployed!")
    return True
