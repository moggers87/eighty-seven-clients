# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 Matt Molyneaux
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals, print_function

import requests

class Model(object):
    id = None
    api_path = "/api/v1/"

    def __init__(self, host):
        self.host = host

    @property
    def url(self):
        name = type(self).__name__.lower()
        url = "{host}{api_path}{name}/".format(
                    host=self.host,
                    api_path=self.api_path,
                    name=name,
                    )
        if self.id is not None:
            url = "{url}{id}/".format(url=url, id=self.id)

        return url

    def save(self):
        """Save object to the server"""
        api_method = getattr(requests, "put")
        if self.id is None:
            api_method = getattr(requests, "post")

        try:
            response = api_method(self.url)
        except requests.exceptions.ConnectionError:
            raise Exception("Connection error")

        if response.status_code > 499:
            raise Exception("Server error: %s" % response.status_code)
        elif response.status_code > 399:
            raise Exception("URL not found")

class PasswordStore(Model):
    pass

class PasswordRecord(Model):
    pass
