class MyFirstMeta(type):
    def __new__(cls, name, bases, attr):
        obj = super().__new__(cls, name, bases, attr)
        obj.say_hello_obj = lambda self: f'Hello from {self} is a type  of {type(self.__class__)}'
        obj.say_hello_cls = lambda self: f'Hello from {cls} is a type of {type(cls.__class__)} '
        return obj


class MyClass(metaclass=MyFirstMeta):
    pass


class MyTest(MyClass):
    pass


if __name__ == '__main__':
    mt = MyTest()
    print(mt.say_hello_cls())
    print((mt.say_hello_obj()))
