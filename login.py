from PyQt5 import QtCore, QtGui, QtWidgets
from login_ui import Ui_MainWindow

class Login_Window(Ui_MainWindow):
	def __init__(self, w):
		Ui_MainWindow.__init__(self)
		self.setupUi(w)

if __name__ == '__main__':
	import sys
	app = QtWidgets.QApplication(sys.argv)
	w  =QtWidgets.QMainWindow()
	ui = Login_Window(w)
	w.show()
	sys.exit(app.exec_())
