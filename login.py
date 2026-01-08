def login(username, password):
    if username == "admin" and password == "admin123":
        print("Login Successful")
    else:
        print("Login Failed")

login("admin", "admin123")