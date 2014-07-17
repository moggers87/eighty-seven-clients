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

import json

__all__ = ["PasswordStore", "PasswordRecord"]

class Model(object):
    """Base model for API objects

    Fields are accessible as attributes"""
    id = None

    def __init__(self, session):
        """Create a blank object

        `session` should be a subclass of requests.Session that prefixes all
        URLs with the API root
        """
        self._session = session

        # where fields are really stored :D
        self._fields = {}

    def __getattr__(self, field):
        if field in self._fields:
            return self._fields[field]
        elif self.id is None:
            raise AttributeError("%s could not be found" % field)
        else:
            raise AttributeError("%s cannot be found on object id %s" % (field, self.id))

    def _url(self):
        """Get URL of object or of object type if it doesn't have an ID """
        name = type(self).__name__.lower()
        url = "/{name}/".format(name=name)
        if self.id is not None:
            url = "{url}{id}/".format(url=url, id=self.id)

        return url

    def _prepare_data(self, update_fields=None):
        """Prepare data and spit out JSON"""
        if update_fields is None:
            data = self._fields
        else:
            data = {}
            for field in update_fields:
                data[field] = self._fields[field]

        return json.dumps(data)

    @classmethod
    def create(cls, session, data):
        """Creates object from API data

        It expects a single object as JSON or a dict"""
        obj = cls(session)

        if not isinstance(data, dict):
            data = json.loads(data)
        obj.id = data["id"]

        # we've either dealth with these fields or don't care about them
        del data["id"]
        del data["resource_uri"]

        for field in data:
            obj._fields[field] = data[field]

        return obj

    def delete(self):
        if self.id is None:
            raise Exception("This object has not been populated with data")
        response = self.session.delete(self._url())

        if response.status_code > 499:
            raise Exception("Server error: %s" % response.status_code)
        elif response.status_code > 399:
            raise Exception("URL not found")

        self.id = None
        self._fields = {}

    def save(self, update_fields=None):
        """Save object to the server"""
        # prepare data
        data = self._prepare_data(update_fields)

        # select HTTP method to use
        api_method = getattr(self._session, "patch")
        if self.id is None:
            api_method = getattr(self._session, "post")

        # exceptions will filter up
        response = api_method(self._url(), data=data)

        if response.status_code > 499:
            raise Exception("Server error: %s" % response.status_code)
        elif response.status_code > 399:
            raise Exception("URL not found")

        # work out ID
        if self.id is None:
            location = response.headers["location"]
            location = location.replace(self._url(), "").strip("/")
            self.id = location

class PasswordStore(Model):
    pass

class PasswordRecord(Model):
    pass
