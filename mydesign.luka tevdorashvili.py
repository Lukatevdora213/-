from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1151, 829)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 1131, 781))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.graphicsView.setFont(font)
        self.graphicsView.setObjectName("graphicsView")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 60, 1011, 91))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(240, 180, 661, 71))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(30, 300, 1051, 391))
        self.listView.setObjectName("listView")
        font = QtGui.QFont()
        font.setPointSize(15)  
        self.listView.setFont(font)

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 575, 1051, 120))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        self.textEdit.hide()

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 730, 311, 28))
        self.pushButton.setObjectName("pushButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1151, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.comboBox.currentIndexChanged.connect(self.load_songs)
        self.model = QtCore.QStringListModel()
        self.listView.setModel(self.model)
        self.listView.clicked.connect(self.display_lyrics)

        self.pushButton.clicked.connect(self.restart_program)  
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", " ქართული სიმღერების ტექსტები და აკორდები"))
        self.comboBox.setItemText(0, _translate("MainWindow", "აირჩიეთ ჟანრი"))
        self.comboBox.setItemText(1, _translate("MainWindow", "ხალხური"))
        self.comboBox.setItemText(2, _translate("MainWindow", "ქალაქური"))
        self.comboBox.setItemText(3, _translate("MainWindow", "გალობა"))
        self.pushButton.setText(_translate("MainWindow", "გადატვირთვა"))
        
    def load_songs(self, index):
        songs = {
            1: ["გთხოვთ აირჩიოთ სასურველი სიმღერა","ჩაკრულო", "გარეკახური", "მრავალჟამიერი", "ცანგალა", "თუ ასე ტურფა იყავი", "ჩანამღერი"],
            2: ["თბილისო", "ქუთაისო ჩემო", "ოღონდ შენთან მამყოფინა", "მინდვრად დაგიჭერ პეპელას"],
            3: ["წმინდაო ღმერთო", "ჯვარსა შენსა", "სულო ჩემო", "ღმერთი უფალი"]
        }

        if index in songs:
            self.model.setStringList(songs[index])
        else:
            self.model.setStringList([])
        self.textEdit.hide()

    def display_lyrics(self, index):
        song = index.data()
        lyrics = {
            "ჩაკრულო": "ჰაი ხიდის თავს შევკრავთ პირობას,\n"
                      "ჩვენ გავხდეთ ღვიძლი ძმანია,\n"
                      "ჩავუხტეთ მუხრან ბატონსა,\n"
                      "თავს დავანგრიოთ ბანია",
            "გარეკახური": "ქუდი გვერძე დაგიხურავს,\n"
                          "ჰარალალი ჰარალალო,\n"
                          "ქუდი გვერძე დაგიხურავს ამპარტავანსა გეხარო,\n"
                          "ჰარალალი ჰარალალო",
            "მრავალჟამიერი": "მრავალჟაიმიერ მრავალო მრავალჟამიერ,\n"
                             "ღმერთმა ინებოს მრავალო ჩვენი სიცოცხლე,\n"
                             "მრაავალ - ჟააიმიერ...",
            "თბილისო": "გიტარის აკორდები - Am-Dm-Fm-c-E7\n\n"
                       "თბილისო მზის და ვარდების მხარეო,\n"
                       "უშენოდ სიცოცხელეც არმინდაა,\n"
                       "სადარის სხვაგან ახალი ვარაზი,\n"
                       "სადარის ჭაღარა მთაწმინდა...",
            "ქუთაისო ჩემო": "გიტარის აკორდები - Cm-Fm-G \n\n"
                            "ქუთაისო ჩემო,ჩემო დედულეთო,\n"
                            "გული საგულედან ლამის ამომენთოს,\n"
                            "ჩემი ბაღის კიდე ხავსიანი ეზო,\n"
                            "ძველი ჯაჭვის ხიდი არ მოშალო ღმერთო...",
            "წმინდაო ღმერთო": "წმინდაო ღმერთო,წმინდაო ძლიერო,წმინდაო უკუდაო შეგვიწყალენ ჩვენ!\n"
                             "დიდება მამასა და ძესა წმინდასა სულსა აწ და მარადის და უკუნითი უკუნითამდე ამინ!\n"
                             "უფალო შეგვიწყალენ!უფალო შეგვწყალენ!უფალო შეგვწყალენ!",
            "ჯვარსა შენსა": "ჯვარსა შენსა,თაყვანი ვსცეთ მეუფეო,\n"
                           "და წმინდასა აღდგომასა შენსა"
        }
        if song in lyrics:
            self.textEdit.setText(lyrics[song])
        else:
            self.textEdit.setText("ტექსტი ამ სიმღერისთვის მიუწვდომელია.")
        self.textEdit.show()

    def restart_program(self):
        self.comboBox.setCurrentIndex(0)
        self.model.setStringList([])
        self.textEdit.clear()
        self.textEdit.hide()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
