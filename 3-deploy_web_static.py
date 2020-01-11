#!/usr/bin/python3
# Script that diply web static into the servers
from fabric.api import *
import datetime
import os.path

env.hosts = ['34.73.226.110', '35.243.175.109']
env.user = "ubuntu"


def do_pack():
    """Function that pack all files of the web_static
    """
    now = datetime.datetime.now()
    local("mkdir -p versions/")
    file = "versions/web_static_{}{}{}{}{}.tgz".format(now.year, now.month,
                                                     now.day, now.minute,
                                                       now.second)
    local("sudo tar -cvzf {} web_static".format(file))
    if file:
        return file
    return None


def do_deploy(archive_path):
    """Function that deploy using fabric
    """
    try:
        if not os.path.exists(archive_path):
            return False
        file = archive_path.split("/")[1]
        directory = file.split(".")[0]
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{:s}/".format(directory))
        run("tar -xzf /tmp/{:s} -C /data/web_static/releases/{:s}/"
            .format(file, directory))
        run("rm /tmp/{:s}".format(file))
        run("mv /data/web_static/releases/{:s}/web_static/* \
            /data/web_static/releases/{:s}/".format(directory, directory))
        run("rm -rf /data/web_static/releases/{:s}/web_static"
            .format(directory))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{:s} /data/web_static/current"
            .format(directory))
        return True
    except:
        return False


def deploy():
    """ Function deploy into the servers
    """
    archive_path = do_pack()
    if not os.path.exists(archive_path):
        return False
    value = do_deploy(archive_path)
    return value
