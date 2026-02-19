class Retangulo:
    def __init__(self, largura, altura):
        self._largura = largura
        self._altura = altura
    @property
    def largura(self):
        return self._largura
    @largura.setter
    def largura(self, value):
        self._largura = value
    @property
    def altura(self):
        return self._altura
    @altura.setter
    def altura(self, value):
        self._altura = value
    def calcularArea(self):
        return f'O retângulo de altura {self._altura}cm e largura {self._largura}cm tem {self._altura * self._largura}cm^2 de área.'


altura = float(input("Digite a altura do retãngulo: "))
largura = float(input("Digite a largura do retângulo: "))
retangulo = Retangulo(largura, altura);
print(retangulo.calcularArea())