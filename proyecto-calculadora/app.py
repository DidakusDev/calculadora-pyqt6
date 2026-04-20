import sys
from PyQt6 import uic
from PyQt6.QtCore import QStandardPaths
from PyQt6.QtWidgets import *


class ventana:
    def __init__(self):
        
        self.main=uic.loadUi('GUI\main.ui')
        self.init_ui()
        self.lista_numeros=[]
        self.oper=[]

        #QDockWidget.setFixedWidth()  

    def init_ui(self):  
        self.main.btn0.clicked.connect(self.validar_numero0)
        self.main.Btn1.clicked.connect(self.validar_numero1)
        self.main.Btn2.clicked.connect(self.validar_numero2)
        self.main.Btn3.clicked.connect(self.validar_numero3)
        self.main.Btn4.clicked.connect(self.validar_numero4)
        self.main.Btn5.clicked.connect(self.validar_numero5)
        self.main.Btn6.clicked.connect(self.validar_numero6)
        self.main.Btn7.clicked.connect(self.validar_numero7)
        self.main.Btn8.clicked.connect(self.validar_numero8)
        self.main.Btn9.clicked.connect(self.validar_numero9)
        #calculos
        self.main.BtnSum.clicked.connect(self.suma)
        self.main.BtnRest.clicked.connect(self.resta)
        self.main.BtnMult.clicked.connect(self.mult)
        self.main.BtnDiv.clicked.connect(self.div)
        self.main.BtnIgual.clicked.connect(self.resultado)
        self.main.btnAC.clicked.connect(self.borrar_todo)
        self.main.btn00.clicked.connect(self.doble_cero)
        self.main.btnC.clicked.connect(self.borrar)
   
    def validar_numero0(self):
        pantalla=self.main.entrada.text()
        if pantalla in ['0','','+','-','x','/']:
            self.main.entrada.setText(str(self.numeros(num0=True)))
        else:
            self.main.entrada.setText(f'{pantalla + str(self.numeros(num0=True))}')
    def validar_numero1(self):
        pantalla=self.main.entrada.text()
        if pantalla in ['','+','-','x','/']:
            self.main.entrada.setText(str(self.numeros(num1=True)))
        else:
            self.main.entrada.setText(f'{pantalla + str(self.numeros(num1=True))}')
    def validar_numero2(self):
        pantalla=self.main.entrada.text()
        if pantalla in ['','+','-','x','/']:
            self.main.entrada.setText(str(self.numeros(num2=True)))
        else:
            self.main.entrada.setText(f'{pantalla + str(self.numeros(num2=True))}')
    def validar_numero3(self):
        pantalla=self.main.entrada.text()
        if pantalla in ['','+','-','x','/']:
            self.main.entrada.setText(str(self.numeros(num3=True)))
        else:
            self.main.entrada.setText(f'{pantalla + str(self.numeros(num3=True))}')
    def validar_numero4(self):
        pantalla=self.main.entrada.text()
        if pantalla in ['','+','-','x','/']:
            self.main.entrada.setText(str(self.numeros(num4=True)))
        else:
            self.main.entrada.setText(f'{pantalla + str(self.numeros(num4=True))}')
    def validar_numero5(self):
        pantalla=self.main.entrada.text()
        if pantalla in ['','+','-','x','/']:
            self.main.entrada.setText(str(self.numeros(num5=True)))
        else:
            self.main.entrada.setText(f'{pantalla + str(self.numeros(num5=True))}')
    def validar_numero6(self):
        pantalla=self.main.entrada.text()
        if pantalla in ['','+','-','x','/']:
            self.main.entrada.setText(str(self.numeros(num6=True)))
        else:
            self.main.entrada.setText(f'{pantalla + str(self.numeros(num6=True))}')
    def validar_numero7(self):
        pantalla=self.main.entrada.text()
        if pantalla in ['','+','-','x','/']:
            self.main.entrada.setText(str(self.numeros(num7=True)))
        else:
            self.main.entrada.setText(f'{pantalla + str(self.numeros(num7=True))}')
    def validar_numero8(self):
        pantalla=self.main.entrada.text()
        if pantalla in ['','+','-','x','/']:
            self.main.entrada.setText(str(self.numeros(num8=True)))
        else:
            self.main.entrada.setText(f'{pantalla + str(self.numeros(num8=True))}')
    def validar_numero9(self):
        pantalla=self.main.entrada.text()
        if pantalla in ['','+','-','x','/']:
            self.main.entrada.setText(str(self.numeros(num9=True)))
        else:
            self.main.entrada.setText(f'{pantalla + str(self.numeros(num9=True))}')
    def suma(self):
        pantalla=self.main.entrada.text()
        if pantalla == '':
            self.main.entrada.setText('0')
            pantalla=self.main.entrada.text()
        valor=float(pantalla)
        self.lista_numeros.append(valor)
        self.main.entrada.setText('+')
        self.oper.append(self.numeros(suma=True))
    def resta(self):
        pantalla=self.main.entrada.text()
        if pantalla == '':
            self.main.entrada.setText('0')
            pantalla=self.main.entrada.text()
        valor=float(pantalla)
        self.lista_numeros.append(valor)
        self.main.entrada.setText('-')
        self.oper.append(self.numeros(rest=True))
    def mult(self):
        pantalla=self.main.entrada.text()
        if pantalla == '':
            self.main.entrada.setText('0')
            pantalla=self.main.entrada.text()
        valor=float(pantalla)
        self.lista_numeros.append(valor)
        self.main.entrada.setText('x')
        self.oper.append(self.numeros(mult=True))
    def div(self):
        pantalla=self.main.entrada.text()
        if pantalla == '':
            self.main.entrada.setText('0')
            pantalla=self.main.entrada.text()
        valor=float(pantalla)
        self.lista_numeros.append(valor)
        self.main.entrada.setText('/')
        self.oper.append(self.numeros(div=True))
    def resultado(self):
        pantalla=self.main.entrada.text()
        if pantalla == '':
            self.main.entrada.setText('0')
            pantalla=self.main.entrada.text()
        valor=float(pantalla)
        self.lista_numeros.append(valor)
        if self.oper[-1]=='suma':
            valor=self.calculadora(int(self.lista_numeros[-2]),int(self.lista_numeros[-1]),suma=True)
        if self.oper[-1]=='rest':
            valor=self.calculadora(int(self.lista_numeros[-2]),int(self.lista_numeros[-1]),res=True)
        if self.oper[-1]=='mult':
            valor=self.calculadora(int(self.lista_numeros[-2]),int(self.lista_numeros[-1]),mult=True)
        if self.oper[-1]=='div':
            valor=self.calculadora(int(self.lista_numeros[-2]),int(self.lista_numeros[-1]),div=True)
        self.main.entrada.setText(str(valor))
        self.lista_numeros.clear()
        self.lista_numeros.append(valor)
    def borrar_todo(self):
        self.main.entrada.setText('')
    def doble_cero(self):
        pantalla=self.main.entrada.text()
        if pantalla in ['','0','+','-','x','/']:
            self.main.entrada.setText('0')
        else:
            self.main.entrada.setText(f'{pantalla}00')
    def borrar(self):
        pantalla=self.main.entrada.text()
        if pantalla in ['','+','-','x','/']:
            self.main.entrada.setText('')
        else:
            self.main.entrada.setText(pantalla[:-1])

    def calculadora(self,a=0,b=0,suma=None,res=None,mult=None,div=None):
        if suma:
            print(self.lista_numeros)
            res=a+b
        elif res:
            print(self.lista_numeros)
            res=a-b
        elif mult:
            print(self.lista_numeros)
            res=a*b
        elif div:
            print(self.lista_numeros)
            res=a/b
        return res
    
    def numeros(self,num0=None,num1=None,num2=None,num3=None,num4=None,num5=None,num6=None,num7=None,num8=None,num9=None,suma=None,rest=None,mult=None,div=None,igu=None):
        if num0:
            return 0
        elif num1:
            return 1
        elif num2:
            return 2
        elif num3:
            return 3
        elif num4:
            return 4
        elif num5:
            return 5
        elif num6:
            return 6
        elif num7:
            return 7
        elif num8:
            return 8
        elif num9:
            return 9
        elif suma:
            return 'suma'
        elif rest:
            return 'rest'
        elif mult:
            return 'mult'
        elif div:
            return 'div'
        elif igu:
            return 'resultado'
        else:
            return 0
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    vent=ventana()
    vent.main.show()
    sys.exit(app.exec())