import sys, psycopg2
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem
import pymsgbox
from allTeamsUI import *
class MyForm(QDialog):
	def __init__(self):
		super().__init__()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		password = pymsgbox.prompt("Please enter the database password: ")
		conn = psycopg2.connect(host="localhost",database="arnold",user="postgres",password=password)
		curs = conn.cursor()
		query = """
			SELECT 
				t.team_name,
				p1.first_name AS first_name1, 
				p1.last_name AS last_name1,
				p2.first_name AS first_name2,
				p2.last_name AS last_name2
			FROM team t
			INNER JOIN players p1
				ON t.player1_id = p1.player_id
			INNER JOIN players p2
				ON t.player2_id = p2.player_id
		""" 
		curs.execute(query)
		players = curs.fetchall()
		self.ui.tableWidgetName.setRowCount(len(players))
		self.ui.tableWidgetName.setColumnCount(5)
		
		row = 0
		for item in players:
			team_name = QTableWidgetItem(item[0])
			first_name1 = QTableWidgetItem(item[1])
			last_name1 = QTableWidgetItem(item[2])
			first_name2 = QTableWidgetItem(item[3])
			last_name2 = QTableWidgetItem(item[4])
			self.ui.tableWidgetName.setItem(row, 0, team_name)
			self.ui.tableWidgetName.setItem(row, 1, first_name1)
			self.ui.tableWidgetName.setItem(row, 2, last_name1)
			self.ui.tableWidgetName.setItem(row, 3, first_name2)
			self.ui.tableWidgetName.setItem(row, 4, last_name2)
			row += 1

		self.show()

if __name__=="__main__":
	app = QApplication(sys.argv)
	w = MyForm()
	w.show()
	sys.exit(app.exec_())