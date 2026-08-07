class Person:
    def __init__(self, name, birth_day , occupation , friend_name):
        self.name = name
        self.birth_day = birth_day
        self.occupation = occupation
        self.friend_name = friend_name

    def printObject(self):
        print(f"Привет, меня зовут {self.name}, я друг {self.friend_name}, я родился {self.birth_day}, работаю {self.occupation}")

class Classmate(Person):
    def __init__(self, name, birth_day, occupation, friend_name, group):
        super().__init__(name, birth_day, occupation, friend_name)
        self.group = group

    def printObject(self):
        print(f"Привет, меня зовут {self.name}, я друг {self.friend_name}, я родился {self.birth_day}, работаю {self.occupation}, номер моей группы {self.group}")


class Friend(Person):
    def __init__(self, name, birth_day, occupation, friend_name, hobby):
        super().__init__(name, birth_day, occupation, friend_name)
        self.hobby = hobby

    def printObject(self):
        print(f"Привет, меня зовут {self.name}, я друг {self.friend_name}, я родился {self.birth_day}, работаю {self.occupation}, мое хобби {self.hobby}")


class Best_friend(Friend):
    def __init__(self, name, birth_day, occupation, friend_name, shared_memory):
        super().__init__(name, birth_day, occupation, friend_name)
        self.memory = shared_memory

    def printMemory(self):
        print(f"наше общее воспоминание {self.memory}")


classmate_1 = Classmate('Жека', '21.05.2000', 'программист', 'Ванька', '8a')
classmate_2 = Classmate('Васек', '15.04.2007', 'рэпер', 'Ванька', '4a')
friend_1 = Friend('Дима', '07.10.2010', 'дизайнер', 'Ванька', 'волонтер')
friend_2 = Friend('Ян', '05.12.2005', 'адвокат', 'Ванька', 'рэп')
me = Person('Арсений', '21.03.2003', 'rap', 'Ванька')
# bestt_friend = ('bimbo', '23.09.2031', 'rap rap rap', )

# classmate_1.printObject()
# classmate_2.printObject()
# friend_1.printObject()
# friend_2.printObject()
# me.printObject()
people = [classmate_1, classmate_2, friend_1, friend_2, me]
for p in people:
    p.printObject()
    
