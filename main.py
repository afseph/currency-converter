from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtWidgets import QWidget, QSlider, QMessageBox, QPushButton, QDialog, QDialogButtonBox, QLabel, QVBoxLayout

import interface
import sys
from services import get_curr, convert


class Converter(QtWidgets.QMainWindow, interface.Ui_MainWindow):
    def __init__(self, curr):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.setWindowTitle("Конвертер валют")
        self.setWindowIcon(QtGui.QIcon("icon.ico"))
        self.curr = curr

        # ! Closes app if it is unable to get currencies list
        if self.curr != None:
            self.FromCurr.addItems(curr.keys())
            self.ToCurr.addItems(curr.keys())
        else:
            self.unable_to_get_currs()


        # ! Part that allows QComboBox to be searchable
        self.FromCurr.setEditable(True)
        self.FromCurr.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.FromCurr.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)

        self.ToCurr.setEditable(True)
        self.ToCurr.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.ToCurr.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)

        self.ConvertButton.clicked.connect(self.convert_values)


    def convert_values(self):
        """
        Function to get values and convert them to result
        """
        to_curr = self.ToCurr.currentText()
        from_curr = self.FromCurr.currentText()
        to_amount = self.ToAmount.text()
        if to_amount != "":
            if (res := convert(to_curr=to_curr,from_curr=from_curr,to_amount=to_amount,curr=self.curr)) != None:
                self.Result.setText(str(res))
            else:
                self.error()
        else:
            self.input_error()

    def input_error(self):
        """
        Message box that allows to informate user of input error
        """
        button = QMessageBox.information(self, "ИНФОРМАЦИЯ", "Поле не должно быть пустым.")


    def unable_to_get_currs(self):
        """
        Function that closes app if it is unable to get currencies list(by message box)
        """
        button = QMessageBox.critical(self, "ОШИБКА", "Произошла ошибка во время получения списка валют, проверьте подключение к инетрнету и перезапустите приложение.")
        if button == QMessageBox.Ok:
            sys.exit()


    def error(self):
        """
        Function that closes app if error happens
        """
        button = QMessageBox.critical(self, "ОШИБКА", "Произошла ошибка во время выполнения программы.")
        if button == QMessageBox.Ok:
            sys.exit()


if __name__ == "__main__":
    curr = get_curr()
    app = QtWidgets.QApplication([])
    converter = Converter(curr=curr)
    converter.show()
    app.exec()