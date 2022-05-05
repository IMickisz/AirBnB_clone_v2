#!/usr/bin/python3
"""
Module that contain the function do_pack
"""

from fabric.api import local
from time import strftime as date
from os import path


def do_pack():
    """Function that generates a .tgz archive from the web_static folder"""
    if path.exists("versions/") is False:
        local("mkdir versions/")
    try:
        file_path = "versions/web_stastic_{}{}{}{}{}{}.tgz".format(
            date("%Y"), date("%m"), date("%d"), date("%H"), date("%M"),
            date("%S"))
        local("tar -cvzf {} web_static".format(file_path))
        return file_path
    except Exception:
        return None
