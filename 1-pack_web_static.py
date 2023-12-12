#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the contents"""

from datetime import datetime
from fabric import operations


def do_pack():
    """
    Function do_pack to generate the .tgz archive
    """
    # create local versions if they do not exist
    operations.local("mkdir -p ./versions")

    # file will be in format, web_static_<year><month><day><hour><minute><second>.tgz
    format = "%Y%m%d%H%M%S"
    file_time = datetime.utcnow().strftime(format)
    file_name = "web_static_"
    file_name += file_time
    file_name += ".tgz"

    # generate archive
    result = operations.local(
        "tar --create --verbose -z --file='./versions/{}' web_static".format(
            file_name))

    if result is not None:
        return result
    else:
        return None