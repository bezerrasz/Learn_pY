from PySide6.QtWidgets import QMainWindow, QMessageBox
from ui.Ui_janela1 import Ui_MainWindow

class MainController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Conecta o botão à função
        self.ui.btn_validar.clicked.connect(self.validar_nome)

    def validar_nome(self):
        nome = self.ui.txt_nome.text().strip()
        idade = self.ui.txt_idade.text().strip()

        if nome and idade:
            QMessageBox.information(self,"Sucesso",f"Seja Bem-Vindo, {nome} \n Você tem {idade} anos \n E vai morrer em {idade} segundos")
            return
        else:
            QMessageBox.warning(self,"Atenção","Você vai morrer em 3 dias")

        