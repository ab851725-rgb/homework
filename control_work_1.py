class Animal:
    def __init__(self, name, age, sound):
        self.__name = name
        self.__age = age
        self.sound = sound

    def set_age(self, amount):
        self.__age = amount

    def set_name(self, new_name):
        self.__name = new_name

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def make_sound(self):
        print(f'животное {self.__name} издает звук: {self.sound}')

class Dog(Animal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
    def make_sound(self):
        print(f'собака {self.get_name()} издает звук: {self.sound}')

class Cat(Animal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
    def make_sound(self):
        print(f'кот {self.get_name()} издает звук: {self.sound}')


animal_1 = Dog('bobby', 12, 'woof woof')
animal_1.make_sound()
animal_2 = Cat('muzya', 8, 'mew mew')
animal_2.make_sound()
animal_2.set_name('Jeka')
animal_2.set_age(6)
animal_1.set_age(17)
animal_1.set_name('jandosik')
print(animal_2.get_age())
print(animal_2.get_name())
print(animal_1.get_age())
print(animal_1.get_name())