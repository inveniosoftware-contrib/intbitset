Changes
=======

Here you can see the full list of changes between each intbitset
release.

Version 2.3.0 (released 2016-06-21)
-----------------------------------

Bug fixes
~~~~~~~~~

- Fixes implementation of `del x[123]` operator which was wrongly
  defined as `__del__` rather than `__delitem__`. (#40)
- Amends license reST reference from gpl to lgpl to avoid  detection
  as GPL when scanning the docs for licensing information.

Version 2.2.1 (released 2015-09-16)
-----------------------------------

Bug fixes
~~~~~~~~~

- Reorganizes MANIFEST.in and adds missing files.  (#28) (#29)


Version 2.2.0
-------------
* Removes coverage because it is not really supported for Cython modules.
* Automatically generates intbitset documentation by using Sphinx automodule
  functionality.
* Overall, amends documentation to be compatible with reStructuredText.
* Amends .update() and corresponding methods to accept also non-intbitset
  objects, such as lists or sets of integers respecting the set interface.
* Raises TypeError rather than terminating current process with a segmentation
  fault when None is used on the left side of an operation with an intbitset.
* Initial release of Docker configuration suitable for local developments.
* No longer returns self in fastload().
* Stops using `-march=native` for compilation, because it makes the compiler
  to optimize the code for only the currently used processor.

Version 2.1.1
-------------
* PyBytes_FromStringAndSize() fix in Python 2

Version 2.1
-----------
* Adds type checking for &, \|, etc. operators. The type of "self" was not
  checked.
* Adds support for new union() and isdisjoint() set methods.
* Updates intbitset interface to look like set built-in in Python 2.6.
* Supports initialization of an intbitset from a set.
* No crash when intbitset is on rhs.
* Complete Python 3.x support.

Version 2.0
-----------
* Packaged into a standalone git repository.
