class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute %s" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__ == "__main__":
    d = Dict()
    d["key1"] = "value1"
    d.key2 = "value2"
    print(d.key1)
    print(d["key2"])
    # Result :
    # value1
    # value2
