Welcome to intbitset's documentation!
=====================================

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

Contents
--------

FIXME

.. toctree::
   :maxdepth: 2

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Additional Notes
----------------

Notes on how to contribute, legal information and changelog are here for the
interested.

.. toctree::
   :maxdepth: 2

   contributing
   changelog
   license
