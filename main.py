from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(402, 394)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 50, 381, 351))
        self.gridLayoutWidget.setAutoFillBackground(False)
        self.gridLayoutWidget.setStyleSheet("QPushButton{\n"
"    width:50px;\n"
"    height:30px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: gray;\n"
"}\n"
"\n"
"QPushButton:click{\n"
"    background-color: pink;\n"
"}")
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 190, 111);\n"
"    width:50px;\n"
"    height:50px;\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: gray;\n"
"}\n"
"\n"
"QPushButton:target{\n"
"    background-color: pink;\n"
"}")
        self.pushButton_6.setAutoDefault(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 2, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 190, 111);\n"
"    width:50px;\n"
"    height:50px;\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: gray;\n"
"}\n"
"\n"
"QPushButton:target{\n"
"    background-color: pink;\n"
"}")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setAutoFillBackground(False)
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 190, 111);\n"
"    width:50px;\n"
"    height:50px;\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: gray;\n"
"}\n"
"\n"
"QPushButton:target{\n"
"    background-color: pink;\n"
"}")
        self.pushButton_8.setAutoDefault(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 1, 1, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_14.setAutoFillBackground(False)
        self.pushButton_14.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 190, 111);\n"
"    width:50px;\n"
"    height:50px;\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: gray;\n"
"}\n"
"\n"
"QPushButton:target{\n"
"    background-color: pink;\n"
"}")
        self.pushButton_14.setAutoDefault(False)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_14, 4, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 190, 111);\n"
"    width:50px;\n"
"    height:50px;\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: gray;\n"
"}\n"
"\n"
"QPushButton:target{\n"
"    background-color: pink;\n"
"}")
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_10.setAutoFillBackground(False)
        self.pushButton_10.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 190, 111);\n"
"    width:50px;\n"
"    height:50px;\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: gray;\n"
"}\n"
"\n"
"QPushButton:target{\n"
"    background-color: pink;\n"
"}")
        self.pushButton_10.setAutoDefault(False)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 4, 1, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_12.setAutoFillBackground(False)
        self.pushButton_12.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 190, 111);\n"
"    width:50px;\n"
"    height:50px;\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: gray;\n"
"}\n"
"\n"
"QPushButton:target{\n"
"    background-color: pink;\n"
"}")
        self.pushButton_12.setAutoDefault(False)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 2, 3, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 190, 111);\n"
"    width:50px;\n"
"    height:50px;\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: gray;\n"
"}\n"
"\n"
"QPushButton:target{\n"
"    background-color: pink;\n"
"}")
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 2, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setAutoFillBackground(False)
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 190, 111);\n"
"    width:50px;\n"
"    height:50px;\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: gray;\n"
"}\n"
"\n"
"QPushButton:target{\n"
"    background-color: pink;\n"
"}")
        self.pushButton_7.setAutoDefault(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 1, 0, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_13.setAutoFillBackground(False)
        self.pushButton_13.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 190, 111);\n"
"    width:50px;\n"
"    height:50px;\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: gray;\n"
"}\n"
"\n"
"QPushButton:target{\n"
"    background-color: pink;\n"
"}")
        self.pushButton_13.setAutoDefault(False)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 3, 3, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 190, 111);\n"
"    width:50px;\n"
"    height:50px;\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: gray;\n"
"}\n"
"\n"
"QPushButton:target{\n"
"    background-color: pink;\n"
"}")
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 2, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 190, 111);\n"
"    width:50px;\n"
"    height:50px;\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: gray;\n"
"}\n"
"\n"
"QPushButton:target{\n"
"    background-color: pink;\n"
"}")
        self.pushButton_5.setAutoDefault(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_11.setAutoFillBackground(False)
        self.pushButton_11.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 190, 111);\n"
"    width:50px;\n"
"    height:50px;\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: gray;\n"
"}\n"
"\n"
"QPushButton:target{\n"
"    background-color: pink;\n"
"}")
        self.pushButton_11.setAutoDefault(False)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 1, 3, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setAutoFillBackground(False)
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 190, 111);\n"
"    width:50px;\n"
"    height:50px;\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: gray;\n"
"}\n"
"\n"
"QPushButton:target{\n"
"    background-color: pink;\n"
"}")
        self.pushButton_9.setAutoDefault(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 1, 2, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_15.setAutoFillBackground(False)
        self.pushButton_15.setStyleSheet("QPushButton{\n"
"    background-color: rgb(119, 118, 123);\n"
"    width:50px;\n"
"    height:50px;\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: silver;\n"
"}\n"
"\n"
"QPushButton:target{\n"
"    background-color: pink;\n"
"}")
        self.pushButton_15.setAutoDefault(False)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout.addWidget(self.pushButton_15, 0, 3, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_16.setAutoFillBackground(False)
        self.pushButton_16.setStyleSheet("QPushButton{\n"
"    background-color: rgb(61, 56, 70);\n"
"    width:50px;\n"
"    height:50px;\n"
"    border:none;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: gray;\n"
"}\n"
"\n"
"QPushButton:target{\n"
"    background-color: pink;\n"
"}")
        self.pushButton_16.setAutoDefault(False)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout.addWidget(self.pushButton_16, 0, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 420, 51))
        self.lineEdit.setStyleSheet("border: none;\n"
"background-color: rgb(164, 152, 57);")
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.addFunc()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton.setText(_translate("MainWindow", "1"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_14.setText(_translate("MainWindow", "/"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_10.setText(_translate("MainWindow", "0"))
        self.pushButton_12.setText(_translate("MainWindow", "-"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_13.setText(_translate("MainWindow", "*"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_11.setText(_translate("MainWindow", "+"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_15.setText(_translate("MainWindow", "="))
        self.pushButton_16.setText(_translate("MainWindow", "clear"))

    def addFunc(self):
        self.pushButton_10.clicked.connect(lambda:self.writeNumber(self.pushButton_10.text()))
        self.pushButton.clicked.connect(lambda:self.writeNumber(self.pushButton.text()))
        self.pushButton_2.clicked.connect(lambda:self.writeNumber(self.pushButton_2.text()))
        self.pushButton_3.clicked.connect(lambda:self.writeNumber(self.pushButton_3.text()))
        self.pushButton_4.clicked.connect(lambda:self.writeNumber(self.pushButton_4.text()))
        self.pushButton_5.clicked.connect(lambda:self.writeNumber(self.pushButton_5.text()))
        self.pushButton_6.clicked.connect(lambda:self.writeNumber(self.pushButton_6.text()))
        self.pushButton_7.clicked.connect(lambda:self.writeNumber(self.pushButton_7.text()))
        self.pushButton_8.clicked.connect(lambda:self.writeNumber(self.pushButton_8.text()))
        self.pushButton_9.clicked.connect(lambda:self.writeNumber(self.pushButton_9.text()))
        self.pushButton_11.clicked.connect(lambda:self.writeNumber(self.pushButton_11.text()))
        self.pushButton_12.clicked.connect(lambda:self.writeNumber(self.pushButton_12.text()))
        self.pushButton_13.clicked.connect(lambda:self.writeNumber(self.pushButton_13.text()))
        self.pushButton_14.clicked.connect(lambda:self.writeNumber(self.pushButton_14.text()))
        self.pushButton_16.clicked.connect(self.clear)

        self.pushButton_15.clicked.connect(self.results)

    def writeNumber(self, number):
        if self.lineEdit.text() == '0':
            self.lineEdit.setText(number)

        else:
            self.lineEdit.setText(self.lineEdit.text()+number)

    def clear(self):
        self.lineEdit.setText('')

    def results(self):
        res = eval(self.lineEdit.text())
        self.lineEdit.setText((str(res)))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
