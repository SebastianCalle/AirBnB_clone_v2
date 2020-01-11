#!/usr/bin/python3
# Script that distributes an archive to your web servers
from fabric.api import *
from os.path import exists

env.hosts = ['34.73.226.110', '35.243.175.109']
env.user = "ubuntu"


def do_deploy(archive_path):
    """Function that deploy using fabric
    """
    if exists(archive_path):
        file = archive_path.split("/")[1]
        directory = file.split(".")[0]
        print(directory)
        put("{}".format(archive_path), "/tmp/")
        run("sudo mkdir -p /data/web_static/releases/{}".format(directory))
        run("sudo tar -xzf /tmp/{} -C\
            /data/web_static/releases/{}".format(file, directory))
        run("rm /tmp/{}".format(file))
        run("sudo mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}".format(directory, directory))
        run("sudo rm -rf /data/web_static/releases/{}/web_static".format(directory))
        run("rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{}\
            /data/web_static/current".format(directory))
        return True
    else:
        return False
