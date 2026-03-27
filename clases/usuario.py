class Usuario:
    def __init__(self,username,password,email,estado):
        self.username = username
        self.password = password
        self.email = email
        self.estado = estado
    
    def login(self):
        pass
    def cambiar_estado(self):
        if(self.estado==True):
            self.estado=False
        else:
            self.estado=True

#instancia
user = Usuario("pepe","pepito123","pepe@gmail.com",True)
print(user.username)
print(user.estado)
user.cambiar_estado()
print(user.estado)