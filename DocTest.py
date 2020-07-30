class Dict(dict):
    '''
    A Dict Class that support both x["y"] and x.y access style.

    >>> d = Dict()

    >>> d["key1"] = "value1"
    >>> d.key1
    'value1'

    >>> d.key2 = "value2"
    >>> d["key2"]
    'value2'

    >>> d.empty
    Traceback (most recent call last):
      ...
    AttributeError: 'Dict' object has no attribute empty

    >>> d["empty"]
    Traceback (most recent call last):
      ...
    KeyError: 'empty'

    '''

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as e:
            raise AttributeError(r"'Dict' object has no attribute %s" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__ == "__main__":
    import doctest
    doctest.testmod()
