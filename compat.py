import six

if six.PY3:
    def ord(a):
      return a
else:
    ord = ord
