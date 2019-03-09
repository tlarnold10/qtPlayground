import sys
from PyQt5.QtWidgets import QDialog, QApplication, QInputDialog
import openpyxl, math, pdb
from demo import *

class MyForm(QDialog):
	def __init__(self):
		super().__init__()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.namePushButton.clicked.connect(self.dispmessage)
		self.show()
	def dispmessage(self):
		name, ok = QInputDialog.getText(self, "Input Dialog", "Enter your name")
		if ok and name:
			self.ui.nameLineEdit.setText(name)
if __name__=="__main__":
	app = QApplication(sys.argv)
	w = MyForm()
	w.show()
	sys.exit(app.exec_())
