import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui
class MainForm(QMainWindow):
     def __init__(self):
          super(MainForm, self).__init__()

          self.setWindowTitle("Calculator")
          self.setGeometry(200,200,500,500)
          self.setWindowIcon(QtGui.QIcon('download.png'))
          self.initUI()
     def initUI(self):
          self.lbl_number1 = QtWidgets.QLabel(self)
          self.lbl_number1.setText('Enter number 1: ')
          self.lbl_number1.move(50,30)

          self.txt_number1 = QtWidgets.QLineEdit(self)
          self.txt_number1.move(150,30)
          self.txt_number1.resize(200,32)

          self.lbl_number2 = QtWidgets.QLabel(self)
          self.lbl_number2.setText('Enter number 2: ')
          self.lbl_number2.move(50,80)

          self.txt_number2 = QtWidgets.QLineEdit(self)
          self.txt_number2.move(150,80)
          self.txt_number2.resize(200,32)

          self.btn_addition = QtWidgets.QPushButton(self)
          self.btn_addition.setText("Addition")
          self.btn_addition.move(150,130)
          self.btn_addition.clicked.connect(self.calculate)

          self.btn_subtraction = QtWidgets.QPushButton(self)
          self.btn_subtractionr.setText("Subtraction")
          self.btn_subtraction.move(150,170)
          self.btn_subtraction.clicked.connect(self.calculate)

          self.btn_multiplication = QtWidgets.QPushButton(self)
          self.btn_multiplication.setText("Multiplication")
          self.btn_multiplication.move(150,210)
          self.btn_multiplication.clicked.connect(self.calculate)

          self.btn_division = QtWidgets.QPushButton(self)
          self.btn_division.setText("Division")
          self.btn_division.move(150,250)
          self.btn_division.clicked.connect(self.calculate)

          self.lbl_result = QtWidgets.QLabel(self)
          self.lbl_result.setText('Result: ')
          self.lbl_result.move(150,290)
     def calculate(self):
          sender = self.sender().text()
          result = 0
          if sender == 'Addition':
               result = int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())
               
          elif sender == 'Subtraction':
               result = int(self.txt_sayi1.text()) - int(self.txt_sayi2.text())
               
          elif sender == 'Division':
               result = int(self.txt_sayi1.text()) / int(self.txt_sayi2.text())
               
          elif sender == 'Multiplication':
               result = int(self.txt_sayi1.text()) * int(self.txt_sayi2.text())
          
          self.lbl_sonuc.setText('Sonuç: '+ str(result))


          

def app():
     app = QApplication(sys.argv)
     win = MainForm()
     win.show()
     sys.exit(app.exec_())

app()
