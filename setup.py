# -*- coding: utf-8 -*-
#
# This file is part of intbitset
# Copyright (C) CERN and others
#
# SPDX-License-Identifier: LGPL-3.0-or-later
#
# intbitset is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# intbitset is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with intbitset; if not, write to the Free Software Foundation,
# Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
#
# In applying this licence, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.

"""C-based extension implementing fast integer bit sets."""

from setuptools import Extension
from setuptools import setup

setup(
    name="intbitset",
    version="4.0.0",
    url="http://github.com/inveniosoftware-contrib/intbitset/",
    license="LGPL-3.0-or-later",
    author="Invenio collaboration, maintained by Philippe Ombredanne and AboutCode.org",
    author_email="pombredanne@nexb.com",
    description="C-based extension implementing fast integer bit sets.",
    long_description=open("README.rst").read(),
    long_description_content_type="text/x-rst",
    package_dir={"": "intbitset"},
    py_modules=["intbitset_helper", "intbitset_version"],
    ext_modules=[
        Extension(
            "intbitset",
            ["intbitset/intbitset.c", "intbitset/intbitset_impl.c"],
            # extra_compile_args = []
            # For debug -> extra_compile_args=['-ftree-vectorizer-verbose=2']
        )
    ],
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Cython",
        "Programming Language :: C",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
    ],
    extras_require={"tests": ["pytest", "pytest-xdist"]}
)
