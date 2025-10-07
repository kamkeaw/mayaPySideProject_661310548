try:
	from PySide6 import QtCore, QtGui, QtWidgets
	from shiboken6 import wrapInstance
except:
	from PySide2 import QtCore, QtGui, QtWidgets
	from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui
import os
import importlib
from . import Util as UT
importlib.reload(UT)

ROOT_RESOURCE_DIR = 'C:/Users/SIPHAT/OneDrive/เอกสาร/maya/2024/scripts/mayaPySideProject_661310548/Image'

class JointWindowDialog(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		

		self.resize(400,700)
		self.setWindowTitle('Joint Window')

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)
		self.setStyleSheet('background-color: qLineargradient(x1:0,y1:0,x2:1, stop:0 black, stop:1 #303030);')

		self.imageLabel = QtWidgets.QLabel()
		self.imagePixmap = QtGui.QPixmap(f"{ROOT_RESOURCE_DIR}/resource/Image_Window.jpg")
		scaled_pixmap = self.imagePixmap.scaled(
				QtCore.QSize(375,200),
				QtCore.Qt.KeepAspectRatio,
				QtCore.Qt.SmoothTransformation
		)

		self.imageLabel.setPixmap(scaled_pixmap)
		self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)

		self.mainLayout.addWidget(self.imageLabel)


		self.tab_Widgets = QtWidgets.QTabWidget()
		self.mainLayout.addWidget(self.tab_Widgets)
		self.add_tabs()

	def add_tabs(self):
		self.create_tab = QtWidgets.QWidget()
		self.create_layout = QtWidgets.QVBoxLayout(self.create_tab)

		self.create_button_layout = QtWidgets.QHBoxLayout()
		self.createButton = QtWidgets.QPushButton('CreateJoint')
		self.createButton.setFixedWidth(70)	
		self.createButton.setFixedHeight(60)		
		self.InsertButton = QtWidgets.QPushButton('InsertJoint')
		self.InsertButton.setFixedWidth(70)
		self.InsertButton.setFixedHeight(60)
		self.MirrorButton = QtWidgets.QPushButton('MirrorJoint')
		self.MirrorButton.setFixedWidth(70)
		self.MirrorButton.setFixedHeight(60)
		self.OrientButton = QtWidgets.QPushButton('OrientJoint')
		self.OrientButton.setFixedWidth(70)
		self.OrientButton.setFixedHeight(60)

		self.create_button_layout.addWidget(self.createButton)
		self.create_button_layout.addWidget(self.InsertButton)
		self.create_button_layout.addWidget(self.MirrorButton)
		self.create_button_layout.addWidget(self.OrientButton)

		#######################################################
		self.nameLayout = QtWidgets.QHBoxLayout()
		self.nameLabel = QtWidgets.QLabel('DefaultRadius:')

		self.nameLineEdit = QtWidgets.QLineEdit()
		self.nameLayout.addWidget(self.nameLabel)
		self.nameLayout.addWidget(self.nameLineEdit)

		#########################################################
		self.ClusterLayout = QtWidgets.QHBoxLayout()
		self.ClusterButton = QtWidgets.QPushButton('ClusterJoint')
		self.ClusterButton.setFixedWidth(50)
		self.ClusterButton.setFixedHeight(50)
		self.nameLineEdit = QtWidgets.QLineEdit()
		self.ClusterLayout.addWidget(self.ClusterButton)
		self.ClusterLayout.addWidget(self.nameLineEdit)
		############################################################
		self.tool_button_layout = QtWidgets.QHBoxLayout()
		self.HierarchyButton = QtWidgets.QPushButton('HierarchyJoint')
		self.HierarchyButton.setFixedWidth(70)	
		self.HierarchyButton.setFixedHeight(60)		
		self.ParentButton = QtWidgets.QPushButton('ParentJoint')
		self.ParentButton.setFixedWidth(70)
		self.ParentButton.setFixedHeight(60)
		self.ConstaintButton = QtWidgets.QPushButton('ConstaintJoint')
		self.ConstaintButton.setFixedWidth(70)
		self.ConstaintButton.setFixedHeight(60)
	
		self.tool_button_layout.addWidget(self.HierarchyButton)
		self.tool_button_layout.addWidget(self.ParentButton)
		self.tool_button_layout.addWidget(self.ConstaintButton)
		##############################################################
		self.RadiusLayout = QtWidgets.QHBoxLayout()
		self.nameLabel = QtWidgets.QLabel('Radius:')


		self.nameLineEdit = QtWidgets.QLineEdit()
		self.RadiusLayout.addWidget(self.nameLabel)
		self.RadiusLayout.addWidget(self.nameLineEdit)
		##############################################################
		self.component_button_layout = QtWidgets.QHBoxLayout()
		self.componentButton = QtWidgets.QPushButton('component [F8]')
		self.MiscellaneousLabel = QtWidgets.QLabel('Miscellaneous')
		self.component_button_layout.addWidget(self.componentButton)
		self.component_button_layout.addWidget(self.MiscellaneousLabel)
		#############################################################
		self.LRALayout = QtWidgets.QHBoxLayout()
		self.LRALabel = QtWidgets.QLabel('Location Rotation Axes')
		self.LRAOffButton = QtWidgets.QPushButton('ON')
		self.LRAOffButton.setFixedWidth(70)	
		self.LRAOffButton.setFixedHeight(30)
		self.LRAOnButton = QtWidgets.QPushButton('OFF')
		self.LRAOnButton.setFixedWidth(70)	
		self.LRAOnButton.setFixedHeight(30)

		self.LRALayout.addWidget(self.LRALabel)
		self.LRALayout.addWidget(self.LRAOffButton)
		self.LRALayout.addWidget(self.LRAOnButton)


		self.create_layout.addLayout(self.create_button_layout)
		self.create_layout.addLayout(self.nameLayout)
		self.create_layout.addLayout(self.ClusterLayout)
		self.create_layout.addLayout(self.tool_button_layout)
		self.create_layout.addLayout(self.RadiusLayout)
		self.create_layout.addLayout(self.component_button_layout)
		self.create_layout.addLayout(self.LRALayout)

		self.create_layout.addStretch()



		self.tool_tab = QtWidgets.QWidget()
		self.tool_layout = QtWidgets.QVBoxLayout(self.tool_tab)
		self.tool_layout.addWidget(QtWidgets.QLabel("Tool settings content here"))

		self.tab_Widgets.addTab(self.create_tab, "Create Joint")
		self.tab_Widgets.addTab(self.tool_tab, "Calculate")




def run():
	global ui

	try:
		ui.close()
	except:
		pass
	ptr = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
	ui = JointWindowDialog(parent=ptr)
	ui.show()

