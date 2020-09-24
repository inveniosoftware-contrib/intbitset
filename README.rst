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

intbitset is on PyPI so all you need is a C compiler and pip: ::

    pip install intbitset

Documentation
=============

The ``intbitset`` library provides a set implementation to store sorted
unsigned integers either 32-bits integers (between ``0`` and
``2**31 - 1`` or ``intbitset.__maxelem__``) or an infinite range
with fast set operations implemented via bit vectors in a *Python C
extension* for speed and reduced memory usage.

The ``inbitset`` class emulates the Python built-in set class interface
with some additional specific methods such as its own fast dump and load
marshalling functions.  ::

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
behave like a ``sequence`` that can be sliced. Because the intergers are
always stored sorted, the fist element of a non-empty set `[0]` is also
the `min()` integer and the last element `[-1]` is also the `max()` integer
in the set.

When compared to the standard library ``set`` class, ``intbitset`` set
operations such as intersection, union and difference can be up to 5000
faster for dense integer sets.

Complete documentation is available at <http://intbitset.readthedocs.io> or
can be built using Sphinx: ::

    pip install Sphinx
    python setup.py build_sphinx

Testing
=======

Running the tests are as simple as: ::

    python setup.py test

Running the tests on multiple Python versions: ::

    pip install tox
    tox


Development
===========

To regenerate the C code with Cython: ::

    pip install cython
    cython intbitset/intbitset.pyx

Then commit the regenarted C source and update the CHANGE.rst


License
=======

Copyright (C) CERN and others

SPDX-License-Indetifier: LGPL-3.0-or-later

intbitset is free software; you can redistribute it and/or modify it under the
terms of the GNU Lesser General Public License as published by the Free Software
Foundation; either version 3 of the License, or (at your option) any later
version.

intbitset is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along with
intbitset; if not, write to the Free Software Foundation, Inc., 59 Temple
Place, Suite 330, Boston, MA 02111-1307, USA.

In applying this licence, CERN does not waive the privileges and immunities
granted to it by virtue of its status as an Intergovernmental Organization or
submit itself to any jurisdiction.
