=========
intbitset
=========

.. image:: https://travis-ci.org/inveniosoftware/intbitset.png?branch=master
    :target: https://travis-ci.org/inveniosoftware/intbitset
.. image:: https://coveralls.io/repos/inveniosoftware/intbitset/badge.png?branch=master
    :target: https://coveralls.io/r/inveniosoftware/intbitset
.. image:: https://pypip.in/v/intbitset/badge.png
   :target: https://crate.io/packages/intbitset/
.. image:: https://pypip.in/d/intbitset/badge.png
   :target: https://crate.io/packages/intbitset/
.. image:: https://d2weczhvl823v0.cloudfront.net/kaplun/intbitset/trend.png
   :target: https://bitdeli.com/free

Installation
============
intbitset is on PyPI so all you need is: ::

    pip install intbitset

Documentation
=============
Provides an intbitset data object holding unordered sets of unsigned
integers with ultra fast set operations, implemented via bit vectors
and Python C extension to optimize speed and memory usage.

Emulates the Python built-in set class interface with some additional
specific methods such as its own fast dump and load marshalling
functions.  Uses real bits to optimize memory usage, so may have
issues with endianness if you transport serialized bitsets between
various machine architectures.

Please note that no bigger than __maxelem__ elements can be added to
an intbitset. ::

    >>> x = intbitset([1,2,3])
    >>> y = intbitset([3,4,5])
    >>> print x & y
    intbitset([3])
    >>> print x | y
    intbitset([1, 2, 3, 4, 5])

Complete documentation is available at <http://intbitset.readthedocs.org> or can be build using Sphinx: ::

    pip install Sphinx
    python setup.py build_sphinx

Testing
=======
Running the tests are as simple as: ::

    python setup.py test

or (to also show test coverage) ::

    source run-tests.py

License
=======
Copyright (C) 2013 CERN.

intbitset is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

intbitset is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with intbitset; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

In applying this licence, CERN does not waive the privileges and immunities granted to it by virtue of its status as an Intergovernmental Organization or submit itself to any jurisdiction.
