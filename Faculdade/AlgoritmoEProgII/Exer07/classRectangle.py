class Retangulo:
    def __init__(self, altura, larg):
        self.altura = altura
        self.larg = larg

    def areaComputada(self):
        area = (self.altura * self.larg)
        return area

    def imprimiAtributos(self):
        print('Altura = {}'.format(self.altura))
        print('Largura = {}'.format(self.larg))

r = Retangulo(2, 4)
Retangulo.imprimiAtributos(r)
print('#'*20)
print('Area do Retangulo = {}'.format(Retangulo.areaComputada(r)))
print('#'*20)