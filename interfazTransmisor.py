# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfazTransmisor.ui'
#
# Created: Mon Dec 21 18:49:16 2015
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(800, 480)
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 20, 751, 231))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(30, 80, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 80, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.scrollArea = QtGui.QScrollArea(self.frame)
        self.scrollArea.setGeometry(QtCore.QRect(360, 50, 361, 161))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 359, 159))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.frame)
        self.doubleSpinBox.setGeometry(QtCore.QRect(270, 80, 71, 91))
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(360, 20, 66, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.frame_2 = QtGui.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(20, 260, 521, 191))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label_2 = QtGui.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(320, 20, 171, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(320, 60, 191, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(320, 100, 66, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(320, 140, 66, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.progressBar = QtGui.QProgressBar(self.frame_2)
        self.progressBar.setGeometry(QtCore.QRect(20, 20, 291, 23))
        self.progressBar.setProperty("value", 99)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.progressBar_2 = QtGui.QProgressBar(self.frame_2)
        self.progressBar_2.setGeometry(QtCore.QRect(20, 60, 291, 23))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName(_fromUtf8("progressBar_2"))
        self.progressBar_3 = QtGui.QProgressBar(self.frame_2)
        self.progressBar_3.setGeometry(QtCore.QRect(20, 100, 291, 23))
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setObjectName(_fromUtf8("progressBar_3"))
        self.progressBar_4 = QtGui.QProgressBar(self.frame_2)
        self.progressBar_4.setGeometry(QtCore.QRect(20, 140, 291, 23))
        self.progressBar_4.setProperty("value", 24)
        self.progressBar_4.setObjectName(_fromUtf8("progressBar_4"))
        self.frame_3 = QtGui.QFrame(Dialog)
        self.frame_3.setGeometry(QtCore.QRect(550, 260, 221, 191))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.label_6 = QtGui.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(20, 10, 161, 41))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(20, 50, 161, 41))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(20, 90, 161, 41))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.frame_3)
        self.label_9.setGeometry(QtCore.QRect(20, 130, 161, 41))
        self.label_9.setObjectName(_fromUtf8("label_9"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "ON", None))
        self.pushButton_2.setText(_translate("Dialog", "OFF", None))
        self.label.setText(_translate("Dialog", "ALARMAS", None))
        self.label_2.setText(_translate("Dialog", "POTENCIA DIRECTA (KW)", None))
        self.label_3.setText(_translate("Dialog", "POTENCIA REFLEJADA (KW)", None))
        self.label_4.setText(_translate("Dialog", "AUDIO IN", None))
        self.label_5.setText(_translate("Dialog", "AUDIO Tx", None))
        self.label_6.setText(_translate("Dialog", "TextLabel", None))
        self.label_7.setText(_translate("Dialog", "TextLabel", None))
        self.label_8.setText(_translate("Dialog", "TextLabel", None))
        self.label_9.setText(_translate("Dialog", "TextLabel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

