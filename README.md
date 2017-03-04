grcpass
=======

Description
-----------

This little script scrapes out passwords from [http://grc.com/passwords.htm](http://grc.com/passwords.htm) and returns them in named tuple.

Usage
-----

In python code

```python
import grcpass

passwords = grcpass.generate()

print(passwords.hex)
print(passwords.ascii)
print(passwords.alpha)
```


Or in shell
```shell
grcpass -h
```
