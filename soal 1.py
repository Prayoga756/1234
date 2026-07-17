akun = {
    "admin": "12345"
}

username = input("Username : ")
password = input("Password : ")

if username in akun and akun[username] == password:
    print("Login Berhasil")
else:
    print("Username atau Password Salah")