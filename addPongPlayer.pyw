import sys, psycopg2
from PyQt5.QtWidgets import QDialog, QApplication
import pymsgbox
from pongPlayerAdd import *
class MyForm(QDialog):
	def __init__(self):
		super().__init__()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.addPlayer)
		self.show()
	def addPlayer(self):
		password = pymsgbox.prompt("Please enter the database password: ")
		conn = psycopg2.connect(host="localhost",database="arnold",user="postgres",password=password)
		curs = conn.cursor()
		insertFirstName = self.ui.lineEdit.text()
		insertLastName = self.ui.lineEdit_2.text()
		query = """
			INSERT INTO players 
			(first_name, last_name) 
			VALUES ('%s', '%s')
		""" % (insertFirstName, insertLastName)
		curs.execute(query)
		conn.commit()
		conn.close()

		self.ui.label.setText("User Created, please add.")
		self.ui.lineEdit.setText("")
		self.ui.lineEdit_2.setText("")


if __name__=="__main__":
	app = QApplication(sys.argv)
	w = MyForm()
	w.show()
	sys.exit(app.exec_())