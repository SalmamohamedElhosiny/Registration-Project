def login():
    while True:
      with open('Userdata.txt', 'r') as file:
        user_data = file.read().splitlines()
      username = input('Enter your username or your email: ' )
      if username in user_data and len(username) != 0:
         break
    while True:
      password = input('Enter your password: ')
      if password in user_data and len(password) != 0:
        pass
        break
      else:
        print('Invalid username. Please sign up.')
    print("Login successful")
    print('Welcome '+username)
login()