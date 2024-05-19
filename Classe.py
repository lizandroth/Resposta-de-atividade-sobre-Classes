class Pessoa:
    def __init__(self,nome,peso,idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.parado = True
        self.comendo = False
        self.andando = False
        self.falando = False

    def parar(self):
        if self.andando:
            self.andando == False
            print(self.nome, "está parado")
        else:
            print(self.nome, "já está parado")

    def comer(self, alimento):
        if not self.comendo:
            self.comendo = True
            print(f' {self.nome} está comendo {alimento}')
        else:
            print(f'{self.nome}, já está comendo')

    def andar(self):
        if not self.andando:
            self.andando = True
            print(f'{self.nome}, está andando')
        else:
            print(f'{self.nome}, já está andando')

    def falar(self, comunicando):
        if not self.falando:
            self.falando = True
            print(f"{self.nome} fala: {comunicando}")
            self.falando = False
        else:
            print(f"{self.nome} já está falando.")

#Teste Objeto

p1 = Pessoa('Lizandro', 64, 25)

p1.andar()
p1.parar()
p1.comer('Lasanha')
p1.falar('Eae, de boa?')