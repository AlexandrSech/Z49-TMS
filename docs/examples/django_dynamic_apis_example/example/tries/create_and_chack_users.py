from users.models import Users, Profile


user_name_template = {'login': 'User{}', 'password': 123,
                      'user_id': '', 'first_name': 'F_name{}', 'last_name': 'L_name{}',
                      'email': 'some_email_of_user{}@example.com',
                      'age': '{}'}


def create_users():
    for i in range(1, 11):
        new_user = Users()

