class Animal:
    def eat(self):
        pass

    def move(self):
        pass


class Flying(Animal):
    def feed_baby_bird(self):
        print('animal feeding lil bird')

    def move(self):
        print('animal flying')


class Swimming(Animal):
    def sleep(self):
        print('animal sleeping')

    def move(self):
        print('animal swimming')

class Duck(Flying, Swimming):
    pass


donald_duck = Duck()
donald_duck.move()
donald_duck.eat()   
donald_duck.feed_baby_bird()
donald_duck.sleep()