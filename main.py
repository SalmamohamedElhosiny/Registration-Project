from Signup import signup
from Login import login
welcome = input('Enter signup or login: ').lower()
if welcome == 'signup':
    signup()
elif welcome == 'login':
    login()
else:
    print("Invalid option. Please enter 'signup' or 'login'.")