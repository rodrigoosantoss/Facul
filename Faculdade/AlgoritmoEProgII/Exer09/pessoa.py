class Pessoa:
  def __init__(self, cod, nome, endereco, telefone):
    self.__codigo = cod
    self.nome = nome
    self._endereco = endereco
    self._telefone = telefone
    
  def ImprimirNome(self):
    print(self.nome)

  def _ImprimirEndereco(self):
    print(self._endereco)

  def _ImprimirTelefone(self):
    print(self._telefone)

class PF(Pessoa):
  def __init__(self, cod, nome, endereco, telefone, cpf, idade, peso, altura):
    Pessoa.__init__(self, cod, nome, endereco, telefone)
    self.__cpf = cpf
    self.idade = idade
    self.peso = float(peso)
    self.altura = float(altura)
    self.imc = 0
    
  def ImprimirCPF(self):
    print(self.__cpf)

  def ImprimirIdade(self):
    print(self.idade)

  def ImprimirPeso(self):
    print(self.peso)

  def ImprimirAltura(self):
    print(self.altura)
    
  def CalcularIMC(self):
    self.imc = self.peso/(self.altura*self.altura)
    return self.imc
  
  def ImprimirIMC(self):
    print ("O IMC do %s é de %f" % (self.nome,self.CalcularIMC()))
      
class PJ(Pessoa):
  def __init__(self, cod, nome, endereco, telefone, cnpj, registroEstadual, nroEmpregados):
    Pessoa.__init__(self, cod, nome, endereco, telefone)
    self.__cnpj = cnpj
    self.__registroEstadual = registroEstadual
    self.nroEmpregados = nroEmpregados
    
  def ImprimirCNPJ(self):
    print(self.__cnpj)

  def ImprimirRegistroEstadual(self):
    print(self.__registroEstadual)
    
  def __EmitirNF(self):
    print(self.__registroEstadual)
    
  def pegarNF(self):
    return (self.__EmitirNF())
