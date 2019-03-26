import sys, psycopg2
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem
from allPlayerUI import *
class MyForm(QDialog):
	def __init__(self):
		super().__init__()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		conn = psycopg2.connect(host="localhost",database="arnold",user="postgres",password="snowlep")
		curs = conn.cursor()
		query = """
			SELECT first_name, last_name
			FROM players
		""" 
		curs.execute(query)
		players = curs.fetchall()
		self.ui.tableWidgetName.setRowCount(len(players))
		
		row = 0
		for item in players:
			first_name = QTableWidgetItem(item[0])
			last_name = QTableWidgetItem(item[1])
			self.ui.tableWidgetName.setItem(row, 0, first_name)
			self.ui.tableWidgetName.setItem(row, 1, last_name)
			row += 1

		self.show()

if __name__=="__main__":
	app = QApplication(sys.argv)
	w = MyForm()
	w.show()
	sys.exit(app.exec_())