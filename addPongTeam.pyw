import sys, psycopg2, pdb
from PyQt5.QtWidgets import QDialog, QApplication
from addTeamUI import *
class MyForm(QDialog):
	def __init__(self):
		super().__init__()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		conn = psycopg2.connect(host="localhost",database="arnold",user="postgres",password="snowlep")
		curs = conn.cursor()
		query = """
		SELECT CONCAT(first_name, ' ', last_name)
		FROM players
		"""
		curs.execute(query)
		names = curs.fetchall()
		for name in names:
			self.ui.comboBoxPlayer1.addItem(name[0])
			self.ui.comboBoxPlayer2.addItem(name[0])
		conn.commit()
		conn.close()
		self.ui.pushButton.clicked.connect(self.addTeam)
		self.show()
	def addTeam(self):
		conn = psycopg2.connect(host="localhost",database="arnold",user="postgres",password="snowlep")
		curs = conn.cursor()
		insert_player1 = self.ui.comboBoxPlayer1.itemText(self.ui.comboBoxPlayer1.currentIndex())
		player1_first_name = insert_player1.split()[0]
		player1_last_name = insert_player1.split()[1]
		insert_player2 = self.ui.comboBoxPlayer2.itemText(self.ui.comboBoxPlayer2.currentIndex())
		player2_first_name = insert_player2.split()[0]
		player2_last_name = insert_player2.split()[1]
		
		# get player1_id 
		query = """
		SELECT player_id
		FROM players
		WHERE first_name = '%s'
			AND last_name = '%s'
		""" % (player1_first_name, player1_last_name)
		curs.execute(query)
		player1_id = curs.fetchone()

		# get player2_id 
		query = """
		SELECT player_id
		FROM players
		WHERE first_name = '%s'
			AND last_name = '%s'
		""" % (player2_first_name, player2_last_name)
		curs.execute(query)
		player2_id = curs.fetchone()

		# get team name from form

		team_name = self.ui.lineEditTeamName.text()

		query = """
			INSERT INTO team 
			(team_name, player1_id, player2_id) 
			VALUES ('%s', '%s', '%s')
		""" % (team_name, player1_id[0], player2_id[0])
		curs.execute(query)
		conn.commit()
		conn.close()

		self.ui.label.setText("Team Created, please add.")


if __name__=="__main__":
	app = QApplication(sys.argv)
	w = MyForm()
	w.show()
	sys.exit(app.exec_())