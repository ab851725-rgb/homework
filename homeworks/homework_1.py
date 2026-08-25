class Person:
    def __init__(self, name = None, birth_day = None, occupation = None, higher_educaton = None):
        self.name = name
        self.birth_day = birth_day
        self.occupation = occupation
        self.higher_educaton = higher_educaton

    def printObject(self):
        print(f"имя - {self.name}, дата рождения - {self.birth_day}, профессия - {self.occupation}, высшее образование - {self.higher_educaton}")

    def inputFunction(self):
        inputName = input('введите имя: ')
        self.name = inputName
        inputBirth_day = input('введите дату рождения: ')
        self.birth_day = inputBirth_day
        inputOccupation = input('какая ваша профессия: ')
        self.occupation = inputOccupation
        while True:
            inputHigher_education = input('есть ли у вас высшее образование? ' \
            'только (да/нет): ').lower()
            if inputHigher_education == 'да':
                self.higher_educaton = True
                break
            elif inputHigher_education == 'нет':
                self.higher_educaton = False
                break
            else:
                print('введите только да или нет')
                

user_1 = Person()
user_1.inputFunction()
user_1.printObject()


ivan = Person('Ivan', '10.07.2003', 'ingener', True)
ivan.printObject()
chizh = Person('Denis', '05.01.2004', 'military boy', False)
chizh.printObject()
arseny = Person('Arseny', '21.03.2003', 'rapper', False)
arseny.printObject()