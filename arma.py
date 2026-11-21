class Arma:
    def __init__(self, nombre, dano):
        self.nombre = nombre
        self.dano = dano

    def usar(self):
        print(f'Ataque con {self.nombre}')
        return self.dano

    