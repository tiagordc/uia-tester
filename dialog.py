# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 120)
        Dialog.setWindowTitle("UIA Tester")
        self.detect = QtWidgets.QPushButton(Dialog)
        self.detect.setGeometry(QtCore.QRect(520, 60, 101, 41))
        self.detect.setStyleSheet("font-size: 16px; font-weight: normal;")
        self.detect.setText("Detect")
        self.detect.setObjectName("detect")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 601, 51))
        self.label.setStyleSheet("font-size: 24px")
        self.label.setText("Value:")
        self.label.setObjectName("label")
        self.copy = QtWidgets.QPushButton(Dialog)
        self.copy.setEnabled(False)
        self.copy.setGeometry(QtCore.QRect(410, 60, 101, 41))
        self.copy.setStyleSheet("font-size: 16px; font-weight: normal;")
        self.copy.setText("Copy")
        self.copy.setObjectName("copy")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
