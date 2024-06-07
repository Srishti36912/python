while True:
    username = input('Enter username:')
    password = input('Enter password:')
    if username == 'admin' and password == 'password':
        print('Login successful')
        break
    else:
        print('😮 Login failed')