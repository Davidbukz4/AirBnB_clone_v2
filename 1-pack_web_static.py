#!/usr/bin/python3
"""
A fabric scipt that generates a .tgz archive file from my web_static folder
"""
from fabric.api import *
from datetime import datetime
import os


def do_pack():
    """ Compress files """
    try:
        if not os.path.exists('versions'):
            local('mkdir versions')
        date = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
        local('tar -cvzf versions/web_static_{}.tgz web_static/'.format(date))
        return ('versions/web_static_{}.tgz'.format(date))
    except Exception:
        return None
