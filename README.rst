grcpass
=======

Description
-----------

This little script scrapes out passwords from
http://grc.com/passwords.htm and returns them in named tuple.

Installation
------------

.. code:: shell

    pip install grcpass

Usage
-----

In python code

.. code:: python

    import grcpass

    passwords = grcpass.generate()

    print(passwords.hex)
    print(passwords.ascii)
    print(passwords.alpha)

Or in shell

.. code:: shell

    grcpass -h
