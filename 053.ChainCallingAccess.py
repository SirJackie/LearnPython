class Chain(object):
    def __init__(self, path=""):
        self.path = path

    def __getattr__(self, attr):
        return Chain("%s/%s" % (self.path, attr))

    def __call__(self, *args):
        _self = self
        for i in args:
            _self = Chain("%s/%s" % (_self.path, i))
        return _self

    def __str__(self):
        return self.path

    __repr__ = __str__


print(Chain().a("hello").b)
