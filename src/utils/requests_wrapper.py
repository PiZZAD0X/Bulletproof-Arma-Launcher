# Tactical Battlefield Installer/Updater/Launcher
# Copyright (C) 2015 TacBF Installer Team.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

from __future__ import unicode_literals

import requests


class DownloadException(Exception):
    pass


def download_url(domain, *args, **kwargs):
    """
    Helper function that adds our error handling to requests.get.
    Feel free to refactor it.
    """

    if not domain:
        domain = "the domain"

    try:
        res = requests.get(*args, **kwargs)
    except requests.exceptions.ConnectionError as ex:
        try:
            reason_errno = ex.message.reason.errno
            if reason_errno == 11004:
                raise DownloadException('Could not resolve {}. Check your DNS settings.'.format(domain))
        except Exception:
            raise DownloadException('Could not connect to the server.')

        raise DownloadException('Could not connect to the server.')

    except requests.exceptions.Timeout:
        raise DownloadException('The server timed out while downloading data from the server.')

    except requests.exceptions.RequestException as ex:
        raise DownloadException('Could not download data from the server.')

    return res
