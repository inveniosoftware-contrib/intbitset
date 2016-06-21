==================
 intbitset v2.3.0
==================

intbitset v2.3.0 was released on June 21, 2016.

About
-----

Provides an ``intbitset`` data object holding unordered sets of unsigned
integers with ultra fast set operations, implemented via bit vectors and
*Python C extension* to optimize speed and memory usage.

Bug fixes
---------

- Fixes implementation of `del x[123]` operator which was wrongly
  defined as `__del__` rather than `__delitem__`. (#40)
- Amends license reST reference from gpl to lgpl to avoid  detection
  as GPL when scanning the docs for licensing information.

Installation
------------

   $ pip install intbitset==2.3.0

Documentation
-------------

   http://intbitset.readthedocs.org/en/v2.3.0

Happy hacking and thanks for flying intbitset.

| Invenio Development Team
|   Email: info@invenio-software.org
|   IRC: #invenio on irc.freenode.net
|   Twitter: http://twitter.com/inveniosoftware
|   GitHub: https://github.com/inveniosoftware/intbitset
|   URL: http://invenio-software.org
