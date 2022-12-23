
def check_credentials(username, password):
    if username == "username" and password == "password":
        return True
    return False

username = "username"
password = "password123"

print(check_credentials(username, password))
