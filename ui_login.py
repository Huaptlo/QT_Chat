# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_login.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(579, 407)
        self.login_button = QtWidgets.QPushButton(Widget)
        self.login_button.setGeometry(QtCore.QRect(150, 240, 261, 51))
        self.login_button.setObjectName("login_button")
        self.textEdit = QtWidgets.QTextEdit(Widget)
        self.textEdit.setGeometry(QtCore.QRect(150, 140, 261, 70))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Dialog"))
        self.login_button.setText(_translate("Widget", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QDialog()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
