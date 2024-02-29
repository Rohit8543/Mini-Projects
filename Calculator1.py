import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MyGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calculator')
        self.setGeometry(50, 50, 750, 400)



        # Title label
        self.title_label = QLabel("Calculator", self)
        self.title_label.setGeometry(0, 0, 800, 60)
        title_font = QFont("Arial", 24)
        title_font.setBold(True)
        self.title_label.setFont(title_font)
        self.title_label.setAlignment(Qt.AlignCenter)



        # Name label and entry
        self.num_label = QLabel("Number 1", self)
        self.num_label.setGeometry(20, 70, 170, 40)
        
        self.a = QLineEdit(self)
        self.a.setGeometry(190, 70, 170, 40)
        self.a.setFont(QFont("Arial", 20))
        

        # Password label and entry
        self.numlabel = QLabel("Number 2", self)
        self.numlabel.setGeometry(20, 150, 170, 40)

        self.result=QLabel("Result",self)
        self.result.setGeometry(20,220,170,40)

        self.output=QLabel(self)
        self.output.setGeometry(190,220,170,40)
        self.output.setStyleSheet("color:Blue")
        self.output.setFont(QFont("Arial",20))
        self.b = QLineEdit(self)
        self.b.setGeometry(190, 150, 170, 40)
        self.b.setFont(QFont("Arial", 20))
 

        # Login button
        self.button = QPushButton("Add", self)
        self.button.setGeometry(20, 300, 170, 40)
        self.button.clicked.connect(self.add)
        
        self.button1 = QPushButton("Subtract", self)
        self.button1.setGeometry(200, 300, 170, 40)
        self.button1.clicked.connect(self.sub)
        self.button2 = QPushButton("Multiply", self)
        self.button2.setGeometry(380, 300, 170, 40)
        self.button2.clicked.connect(self.mul)
        self.button3 = QPushButton("Division", self)
        self.button3.setGeometry(560, 300, 170, 40)
        self.button3.clicked.connect(self.div)

        self.button4 = QPushButton("Percentage", self)
        self.button4.setGeometry(20, 350, 170, 40)
        self.button4.clicked.connect(self.per)
        
        self.button5 = QPushButton("Exponential (Number1)", self)
        self.button5.setGeometry(200, 350, 170, 40)
        self.button5.clicked.connect(self.exp)
        
        self.button6 = QPushButton("Square Root (Number1)", self)
        self.button6.setGeometry(380, 350, 170, 40)
        self.button6.clicked.connect(self.sqr)
        
        self.button7=QPushButton("Log",self)
        self.button7.setGeometry(560,350,170,40)
        self.button7.clicked.connect(self.log)
    def add(self):
        a=float(self.a.text())
        b=float(self.b.text())
        res=a+b
        self.output.setText((str(res)))
        
    def sub(self):
        a=float(self.a.text())
        b=float(self.b.text())
        result=a-b
        self.output.setText((str(result)))
        
    def mul(self):
        a=float(self.a.text())
        b=float(self.b.text())
        result=a*b
        self.output.setText((str(result)))
        
    def div(self):
        a=float(self.a.text())
        b=float(self.b.text())
        if(b==0):
           self.output.setText("Not possible") 
        result=a/b
        self.output.setText((str(result)))

    def per(self):
        a=float(self.a.text())
        b=float(self.b.text())
        result=((a/b)*100)
        self.output.setText((str(result)))
    
 
        
    def exp(self):
        a=float(self.a.text()) 
        b=float(self.b.text())
        result=a**b
        self.output.setText((str(result))) 
        
    def sqr(self):
        a=float(self.a.text())
        res=a**a  
        self.output.setText((str(res)))
        
    def log(self):
        a=float(self.a.text())
        b=float(self.b.text())        
        res=math.log(a,b)  
        self.output.setText((str(res)))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_gui = MyGUI()
    my_gui.show()
    sys.exit(app.exec_())
