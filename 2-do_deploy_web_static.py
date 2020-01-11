#!/usr/bin/python3
# Script that distributes an archive to your web servers
from fabric.api import *
import os.path

env.hosts = ['34.73.226.110', '35.243.175.109']
env.user = "ubuntu"


def do_deploy(archive_path):
    """Function that deploy using fabric
    """
    if os.path.isfile(archive_path):
        try:
            file = archive_path.split("/")[1]
            directory = file.split(".")[0]
            put("{:s}".format(archive_path), "/tmp/")
            run("sudo mkdir -p /data/web_static/releases/{:s}".format(directory))
            run("sudo tar -xzf /tmp/{:s} -C\
                /data/web_static/releases/{:s}".format(file, directory))
            run("sudo rm /tmp/{:s}".format(file))
            run("sudo mv /data/web_static/releases/{:s}/web_static/*\
                /data/web_static/releases/{:s}".format(directory, directory))
            run("sudo rm -rf /data/web_static/releases/{:s}\
                /web_static".format(directory))
            run("sudo rm -rf /data/web_static/current")
            run("sudo ln -s /data/web_static/releases/{:s}\
                /data/web_static/current".format(directory))
            return True
        except:
            return False
    else:
        return False
