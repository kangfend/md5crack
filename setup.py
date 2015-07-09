#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  py-md5crack - Crack your md5 hash over http://haskiller.co.uk
#  Copyright (C) 2014 Sutrisno Efendi - kangfend@gmail.com
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages

setup(
    name = "py-md5crack",
    version = "0.1.0",
    url = 'https://github.com/kangfend/py-md5crack',
    description = 'Crack your md5 hash over http://haskiller.co.uk',
    license = 'GNU/GPL',
    author = 'Sutrisno Efendi',
    author_email = 'kangfend@gmail.com',
    packages = find_packages(),
    install_requires = ['pyquery', 'mechanize', 'Pillow'],
    scripts=['bin/md5crack'],
)
