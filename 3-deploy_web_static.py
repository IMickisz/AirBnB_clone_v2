#!/usr/bin/python3
"""
Module that contains the do_pack, do_deploy and deploy functions
"""

from fabric.api import local, put, run, env
from time import strftime as time
from os import path
env.hosts = ['35.196.253.106', '34.148.114.20']


def do_pack():
    """Function that generates a .tgz archive from the web_static folder"""
    if path.exists("versions/") is False:
        local("mkdir versions/")
    try:
        file_path = "versions/web_static_{}{}{}{}{}{}.tgz".format(time("%Y"),
                                                                  time("%m"),
                                                                  time("%d"),
                                                                  time("%H"),
                                                                  time("%M"),
                                                                  time("%S"))
        local("tar -cvzf {} web_static".format(file_path))
        return file_path
    except Exception:
        return None


def do_deploy(archive_path):
    """Function that distributes an archive to your web servers"""
    if path.exists(archive_path) is False:
        return False
    try:
        p = "/data/web_static/releases"
        file_name = archive_path.split("/")
        put("{}/{}".format(file_name[0], file_name[1]),
            "/tmp/{}".format(file_name[1]))
        name = file_name[1].split(".")
        run("sudo mkdir -p {}/{}/".format(p, name[0]))
        run("tar -xzf /tmp/{} -C {}/{}/".format(file_name[1], p, name[0]))
        run("rm /tmp/{}".format(file_name[1]))
        run("mv {}/{}/web_static/* {}/{}/".format(p, name[0], p, name[0]))
        run("rm -rf {}/{}/web_static".format(p, name[0]))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/{}/ /data/web_static/current".format(p, name[0]))
        return True
    except Exception:
        return False


def deploy():
    """Function that creates and distributes an archive to a web server"""
    archive = do_pack()
    if archive is None:
        return False
    return (do_deploy(archive))
