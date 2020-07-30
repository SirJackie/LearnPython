class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):
    def __init__(self, name):
        super().__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super().__init__(name, 'bigint')

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):

        #
        # Skip the Change to Class "Model"
        #

        # If the New Class is "Model" , do nothing
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)

        # Else , print the Class Name
        print('Found model: %s' % name)


        #
        # Copy all "Field" Properties to variable "mapping"
        #

        # Create a empty Dict called "mappings"
        mappings = dict()

        # Iterate all the Properties in this Class
        for key, value in attrs.items():

            # If this Property is a instance inherit form "Field"
            if isinstance(value, Field):

                # Print out the name and value of this Property
                print('Found mapping: %s ==> %s' % (key, value))

                # Add this Property to Dict "mapping"
                mappings[key] = value


        #
        # Delete all "Field" Properties from this class
        #

        # Iterate all keys inside mapping (which is the "Field" Properties)
        for k in mappings.keys():

            # Delete it from this class
            attrs.pop(k)


        #
        # Saving All the Things
        #

        # Save all "Field" Properties to a Property "__mappings__"
        # Inside this Class
        attrs['__mappings__'] = mappings

        # Save the Class Name as the Table name
        attrs['__table__'] = name

        # Return the changed class
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

class User(Model):
    id = IntegerField("id")
    name = StringField("username")
    email = StringField("email")
    password = StringField("password")

u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()
