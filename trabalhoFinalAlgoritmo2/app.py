import pymysql
from PyQt5 import uic, QtWidgets
import aplicacao


banco = pymysql.connect(host='localhost',
                        database='DB_RODRIGO_FACUL',
                        user='root',
                        passwd='')



def funcao_menu():
    print('Helo world')

app = QtWidgets.QApplication([])
menu = uic.loadUi("menuAcesso.ui")
menu.pushButton_3.clicked.connect(aplicacao.funcao_principal())

menu.show()
app.exec()

