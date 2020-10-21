class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    def getInfo(self):
        print(f'Nombre: {self.age}, Edad: {self.age}, correo: {self.email}') 