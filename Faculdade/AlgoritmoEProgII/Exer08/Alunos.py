class Alunos:
  def __init__(self, codigo, nome, matricula):
    self.codigo = codigo
    self.nome = nome
    self.matricula = matricula

  def imprimiAluno(self):
    print('Código: {} - Nome: {} - Matrícula: {}'.format(str(self.codigo), self.nome, self.matricula))

############################

class Colegio(Alunos):
  def __init__(self, codigo, nome, matricula, ano):
    Alunos.__init__(self, codigo, nome, matricula)
    self.ano = ano

  def imprimirDadosAluno(self):
    print('Código: {} - Nome: {} - Matrícula: {} - Ano: {}'.format(str(self.codigo), self.nome, self.matricula, str(self.ano)))

############################

class Faculdade(Alunos):
  def __init__(self, codigo, nome, matricula, semestre):
    Alunos.__init__(self, codigo, nome, matricula)
    self.semestre = semestre
  
  def imprimirDadosFacul(self):
        print('Código: {} - Nome: {} - Matrícula: {} - Semestre: {}'.format(str(self.codigo), self.nome, self.matricula, str(self.semestre)))