class User:

    user_count = 0
    default_role = 'user'
    default_password = '12345'

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        self.role = User.default_role
        self.password = User.default_password
        User.user_count += 1 


user1 = User('Igor', '992394294')
user2 = User('Ivan', '129030191')
user3 = User('Jeka', '912391393')
# print(user1.name, user1.phone_number)
print(f'users: {User.user_count}')