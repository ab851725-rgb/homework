class Person:
    def __init__(self, name, birth_day, occupation, higher_education=False):
        self.name = name
        self.birth_day = birth_day
        self.__occupation = occupation
        # self.friend_name = friend_name
        self.__higher_education = higher_education


    def get_education(self):
        return self.__higher_education

    def get_occupation(self):
        return self.__occupation

    def print_object(self):
        print(f"Привет, меня зовут {self.name}, высшее образование {self.get_education()}, я родился {self.birth_day}, работаю {self.get_occupation()}")

class Classmate(Person):
    def __init__(self, name, birth_day, occupation, higher_education, group):
        super().__init__(name, birth_day, occupation,  higher_education)
        self.group = group

    def print_object(self):
        print(f"Привет, меня зовут {self.name}, высшее образование {self.get_education()}  я родился {self.birth_day}, работаю {self.get_occupation()}, номер моей группы {self.group}")


class Friend(Person):
    def __init__(self, name, birth_day, occupation, higher_education, hobby):
        super().__init__(name, birth_day, occupation, higher_education)
        self.hobby = hobby

    def print_object(self):
        print(f"Привет, меня зовут {self.name}, высшее образование {self.get_education()}, я родился {self.birth_day}, работаю {self.get_occupation()}, мое хобби {self.hobby}")


class BestFriend(Friend):
    def __init__(self, name, birth_day, occupation, hobby, higher_education, shared_memory):
        super().__init__(name, birth_day, occupation, hobby, higher_education)
        self.memory = shared_memory

    def print_object(self):
        print(f"Привет, меня зовут {self.name}, высшее образование {self.get_education()}, я родился {self.birth_day}, работаю {self.get_occupation()}, мое хобби {self.hobby}, наше общее воспоминание {self.memory}")


classmate_1 = Classmate('Жека', '21.05.2000', 'программист', True, '8a')
classmate_2 = Classmate('Васек', '15.04.2007', 'рэпер', True, '4a')
friend_1 = Friend('Дима', '07.10.2010', 'дизайнер', False, 'волонтер')
friend_2 = Friend('Ян', '05.12.2005', 'адвокат', False, 'рэп')
me = Person('Арсений', '21.03.2003', 'rap', True)
bestt_friend = BestFriend('bimbo', '23.09.2031', 'айтишник', False, 'rap', 'rap rap rap',)

# classmate_1.printObject()
# classmate_2.printObject()
# friend_1.printObject()
# friend_2.printObject()
# me.printObject()
people = [classmate_1, classmate_2, friend_1, friend_2, me, bestt_friend]
for p in people:
    p.print_object()
