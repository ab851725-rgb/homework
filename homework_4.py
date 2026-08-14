class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    @classmethod
    def validate_phone_number(cls, phone_number):
        if len(phone_number) == 10:
            return True

class Contact_List:
    all_contacts = []   
    @classmethod
    def add_contact(cls, name, phone_number):
        if not Contact.validate_phone_number(phone_number):
            print(f'некоректный номер телефона: {phone_number}')
            return None
        user = Contact(name, phone_number)
        cls.all_contacts.append(user)
        return user

print(Contact_List.all_contacts) # []

Contact_List.add_contact("Вася Пупкин", "0700100200")
Contact_List.add_contact("Виктор Цой", "0500123456")

# так как all_contacts является списком, можно пройти по нему циклом
for contact in Contact_List.all_contacts:
    print(contact.name, contact.phone_number)
    # Вася Пупкин 0700100200
    # Виктор Цой 0500123456

Contact_List.add_contact("John Doe", "5551234") 
# получаем ValueError потому что количество цифр не подходит