#########
intbitset
#########

*****
About
*****

Provides an ``intbitset`` data object holding unordered sets of unsigned
integers with ultra fast set operations, implemented via bit vectors
and *Python C extension* to optimize speed and memory usage.

Emulates the Python built-in set class interface with some additional
specific methods such as its own fast dump and load marshalling
functions.

``intbitset`` additionally support the `pickle protocol <https://docs.python.org/2/library/pickle.html>`_, the `iterator protocol <https://docs.python.org/2/library/stdtypes.html#iterator-types>`_ and can behave like a ``sequence`` type.

Usage
=====
Example: ::

    >>> from intbitset import intbitset
    >>> x = intbitset([1,2,3])
    >>> y = intbitset([3,4,5])
    >>> x & y
    intbitset([3])
    >>> x | y
    intbitset([1, 2, 3, 4, 5])

Notes
=====
- Uses real bits to optimize memory usage, so may have issues with *endianness* if you transport serialized bitsets between various machine architectures.

- Please note that no bigger than ``__maxelem__`` elements can be added to an ``intbitset``.

- On modern CPUs, *vectorial instruction sets* (such as MMX/SSE) are exploited to further optimize speed.

***********
Performance
***********
Here is an example of performance gain with respect to traditional ``set`` of positive integers (example of *ipython* session): ::

    >>> ## preparation
    >>> from intbitset import intbitset
    >>> from random import sample
    >>> sparse_population1 = sample(range(1000000), 10000)
    >>> sparse_population2 = sample(range(1000000), 10000)
    >>> dense_population1 = sample(range(1000000), 900000)
    >>> dense_population2 = sample(range(1000000), 900000)
    >>> sparse_set1 = set(sparse_population1)
    >>> sparse_set2 = set(sparse_population2)
    >>> sparse_intbitset1 = intbitset(sparse_population1)
    >>> sparse_intbitset2 = intbitset(sparse_population2)
    >>> dense_set1 = set(dense_population1)
    >>> dense_set2 = set(dense_population2)
    >>> dense_intbitset1 = intbitset(dense_population1)
    >>> dense_intbitset2 = intbitset(dense_population2)
    >>> sorted(sparse_population1)[5000:5002]
    [500095, 500124]
    >>> in_sparse = 500095
    >>> not_in_sparse = 500096
    >>> sorted(dense_population1)[500000:500002]
    [555705, 555707]
    >>> in_dense = 555705
    >>> not_in_dense = 555706


For sparse sets, ``intbitset`` operations are typically **50 times faster** than set operations: ::

    >>> ## Sparse sets operations
    >>> %timeit sparse_set1 & sparse_set2
    1000 loops, best of 3: 263 µs per loop
    >>> %timeit sparse_intbitset1 & sparse_intbitset2 ## more than 20 times faster
    100000 loops, best of 3: 11.6 µs per loop
    >>> %timeit sparse_set1 | sparse_set2
    1000 loops, best of 3: 891 µs per loop
    >>> %timeit sparse_intbitset1 | sparse_intbitset2 ## almost 70 times faster
    100000 loops, best of 3: 12.8 µs per loop
    >>> %timeit sparse_set1 ^ sparse_set2
    1000 loops, best of 3: 1.09 ms per loop
    >>> %timeit sparse_intbitset1 ^ sparse_intbitset2 ## more than 80 times faster
    100000 loops, best of 3: 12.9 µs per loop
    >>> %timeit sparse_set1 - sparse_set2
    1000 loops, best of 3: 739 µs per loop
    >>> %timeit sparse_intbitset1 - sparse_intbitset2 ## almost 60 times faster
    100000 loops, best of 3: 12.5 µs per loop


For dense sets, ``intbitset`` operations are typically **5000 times faster** than set operations: ::

    >>> ## Dense sets operations
    >>> %timeit dense_set1 & dense_set2
    10 loops, best of 3: 62.1 ms per loop
    >>> %timeit dense_intbitset1 & dense_intbitset2 ## more than 5000 times faster
    100000 loops, best of 3: 12.3 µs per loop
    >>> %timeit dense_set1 | dense_set2
    10 loops, best of 3: 84.1 ms per loop
    >>> %timeit dense_intbitset1 | dense_intbitset2 ## more than 6000 times faster
    100000 loops, best of 3: 12.5 µs per loop
    >>> %timeit dense_set1 ^ dense_set2
    10 loops, best of 3: 64.2 ms per loop
    >>> %timeit dense_intbitset1 ^ dense_intbitset2 ## more than 5000 times faster
    100000 loops, best of 3: 12.6 µs per loop
    >>> %timeit dense_set1 - dense_set2
    10 loops, best of 3: 38.6 ms per loop
    >>> timeit dense_intbitset1 - dense_intbitset2 ## more than 3000 times faster
    100000 loops, best of 3: 12.8 µs per loop


Membership operations in ``intbitset`` behave in a comparable way than ``set`` objects, albeit with slightly better performance: ::

    >>> ## Membership tests
    >>> %timeit in_sparse in sparse_set1
    10000000 loops, best of 3: 66.8 ns per loop
    >>> %timeit in_sparse in sparse_intbitset1 ## 1.5 times faster
    10000000 loops, best of 3: 42.8 ns per loop
    >>> %timeit not_in_sparse in sparse_set1
    10000000 loops, best of 3: 71.3 ns per loop
    >>> %timeit not_in_sparse in sparse_intbitset1 ## 1.6 times faster
    10000000 loops, best of 3: 44.7 ns per loop
    >>> %timeit in_dense in dense_set1
    10000000 loops, best of 3: 61.8 ns per loop
    >>> %timeit in_dense in dense_intbitset1 ## 1.3 times faster
    10000000 loops, best of 3: 45.3 ns per loop
    >>> %timeit not_in_dense in dense_set1
    10000000 loops, best of 3: 45.5 ns per loop
    >>> %timeit not_in_dense in dense_intbitset1 ## similar speed
    10000000 loops, best of 3: 41.4 ns per loop

Serialising can be up to **30 times faster**: ::

    >>> ## serialization speed
    >>> ## note: internally intbitset compress using zlib so we are
    >>> ## going to also compress the equivalent set
    >>> from zlib import compress, decompress
    >>> from marshal import dumps, loads
    >>> %timeit loads(decompress(compress(dumps(sparse_set1))))
    100 loops, best of 3: 6.55 ms per loop
    >>> %timeit intbitset(sparse_intbitset1.fastdump()) ## 15% faster
    100 loops, best of 3: 5.63 ms per loop
    >>> %timeit loads(decompress(compress(dumps(dense_set1))))
    1 loops, best of 3: 565 ms per loop
    >>> %timeit intbitset(dense_intbitset1.fastdump()) ## almost 30 times faster for dense sets
    10 loops, best of 3: 20.9 ms per loop


Serialising can lead to **20 times smaller footprint**: ::

    >>> len(compress(dumps(sparse_set1)))
    29349
    >>> len(sparse_intbitset1.fastdump()) ## almost half the space
    16166
    >>> len(compress(dumps(dense_set1)))
    1363026
    >>> len(dense_intbitset1.fastdump()) ## 5% of the space for dense set
    70332

*********
Reference
*********

.. automodule:: intbitset
   :members:
   :undoc-members:
   :special-members:

******************
Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

****************
Additional Notes
****************

Notes on how to contribute, legal information and changelog are here for the
interested.

.. toctree::
   :maxdepth: 2

   contributing
   changelog
   license
