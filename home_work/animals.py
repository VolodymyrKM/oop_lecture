from types import MethodType


class Animals:

    def __init__(self, nick_name, age):
        self.nick_name = nick_name
        self.age = age

    def __repr__(self):
        return f'{self.__class__.__name__} ' \
               f'(nick name: "{self.nick_name}",' \
               f' age: {self.age})'

    def __str__(self):
        return f'I\'m {self.__class__.__name__}' \
               f' my name is "{self.nick_name}",' \
               f' and I\'m {self.age} years old.'

    def _register_behaviour(self, func):
        self._behaviour = MethodType(func, self)

    @property
    def custom_behavior(self):
        behaviour_method = getattr(self, '_behaviour', None)
        if behaviour_method:
            return behaviour_method()
        else:
            raise AttributeError('You must first register a behaviour_method.')

    @property
    def able_to_walk(self):
        return f'{self.__class__.__name__} {self.nick_name} can walk...'

    behaviour = property(fset=_register_behaviour)


class Lion(Animals):

    @property
    def eat_meet(self):
        return f'{self.__class__.__name__} {self.nick_name} eat meet.'


class Wolf(Animals):

    @property
    def hunt(self):
        return f'{self.__class__.__name__} {self.nick_name} is hunting...'


class Bear(Wolf):

    @property
    def make_noise(self):
        result = super().hunt
        return f'{result} and terrible screaming!!!'


class Pantera(Bear):

    @property
    def run_fast(self):
        return f'{self.__class__.__name__} {self.nick_name} running fast...'


class Crocodile(Animals):

    @property
    def able_to_swimming(self):
        return f"{self.__class__.__name__} {self.nick_name} is swimming..."


class WildAnimal(Wolf, Crocodile):

    @property
    def all_possibility(self):
        return f'{super().hunt}, {super().able_to_swimming}, {super().able_to_walk}'


if __name__ == '__main__':
    hyena = WildAnimal('Gena', 8)


    def funny_noise(self):
        return f"{self.nick_name} makes funny noise..."


    hyena.behaviour = funny_noise
    print(hyena.custom_behavior)
    print(hyena.all_possibility)

    p = Pantera('Bagira', 3)

    print(p.make_noise)
    print(p)
