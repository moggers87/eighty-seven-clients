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

from eightyseven_cli.config import JSONStore

from requests.auth import HTTPDigestAuth
import requests

class Session(requests.Session):
    def __init__(self, url):
        self._prepend_url = url
        super(Session, self).__init__()

    def prepare_request(self, request):
        request.url = self._prepend_url + request.url
        return super(Session, self).prepare_request(request)

def main():
    print("Hello")
