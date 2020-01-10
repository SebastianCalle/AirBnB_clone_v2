#!/usr/bin/python3
# Script that generates a tgz arvhive from the contents of the web_static
from fabric.api import local
import datetime


def do_pack():
    """Function that pack all files of the web_static
    """
    now = datetime.datetime.now()
    local("mkdir -p versions/")
    file = "versions/web_static_{}{}{}{}.tgz".format(now.year, now.month,
                                                     now.minute, now.second)
    local("sudo tar -cvzf {} web_static".format(file))
    if file:
        return file
    return None
