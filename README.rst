===========
 intbitset
===========

.. image:: https://img.shields.io/travis/inveniosoftware/intbitset.svg
        :target: https://travis-ci.org/inveniosoftware/intbitset

.. image:: https://img.shields.io/coveralls/inveniosoftware/intbitset.svg
        :target: https://coveralls.io/r/inveniosoftware/intbitset

.. image:: https://img.shields.io/github/tag/inveniosoftware/intbitset.svg
        :target: https://github.com/inveniosoftware/intbitset/releases

.. image:: https://img.shields.io/pypi/dm/intbitset.svg
        :target: https://pypi.python.org/pypi/intbitset

.. image:: https://img.shields.io/github/license/inveniosoftware/intbitset.svg
        :target: https://github.com/inveniosoftware/intbitset/blob/master/LICENSE


Installation
============

intbitset is on PyPI so all you need is: ::

    pip install intbitset

Documentation
=============

Provides an ``intbitset`` data object holding unordered sets of unsigned
integers with ultra fast set operations, implemented via bit vectors and
*Python C extension* to optimize speed and memory usage.

Emulates the Python built-in set class interface with some additional specific
methods such as its own fast dump and load marshalling functions.  ::

    >>> from intbitset import intbitset
    >>> x = intbitset([1,2,3])
    >>> y = intbitset([3,4,5])
    >>> x & y
    intbitset([3])
    >>> x | y
    intbitset([1, 2, 3, 4, 5])

``intbitset`` additionally support the `pickle protocol
<https://docs.python.org/2/library/pickle.html>`_, the `iterator protocol
<https://docs.python.org/2/library/stdtypes.html#iterator-types>`_ and can
behave like a ``sequence`` type.

Complete documentation is available at <http://intbitset.readthedocs.org> or
can be build using Sphinx: ::

    pip install Sphinx
    python setup.py build_sphinx

Testing
=======

Running the tests are as simple as: ::

    python setup.py test

License
=======

Copyright (C) 2013, 2014, 2015 CERN.

intbitset is free software; you can redistribute it and/or modify it under the
terms of the GNU General Public License as published by the Free Software
Foundation; either version 2 of the License, or (at your option) any later
version.

intbitset is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
intbitset; if not, write to the Free Software Foundation, Inc., 59 Temple
Place, Suite 330, Boston, MA 02111-1307, USA.

In applying this licence, CERN does not waive the privileges and immunities
granted to it by virtue of its status as an Intergovernmental Organization or
submit itself to any jurisdiction.
