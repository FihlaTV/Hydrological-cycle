from PyQt4 import QtGui, QtCore
import sys
import inf2
import evtran2
import runoff
import pyqtgraph as pg
import webbrowser

class Main(QtGui.QMainWindow):
    def __init__(self, parent = None):
        super(Main, self).__init__(parent)
        self.setGeometry(50,50,1050,500)
        self.setWindowTitle("Hydrological Cycle")
        self.setWindowIcon(QtGui.QIcon('/home/hardik/evs/py.png'))

        self.comboBox=QtGui.QComboBox(self)
        self.comboBox.addItem("Infiltration")
        self.comboBox.addItem("Evapotranspiration")
        self.comboBox.addItem("Runoff")
        
        self.comboBox.move(50,250)
        self.comboBox.activated[str].connect(self.style_choice)

        # self.vp=Phonon.VideoPlayer()
        
        # self.vp.show()
        # self.media=Phonon.MediaSource("/home/hardik/evs/cycle.gif")
        # self.vp.load(self.media)
        # self.vp.play()

        
        self.status_txt = QtGui.QLabel()
        movie = QtGui.QMovie("/home/hardik/evs/cycle.gif")
        self.status_txt.setMovie(movie)
        movie.start()
        self.status_txt.resize(5000,5000)

     #    QWebView *view = new QWebView(parent);
     # view->load(QUrl("http://qt-project.org"));
     # view->show();

        self.web=QtGui.QPushButton("For more information click here")
        self.web.clicked.connect(lambda: webbrowser.open('https://hydrological-cycle.000webhostapp.com'))
        self.web.setStyleSheet("background-color:#f9be48;color:#000000")

        self.scrollLayout = QtGui.QFormLayout()
        self.scrollWidget = QtGui.QWidget()
        self.scrollWidget.setStyleSheet("background-color:#2db0ed;")
        self.scrollWidget.setLayout(self.scrollLayout)

        # scroll area
        self.scrollArea = QtGui.QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.scrollWidget)

        # main layout
        self.mainLayout = QtGui.QGridLayout()

        self.mainLayout.addWidget(self.comboBox,0,0)
        self.mainLayout.addWidget(self.scrollArea,1,2)
        self.mainLayout.addWidget(self.status_txt,1,0)
        self.mainLayout.addWidget(self.web)
        self.centralWidget = QtGui.QWidget()
        self.centralWidget.setLayout(self.mainLayout)

        # set central widget
        self.setCentralWidget(self.centralWidget)

    def style_choice(self):
        if self.comboBox.currentText() == "Infiltration":
            self.infil()
        elif self.comboBox.currentText()=="Evapotranspiration":
            self.evapo()
        elif self.comboBox.currentText()=="Runoff":
            self.runoff1()

    def infil(self):
        for i in reversed(range(self.scrollLayout.count())): 
            self.scrollLayout.itemAt(i).widget().setParent(None)
        self.scrollLayout.addRow(Test())

    def evapo(self):
        for i in reversed(range(self.scrollLayout.count())): 
            self.scrollLayout.itemAt(i).widget().setParent(None)

        self.scrollLayout.edef=QtGui.QLabel("Evapotranspiration:")
        self.scrollLayout.font=QtGui.QFont("Times",15,QtGui.QFont.Bold)
        self.scrollLayout.edef.setStyleSheet("color:#000000;margin-top:15%")
        self.scrollLayout.edef.setFont(self.scrollLayout.font)

        self.scrollLayout.edef1=QtGui.QLabel("The process by which water is transferred from land to atmosphere by evaporation from<br> the soil and other surfaces and by transpiration from plant.")
        self.scrollLayout.font1=QtGui.QFont("Times",10)
        self.scrollLayout.edef1.setStyleSheet("color:#000000;")
        self.scrollLayout.edef1.setFont(self.scrollLayout.font1) 
        self.scrollLayout.addWidget(self.scrollLayout.edef)
        self.scrollLayout.addWidget(self.scrollLayout.edef1)

        evtran2.evapotranspiration()



    def runoff1(self):
        for i in reversed(range(self.scrollLayout.count())): 
            self.scrollLayout.itemAt(i).widget().setParent(None)
        self.scrollLayout.addRow(Run())



class Run(QtGui.QWidget):
    def __init__( self, parent=None):
        super(Run, self).__init__(parent)
        self.reg_ex=QtCore.QRegExp("[0-9.]+")

        self.ilabel = QtGui.QLabel("Rainfall intensity(mm/hr):")
        self.ilabel.setStyleSheet("color:#000000;")
        self.iedit=QtGui.QLineEdit()
        self.text_validator=QtGui.QRegExpValidator(self.reg_ex,self.iedit)
        self.iedit.setValidator(self.text_validator)
        self.iedit.setPlaceholderText("Enter rainfall intensity here...") 

        self.arealabel = QtGui.QLabel("Catchment area(km<sup>2</sup>):")
        self.arealabel.setStyleSheet("color:#000000")
        self.areaedit=QtGui.QLineEdit()
        self.text_validator=QtGui.QRegExpValidator(self.reg_ex,self.areaedit)
        self.areaedit.setValidator(self.text_validator)
        self.areaedit.setPlaceholderText("Enter area here...")
 

        self.stlabel=QtGui.QLabel("Empirical runoff coefficient: ")
        self.stlabel.setStyleSheet("color:#000000")
        self.comboBox=QtGui.QComboBox(self)
        self.comboBox.addItem("1. Rocky and Impermeable")
        self.comboBox.addItem("2. Slightly Permeable,bare")
        self.comboBox.addItem("3. Slightly Permeable,Partly cultivated/Covered with vegetation")
        self.comboBox.addItem("4. Cultivated absorbent soil")
        self.comboBox.addItem("5. Sandy absorbent soil")
        self.comboBox.addItem("6. Forest")
        self.comboBox.move(50,250)
        self.comboBox.activated[str].connect(self.style1_choice)   
        self.comboBox.setStyleSheet("color:#000000;background-color:#ffffff;selection-background-color:#f9be48")     

        self.pushButton = QtGui.QPushButton('Submit')
        self.pushButton.setStyleSheet("background-color: #088c20;color:#000000")
        self.pushButton.clicked.connect(self.runof)

  

        self.layout = QtGui.QVBoxLayout()
        self.layout.addWidget(self.ilabel)
        self.layout.addWidget(self.iedit)
        self.layout.addWidget(self.arealabel)
        self.layout.addWidget(self.areaedit)
        self.layout.addWidget(self.stlabel)
        self.layout.addWidget(self.comboBox)
        self.layout.addWidget(self.pushButton)
        self.setLayout(self.layout)


    def style1_choice(self):
        self.st=self.comboBox.currentText()


    def runof(self):
        self.intensity=self.iedit.text()
        self.area=self.areaedit.text()
        if self.st=="1. Rocky and Impermeable":
            self.st=1
        elif self.st=="2. Slightly Permeable,bare":
            self.st=2
        elif self.st=="3. Slightly Permeable,Partly cultivated/Covered with vegetation":
            self.st=3
        elif self.st=="4. Cultivated absorbent soil":
            self.st=4
        elif self.st=="5. Sandy absorbent soil":
            self.st=5
        elif self.st=="6. Forest":
            self.st=6
        self.runoff2=runoff.runoff(self.intensity,self.area,self.st)
        self.label=QtGui.QLabel("Maximum Runoff = "+str(self.runoff2)+" mm")
        self.label.setStyleSheet("color:#000000")

        self.layout.addWidget(self.label)
        if self.layout.count() == 9:
            self.layout.itemAt(7).widget().setParent(None)
    def infi(self):
        self.s=self.s.text()
        self.k=self.k.text()
        inf2.infiltration(self.s,self.k)


class Test(QtGui.QWidget):
    def __init__( self, parent=None):
        super(Test, self).__init__(parent)
        self.reg_ex=QtCore.QRegExp("[0-9.]+")

        self.so = QtGui.QLabel("Sorptivity (mm/hr<sup>1/2</sup>):")
        self.so.setStyleSheet("color:#000000")
        self.s=QtGui.QLineEdit()
        self.text_validator=QtGui.QRegExpValidator(self.reg_ex,self.s)
        self.s.setValidator(self.text_validator)
        self.s.setPlaceholderText("Enter sorptivity here...") 

        self.ke = QtGui.QLabel("Hydraulic conductivity of soil (mm/hr):")
        self.ke.setStyleSheet("color:#000000")
        self.k=QtGui.QLineEdit()
        self.text_validator=QtGui.QRegExpValidator(self.reg_ex,self.k)
        self.k.setValidator(self.text_validator)
        self.k.setPlaceholderText("Enter hydraulic conductivity of soil here...")


        self.pushButton = QtGui.QPushButton('Submit')
        self.pushButton.clicked.connect(self.infi)
        self.pushButton.setStyleSheet("background-color: #088c20;color:#000000;font-size:20px")

        self.idef=QtGui.QLabel("Infiltration:")
        self.font=QtGui.QFont("Times",15,QtGui.QFont.Bold)
        self.idef.setStyleSheet("color:#000000;margin-top:15%")
        self.idef.setFont(self.font)

        self.idef1=QtGui.QLabel("Process by which water soaks into subsurface soil and moves into rocks through cracks<br> and pores. Water that infiltrates remains in the shallow soil layer, where it will gradually <br>move vertically and horizontally through the soil and subsurface material.")
        self.font1=QtGui.QFont("Times",10)
        self.idef1.setStyleSheet("color:#000000;")
        self.idef1.setFont(self.font1)    

        self.sdef=QtGui.QLabel("Sorptivity:")
        self.sdef.setStyleSheet("color:#000000;margin-top:15%")
        self.sdef.setFont(self.font)            

        self.sdef1=QtGui.QLabel("A parameter proportional to the square root of the water diffusivity and to the increase <br>in soil water content during infiltration.")
        self.sdef1.setStyleSheet("color:#000000;")
        self.sdef1.setFont(self.font1)  

        self.kdef=QtGui.QLabel("Hydrolic conductiviy:")
        self.kdef.setStyleSheet("color:#000000;margin-top:15%")
        self.kdef.setFont(self.font)            

        self.kdef1=QtGui.QLabel("It is the property of soil and rocks that describes the ease with which a fluid can move<br> through the pore spaces or fractures")
        self.kdef1.setStyleSheet("color:#000000;")
        self.kdef1.setFont(self.font1)  

        self.layout = QtGui.QVBoxLayout()
        self.layout.addWidget(self.so)
        self.layout.addWidget(self.s)
        self.layout.addWidget(self.ke)
        self.layout.addWidget(self.k)
        self.layout.addWidget(self.pushButton)
        self.layout.addWidget(self.idef)
        self.layout.addWidget(self.idef1)
        self.layout.addWidget(self.sdef)
        self.layout.addWidget(self.sdef1)
        self.layout.addWidget(self.kdef)
        self.layout.addWidget(self.kdef1)
        self.setLayout(self.layout)

    def infi(self):
        self.s=self.s.text()
        self.k=self.k.text()

        inf2.infiltration(self.s,self.k)
        


app = QtGui.QApplication(sys.argv)
myWidget = Main()
myWidget.show()
app.exec_()
