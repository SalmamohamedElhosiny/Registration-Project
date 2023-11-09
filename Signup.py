def signup():
    while True:
        firstname = input('Enter your first name: ')
        if firstname.isalpha() and len(firstname) >= 3:
            break
        else:
            print('Invalid input. Please enter a valid alphabetical first name with at least 5 characters.')

    while True:
        lastname = input('Enter your last name: ')
        if lastname.isalpha() and len(lastname) >= 3:
            break
        else:
            print('Invalid input. Please enter a valid alphabetical last name with at least 5 characters.')
    while True:
       data_file = "Userdata.txt"
       username = input('Enter your username: ')
       with open(data_file, "r") as file:
        usernames = file.read().splitlines()
       if username in usernames and len(username) != 0 :
            print("This username is already taken!")
       else:
          with open(data_file, "a") as file:
            file.write(username + "\n")
          break
    from datetime import date
    year = int(input('Enter the year: '))
    month = int(input('Enter the month: '))
    day = int(input('Enter the day: '))
    birthdate = date(year, month, day)
    print("Birthdate:", birthdate)
    while True:
         email = input('Enter your email: ')
         from validate_email import validate_email
         email = "example@domain.com"
         valid = validate_email(email)
         if(valid) and len(email) != 0:
             pass
             break
         else:
             print('Invalid email address')
    
    password = input('Enter your password: ')
    if (len(password) > 8 and len(password) < 10):
        lowercase = False
        uppercase = False
        num = False
        specialcase = False
        for char in password:
            if(char.isdigit()):
             num = True
            if(char.islower()):
             lowercase = True
            if(char.isupper()):
             uppercase = True
            if(char.isalnum()):
             specialcase = True
    while True:        
       confirm_password = input('Please confirm password: ')
       if confirm_password == password and len(password) != 0:
         pass
         break
       else:
        print('Password and Confirm Password does not match!')
    with open('Userdata.txt', 'a') as file:
     file.write(f"{username}\n")
     file.write(f"{firstname}\n")
     file.write(f"{lastname}\n")
     file.write(f"{password}\n")
     file.write(f"{email}\n")
     file.write(f"{birthdate}\n")
    print('Welcome '+username)