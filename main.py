try:
	from PySide6 import QtCore, QtGui, QtWidgets
	from shiboken6 import wrapInstance
except:
	from PySide2 import QtCore, QtGui, QtWidgets
	from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui
import os
import importlib
import maya.mel as mel
from . import Util as UT
importlib.reload(UT)
import maya.cmds as cmds
from . import Util as Jutil
importlib.reload(Jutil)
from . import OrientJoint as OJoint
importlib.reload(OJoint)
from . import MiscellaMode as MSMode
importlib.reload(MSMode)
from . import SelectHierarchy as SelectH
importlib.reload(SelectH)
from . import RunRT as RunRotate
importlib.reload(RunRotate)
from . import RunCreateJoint as RunCJ
importlib.reload(RunCJ)
from . import ClustertoVertex as CTVertex
importlib.reload(CTVertex)
from . import mirrrorJoint as mirrorJ
importlib.reload(mirrorJ)

ROOT_RESOURCE_DIR = 'C:/Users/SIPHAT/OneDrive/เอกสาร/maya/2024/scripts/mayaPySideProject_661310548/Image'

class JointWindowDialog(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		

		self.resize(400,700)
		self.setWindowTitle('Joint Window')

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)
		self.setStyleSheet('background-color: qLineargradient(x0:0,y0:0,x2:1, stop:0 #1D1E36, stop:1 #1D1E36);')

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
		self.createButton = QtWidgets.QPushButton()
		self.createButton = QtWidgets.QToolButton()
		self.createButton.setText("CreateJoint")
		pixmap = QtGui.QPixmap(f"{ROOT_RESOURCE_DIR}/resource/Icon/CreateJoint.png")
		scaled_pixmap = pixmap.scaled(QtCore.QSize(64, 64), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
		self.createButton.setIcon(QtGui.QIcon(scaled_pixmap))

		self.createButton.setIconSize(QtCore.QSize(64, 64))
		self.createButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
		self.createButton.setFixedSize(80, 90)

		self.createButton.setStyleSheet("""
			QToolButton {
				background-color: #1B2842;
				color: white;
				font-weight: bold;
				border-radius: 15px;
				border: 2px solid #1B84C4;
				padding: 5px;
			}
			QToolButton:hover {
				background-color: #2A3F70;
			}
			QToolButton:pressed {
				background-color: #3D569C;
			}
		""")

		self.createButton.clicked.connect(self.create_joint_with_radius)


		self.InsertButton = QtWidgets.QToolButton()
		self.InsertButton.setText("InsertJoint")
		pixmap = QtGui.QPixmap(f"{ROOT_RESOURCE_DIR}/resource/Icon/InsertJoint.png")
		scaled_pixmap = pixmap.scaled(QtCore.QSize(64, 64), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
		self.InsertButton.setIcon(QtGui.QIcon(scaled_pixmap))

		self.InsertButton.setIconSize(QtCore.QSize(64, 64))
		self.InsertButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
		self.InsertButton.setFixedSize(80, 90)

		self.InsertButton.setStyleSheet("""
			QToolButton {
				background-color: #1B2842;
				color: white;
				font-weight: bold;
				border-radius: 15px;
				border: 2px solid #1B84C4;
				padding: 5px;
			}
			QToolButton:hover {
				background-color: #2A3F70;
			}
			QToolButton:pressed {
				background-color: #3D569C;
			}
		""")
		self.InsertButton.clicked.connect(self.insert_joint_with_radius)
		self.MirrorButton = QtWidgets.QToolButton()
		self.MirrorButton.setText("MirrorJoint")
		pixmap = QtGui.QPixmap(f"{ROOT_RESOURCE_DIR}/resource/Icon/MirrorJoint.png")
		scaled_pixmap = pixmap.scaled(QtCore.QSize(64, 64), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
		self.MirrorButton.setIcon(QtGui.QIcon(scaled_pixmap))

		self.MirrorButton.setIconSize(QtCore.QSize(64, 64))
		self.MirrorButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
		self.MirrorButton.setFixedSize(80, 90)

		self.MirrorButton.setStyleSheet("""
			QToolButton {
				background-color: #1B2842;
				color: white;
				font-weight: bold;
				border-radius: 15px;
				border: 2px solid #1B84C4;
				padding: 5px;
			}
			QToolButton:hover {
				background-color: #2A3F70;
			}
			QToolButton:pressed {
				background-color: #3D569C;
			}
		""")

		self.MirrorButton.clicked.connect(self.mirrorJoint)
		self.OrientButton = QtWidgets.QToolButton()
		self.OrientButton.setText("OrientJoint")	
		pixmap = QtGui.QPixmap(f"{ROOT_RESOURCE_DIR}/resource/Icon/OrientJoint.png")
		scaled_pixmap = pixmap.scaled(QtCore.QSize(64, 64), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
		self.OrientButton.setIcon(QtGui.QIcon(scaled_pixmap))

		self.OrientButton.setIconSize(QtCore.QSize(64, 64))
		self.OrientButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
		self.OrientButton.setFixedSize(80, 90)

		self.OrientButton.setStyleSheet("""
			QToolButton {
				background-color: #1B2842;
				color: white;
				font-weight: bold;
				border-radius: 15px;
				border: 2px solid #1B84C4;
				padding: 5px;
			}
			QToolButton:hover {
				background-color: #2A3F70;
			}
			QToolButton:pressed {
				background-color: #3D569C;
			}
		""")
		self.OrientButton.clicked.connect(self.RunOrient)

		self.create_button_layout.addWidget(self.createButton)
		self.create_button_layout.addWidget(self.InsertButton)
		self.create_button_layout.addWidget(self.MirrorButton)
		self.create_button_layout.addWidget(self.OrientButton)

		#######################################################
		self.nameLayout = QtWidgets.QHBoxLayout()
		self.nameLabel = QtWidgets.QLabel('DefaultRadius:')

		self.nameLineEdit = QtWidgets.QLineEdit()
		self.nameLineEdit.setFixedWidth(60)		
		self.nameLayout.addWidget(self.nameLabel)
		self.nameLayout.addWidget(self.nameLineEdit)
		self.nameLayout.addStretch()

		#########################################################
		self.ClusterLayout = QtWidgets.QHBoxLayout()
		self.ClusterButton = QtWidgets.QToolButton()
		self.ClusterButton.setText("Cluster")	
		pixmap = QtGui.QPixmap(f"{ROOT_RESOURCE_DIR}/resource/Icon/Cluster.png")
		scaled_pixmap = pixmap.scaled(QtCore.QSize(64, 64), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
		self.ClusterButton.setIcon(QtGui.QIcon(scaled_pixmap))

		self.ClusterButton.setIconSize(QtCore.QSize(64, 64))
		self.ClusterButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
		self.ClusterButton.setFixedSize(80, 90)

		self.ClusterButton.setStyleSheet("""
			QToolButton {
				background-color: #1B2842;
				color: white;
				font-weight: bold;
				border-radius: 15px;
				border: 2px solid #1B84C4;
				padding: 5px;
			}
			QToolButton:hover {
				background-color: #2A3F70;
			}
			QToolButton:pressed {
				background-color: #3D569C;
			}
		""")
		self.ClusterButton.clicked.connect(cmds.cluster)

		self.Clusterimage = QtWidgets.QLabel()  # ใช้ QLabel แทน QWidget
		pixmap = QtGui.QPixmap(f"{ROOT_RESOURCE_DIR}/resource/Image_Window_small.jpg")
		scaledC_pixmap = pixmap.scaled(
			QtCore.QSize(225, 150),
			QtCore.Qt.KeepAspectRatio,
			QtCore.Qt.SmoothTransformation
		)
		self.Clusterimage.setPixmap(scaledC_pixmap)

		self.ClusterLayout.addWidget(self.ClusterButton)
		self.ClusterLayout.addWidget(self.Clusterimage)
		self.ClusterLayout.setAlignment(QtCore.Qt.AlignCenter)

		############################################################
		self.tool_button_layout = QtWidgets.QHBoxLayout()
		self.HierarchyButton = QtWidgets.QPushButton('HierarchyJoint')
		self.HierarchyButton = QtWidgets.QToolButton()
		self.HierarchyButton.setText("Hierarchy")	
		pixmap = QtGui.QPixmap(f"{ROOT_RESOURCE_DIR}/resource/Icon/Hierachy.png")
		scaled_pixmap = pixmap.scaled(QtCore.QSize(64, 64), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
		self.HierarchyButton.setIcon(QtGui.QIcon(scaled_pixmap))

		self.HierarchyButton.setIconSize(QtCore.QSize(64, 64))
		self.HierarchyButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
		self.HierarchyButton.setFixedSize(80, 90)

		self.HierarchyButton.setStyleSheet("""
			QToolButton {
				background-color: #1B2842;
				color: white;
				font-weight: bold;
				border-radius: 15px;
				border: 2px solid #1B84C4;
				padding: 5px;
			}
			QToolButton:hover {
				background-color: #2A3F70;
			}
			QToolButton:pressed {
				background-color: #3D569C;
			}
		""")
		self.HierarchyButton.clicked.connect(self.RunSelectHierarchy)
		self.ParentButton = QtWidgets.QPushButton()
		self.ParentButton = QtWidgets.QToolButton()
		self.ParentButton.setText("Parent")	
		pixmap = QtGui.QPixmap(f"{ROOT_RESOURCE_DIR}/resource/Icon/Parent.png")
		scaled_pixmap = pixmap.scaled(QtCore.QSize(64, 64), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
		self.ParentButton.setIcon(QtGui.QIcon(scaled_pixmap))

		self.ParentButton.setIconSize(QtCore.QSize(64, 64))
		self.ParentButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
		self.ParentButton.setFixedSize(80, 90)

		self.ParentButton.setStyleSheet("""
			QToolButton {
				background-color: #1B2842;
				color: white;
				font-weight: bold;
				border-radius: 15px;
				border: 2px solid #1B84C4;
				padding: 5px;
			}
			QToolButton:hover {
				background-color: #2A3F70;
			}
			QToolButton:pressed {
				background-color: #3D569C;
			}
		""")
		self.ParentButton.clicked.connect(cmds.parent)

		self.ConstaintButton = QtWidgets.QPushButton('ConstaintJoint')
		self.ConstaintButton = QtWidgets.QToolButton()
		self.ConstaintButton.setText("Constaint")	
		pixmap = QtGui.QPixmap(f"{ROOT_RESOURCE_DIR}/resource/Icon/Constain.png")
		scaled_pixmap = pixmap.scaled(QtCore.QSize(64, 64), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
		self.ConstaintButton.setIcon(QtGui.QIcon(scaled_pixmap))

		self.ConstaintButton.setIconSize(QtCore.QSize(64, 64))
		self.ConstaintButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
		self.ConstaintButton.setFixedSize(80, 90)
		self.ConstaintButton.clicked.connect(cmds.aimConstraint)

		self.ConstaintButton.setStyleSheet("""
			QToolButton {
				background-color: #1B2842;
				color: white;
				font-weight: bold;
				border-radius: 15px;
				border: 2px solid #1B84C4;
				padding: 5px;
			}
			QToolButton:hover {
				background-color: #2A3F70;
			}
			QToolButton:pressed {
				background-color: #3D569C;
			}
		""")
	
		self.tool_button_layout.addWidget(self.HierarchyButton)
		self.tool_button_layout.addWidget(self.ParentButton)
		self.tool_button_layout.addWidget(self.ConstaintButton)
		##############################################################
		self.RadiusLayout = QtWidgets.QHBoxLayout()
		self.nameR_Label = QtWidgets.QLabel('Radius:')


		self.nameR_LineEdit = QtWidgets.QLineEdit()
		self.nameR_LineEdit.setFixedWidth(60)
		self.RunRDButton = QtWidgets.QPushButton('RUN')

		self.RunRDButton.setStyleSheet("""
			QPushButton {
				background-color: #1B2842;
				color: white;
				font-weight: bold;
				border-radius: 15px;
				border: 2px solid #1B84C4;
				padding: 5px;
			}
			QToolButton:hover {
				background-color: #2A3F70;
			}
			QToolButton:pressed {
				background-color: #3D569C;
			}
		""")
		self.RunRDButton.clicked.connect(self.RunRadius)
		self.RunRDButton.setFixedWidth(70)	
		self.RunRDButton.setFixedHeight(30)	
		self.RadiusLayout.addWidget(self.nameR_Label)
		self.RadiusLayout.addWidget(self.nameR_LineEdit)
		self.RadiusLayout.addWidget(self.RunRDButton)
		self.RadiusLayout.addStretch()
		##############################################################
		self.component_button_layout = QtWidgets.QHBoxLayout()
		self.componentButton = QtWidgets.QPushButton('component [F8]')
		self.componentButton.setStyleSheet("""
			QPushButton {
				background-color: #1B2842;
				color: white;
				font-weight: bold;
				border-radius: 15px;
				border: 2px solid #1B84C4;
				padding: 5px;
			}
			QToolButton:hover {
				background-color: #2A3F70;
			}
			QToolButton:pressed {
				background-color: #3D569C;
			}
		""")
		self.componentButton.clicked.connect(self.SelectLRAMode)
		self.MiscellaneousLabel = QtWidgets.QLabel('Miscellaneous')
		self.MScheckBox = QtWidgets.QCheckBox()

		self.MScheckBox.clicked.connect(self.CheckBoxMis)
		self.component_button_layout.addWidget(self.componentButton)
		self.component_button_layout.addWidget(self.MiscellaneousLabel)
		self.component_button_layout.addWidget(self.MScheckBox)
		self.component_button_layout.addStretch()
		#############################################################
		self.LRALayout = QtWidgets.QHBoxLayout()
		self.LRALabel = QtWidgets.QLabel('Location Rotation Axes')
		self.LRAOnButton = QtWidgets.QPushButton('ON')
		self.LRAOnButton.setStyleSheet("""
			QPushButton {
				background-color: #1B2842;
				color: white;
				font-weight: bold;
				border-radius: 15px;
				border: 2px solid #1B84C4;
				padding: 5px;
			}
			QToolButton:hover {
				background-color: #2A3F70;
			}
			QToolButton:pressed {
				background-color: #3D569C;
			}
		""")
		self.LRAOnButton.clicked.connect(self.ConnectLRA)
		self.LRAOnButton.setFixedWidth(70)	
		self.LRAOnButton.setFixedHeight(30)
		self.LRAOffButton = QtWidgets.QPushButton('OFF')
		self.LRAOffButton.setStyleSheet("""
			QPushButton {
				background-color: #1B2842;
				color: white;
				font-weight: bold;
				border-radius: 15px;
				border: 2px solid #1B84C4;
				padding: 5px;
			}
			QToolButton:hover {
				background-color: #2A3F70;
			}
			QToolButton:pressed {
				background-color: #3D569C;
			}
		""")
		self.LRAOffButton.clicked.connect(self.OffLRA)	
		self.LRAOffButton.setFixedWidth(70)	
		self.LRAOffButton.setFixedHeight(30)

		self.LRALayout.addWidget(self.LRALabel)
		self.LRALayout.addWidget(self.LRAOnButton)
		self.LRALayout.addWidget(self.LRAOffButton)
		self.LRALayout.addStretch()
		#############################################################
		self.RTLayout = QtWidgets.QVBoxLayout()
		self.RT_Top_Layout = QtWidgets.QHBoxLayout()

		self.RTLabelRT = QtWidgets.QHBoxLayout()
		self.RTLabel = QtWidgets.QLabel('Rotation Axes')
		self.RTLabel180 = QtWidgets.QLabel('180')
		self.RTLabel90 = QtWidgets.QLabel('90')
		self.RTCheckBoxRT = QtWidgets.QHBoxLayout()
		self.RTcheckBox180 = QtWidgets.QCheckBox()
		self.RTcheckBox90 = QtWidgets.QCheckBox()
		self.RTLabelRT.addWidget(self.RTLabel)
		self.RTLabelRT.addWidget(self.RTLabel180)
		self.RTLabelRT.addWidget(self.RTcheckBox180)
		self.RTLabelRT.addWidget(self.RTLabel90)
		self.RTLabelRT.addWidget(self.RTcheckBox90)
		

		self.RT_Top_Layout.addLayout(self.RTLabelRT)
		self.RT_Top_Layout.addLayout(self.RTCheckBoxRT)
		self.RT_Top_Layout.addStretch()

		self.RT_LayoutXYZ = QtWidgets.QHBoxLayout()
		self.RTLabelX = QtWidgets.QLabel('X')
		self.RTLabelY = QtWidgets.QLabel('Y')
		self.RTLabelZ = QtWidgets.QLabel('Z')
		self.RTcheckBoxX = QtWidgets.QCheckBox()
		self.RTcheckBoxY = QtWidgets.QCheckBox()
		self.RTcheckBoxZ = QtWidgets.QCheckBox()
		self.RTLButton = QtWidgets.QHBoxLayout()
		self.RTButton = QtWidgets.QPushButton('RUN')
		self.RTButton.setStyleSheet("""
			QPushButton {
				background-color: #1B2842;
				color: white;
				font-weight: bold;
				border-radius: 15px;
				border: 2px solid #1B84C4;
				padding: 5px;
			}
			QToolButton:hover {
				background-color: #2A3F70;
			}
			QToolButton:pressed {
				background-color: #3D569C;
			}
		""")
		self.RTButton.setFixedWidth(40)	
		self.RTButton.setFixedHeight(25)
		self.RTButton.clicked.connect(self.RunRotateAxes)
		self.RTLButton.addWidget(self.RTButton)



		self.RT_LayoutXYZ.addWidget(self.RTLabelX)	
		self.RT_LayoutXYZ.addWidget(self.RTcheckBoxX)
		self.RT_LayoutXYZ.addWidget(self.RTLabelY)
		self.RT_LayoutXYZ.addWidget(self.RTcheckBoxY)	
		self.RT_LayoutXYZ.addWidget(self.RTLabelZ)	
		self.RT_LayoutXYZ.addWidget(self.RTcheckBoxZ)
		self.RT_LayoutXYZ.addWidget(self.RTButton)
		self.RT_LayoutXYZ.addStretch()

	

		self.RTLayout.addLayout(self.RT_Top_Layout)
		self.RTLayout.addLayout(self.RT_LayoutXYZ)
		

		#############################################################
		self.NameAll_Layout = QtWidgets.QVBoxLayout()
		self.Name_Layout = QtWidgets.QHBoxLayout()
		self.Name_Label = QtWidgets.QLabel('Name:')
		self.Name_LineEdit = QtWidgets.QLineEdit()
		self.Name_Layout.addWidget(self.Name_Label)
		self.Name_Layout.addWidget(self.Name_LineEdit)
		self.NameP_Layout = QtWidgets.QHBoxLayout()
		self.NameP_Label = QtWidgets.QLabel('Prefix:')
		self.NameP_LineEdit = QtWidgets.QLineEdit()
		self.NameP_Layout.addWidget(self.NameP_Label)
		self.NameP_Layout.addWidget(self.NameP_LineEdit)
		self.NameS_Layout = QtWidgets.QHBoxLayout()
		self.NameS_Label = QtWidgets.QLabel('Suffix:')
		self.NameS_LineEdit = QtWidgets.QLineEdit()
		self.NameS_Layout.addWidget(self.NameS_Label)
		self.NameS_Layout.addWidget(self.NameS_LineEdit)

		self.Name_Button = QtWidgets.QHBoxLayout()
		self.NameRUN_Button = QtWidgets.QPushButton('RUN')
		self.NameRUN_Button.setStyleSheet("""
			QPushButton {
				background-color: #1B2842;
				color: white;
				font-weight: bold;
				border-radius: 15px;
				border: 2px solid #1B84C4;
				padding: 5px;
			}
			QToolButton:hover {
				background-color: #2A3F70;
			}
			QToolButton:pressed {
				background-color: #3D569C;
			}
		""")
		self.NameRUN_Button.clicked.connect(self.RenameCreateJoint)
		self.NameCLOSE_Button = QtWidgets.QPushButton('CLOSE')
		self.NameCLOSE_Button.setStyleSheet("""
			QPushButton {
				background-color: #1B2842;
				color: white;
				font-weight: bold;
				border-radius: 15px;
				border: 2px solid #1B84C4;
				padding: 5px;
			}
			QToolButton:hover {
				background-color: #2A3F70;
			}
			QToolButton:pressed {
				background-color: #3D569C;
			}
		""")
		self.NameCLOSE_Button.clicked.connect(self.close)
		self.Name_Button.addWidget(self.NameRUN_Button)
		self.Name_Button.addWidget(self.NameCLOSE_Button)
		

		self.NameAll_Layout.addLayout(self.Name_Layout)
		self.NameAll_Layout.addLayout(self.NameP_Layout)
		self.NameAll_Layout.addLayout(self.NameS_Layout)
		self.NameAll_Layout.addLayout(self.Name_Button)
		##############################################################

	
		self.frame = QtWidgets.QFrame()
		self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame.setStyleSheet('background-color: qLineargradient(x0:0,y0:0,x2:1, stop:0 #176082, stop:1 #086C99);')

		# ใส่ layout ของ NameAll ลงใน frame
		self.frameLayout = QtWidgets.QVBoxLayout(self.frame)
		self.frameLayout.addLayout(self.NameAll_Layout)


		##############################################################


		self.create_layout.addLayout(self.create_button_layout)
		self.create_layout.addLayout(self.nameLayout)
		self.create_layout.addLayout(self.ClusterLayout)
		self.create_layout.addLayout(self.tool_button_layout)
		self.create_layout.addLayout(self.RadiusLayout)
		self.create_layout.addLayout(self.component_button_layout)
		self.create_layout.addLayout(self.LRALayout)
		self.create_layout.addLayout(self.RTLayout)
		self.create_layout.addLayout(self.NameAll_Layout)
		self.create_layout.addWidget(self.frame)

		###########################################################

		self.create_layout.addStretch()

		###########################################################

		self.tool_tab = QtWidgets.QWidget()

		self.tool_layout = QtWidgets.QVBoxLayout(self.tool_tab)
		self.tool_label = QtWidgets.QLabel("Calculate The number of Joint")
		self.tool_layout.addWidget(self.tool_label)
		
		###########################################################
		self.slider_layout = QtWidgets.QHBoxLayout()
		self.slider_label = QtWidgets.QLabel("Joint:")

		###########################################################
		self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
		self.slider.setMinimum(1)
		self.slider.setMaximum(20)
		self.slider.setValue(5)
		self.slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
		self.slider.setTickInterval(1)
		self.slider.setStyleSheet(
			"""
			QSlider::groove:horizontal {
				border: 1px solid #444;
				height: 6px;
				background: white;
				margin: 2px 0;
				border-radius: 3px;
			}
			QSlider::handle:horizontal {
				background: #2A3F70;
				border: 1px solid #5c5c5c;
				width: 14px;
				height: 14px;
				margin: -4px 0; 
				border-radius: 7px;
			}
			QSlider::handle:horizontal:hover {
				background: #99FFBF;
			}
		"""
		)


		self.slider_value = QtWidgets.QSpinBox()
		self.slider_value.setRange(1, 20)
		self.slider_value.setValue(5)


		self.slider.valueChanged.connect(self.slider_value.setValue)
		self.slider_value.valueChanged.connect(self.slider.setValue)


		self.slider_layout.addWidget(self.slider_label)
		self.slider_layout.addWidget(self.slider)
		self.slider_layout.addWidget(self.slider_value)

		##########################################################
		self.RadiusLayoutS = QtWidgets.QHBoxLayout()
		self.RadiusNameS = QtWidgets.QLabel('Radius:')


		self.RDLineEdit = QtWidgets.QLineEdit()
		self.RDLineEdit.setFixedWidth(60)

		self.RadiusLayoutS.addWidget(self.RadiusNameS)
		self.RadiusLayoutS.addWidget(self.RDLineEdit)
		self.RadiusLayoutS.addStretch()	


		##########################################################
		self.Tool_Button = QtWidgets.QHBoxLayout()
		self.ToolRUN_Button = QtWidgets.QPushButton('RUN')
		self.ToolRUN_Button.setStyleSheet("""
			QPushButton {
				background-color: #1B2842;
				color: white;
				font-weight: bold;
				border-radius: 15px;
				border: 2px solid #1B84C4;
				padding: 5px;
			}
			QToolButton:hover {
				background-color: #2A3F70;
			}
			QToolButton:pressed {
				background-color: #3D569C;
			}
		""")

		self.ToolRUN_Button.clicked.connect(self.RunCalculate)
		self.ToolCLOSE_Button = QtWidgets.QPushButton('CLOSE')
		self.ToolCLOSE_Button.setStyleSheet("""
			QPushButton {
				background-color: #1B2842;
				color: white;
				font-weight: bold;
				border-radius: 15px;
				border: 2px solid #1B84C4;
				padding: 5px;
			}
			QToolButton:hover {
				background-color: #2A3F70;
			}
			QToolButton:pressed {
				background-color: #3D569C;
			}
		""")
		self.ToolCLOSE_Button.clicked.connect(self.close)
		self.Tool_Button.addWidget(self.ToolRUN_Button)
		self.Tool_Button.addWidget(self.ToolCLOSE_Button)
		
		
		###########################################################
		self.tool_layout.addLayout(self.slider_layout)
		self.tool_layout.addLayout(self.RadiusLayoutS)
		self.tool_layout.addLayout(self.Tool_Button)
		self.tool_layout.addStretch()

		self.tool_tab.setLayout(self.tool_layout)

		self.tab_Widgets.addTab(self.create_tab, "Create Joint")
		self.tab_Widgets.addTab(self.tool_tab, "Calculate")
		self.tab_Widgets.setStyleSheet("""
			QTabWidget::pane {
				border: none;
				background: #1D1E36;
			}

			QTabBar::tab {
				background: #1D1E36;
				color: white;
				padding: 6px 20px;
				border: 1px solid #1B84C4;
				border-top-left-radius: 8px;
				border-top-right-radius: 8px;
			}

			QTabBar::tab:selected {
				background: #2A3F70;
				color: #99FFBF;
			}

			QTabBar::tab:hover {
				background: #2A3F70;
			}
		""")


		#####################################################
		self.imageTabLabel = QtWidgets.QLabel()
		self.imageTabLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.imageTabLabel.setScaledContents(True)  
		self.imageTabPixmap = QtGui.QPixmap(f"{ROOT_RESOURCE_DIR}/resource/Image_Window23.jpg")
		scaledS_pixmap = self.imageTabPixmap.scaled(
				QtCore.QSize(900, 500),
				QtCore.Qt.KeepAspectRatio,
				QtCore.Qt.SmoothTransformation
		)

		self.imageTabLabel.setPixmap(scaledS_pixmap)
		self.imageTabLabel.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		self.tool_layout.addWidget(self.imageTabLabel)

		##########################################################
	def create_joint_with_radius(self):
		try:
			radius_value = float(self.nameLineEdit.text())
		except ValueError:
			QtWidgets.QMessageBox.warning(self, "Invalid Input", "Please enter a valid number for Default Radius.")
			return
		
		jnt = cmds.joint(radius=radius_value)
		cmds.select(jnt)

	def insert_joint_with_radius(self):
		try:
			radius_value = float(self.nameLineEdit.text())
		except ValueError:
			QtWidgets.QMessageBox.warning(self, "Invalid Input", "Please enter a valid number for Default Radius.")
			return

		sel = cmds.ls(sl=True, type="joint")
		if not sel:
			QtWidgets.QMessageBox.warning(self, "No Selection", "Please select a joint to insert.")
			return

		new_jnt = cmds.insertJoint(sel[0])
		cmds.setAttr(f"{new_jnt}.radius", radius_value)
		cmds.select(new_jnt)

		#####################################################

	def RenameCreateJoint(self):
		name = self.Name_LineEdit.text()
		prefix = self.NameP_LineEdit.text()
		suffix = self.NameS_LineEdit.text()
		Jutil.renameSelection(name, prefix, suffix)

		#########################################################
	def RunRadius(self):
		try:
			radius_value = float(self.nameR_LineEdit.text())
		except ValueError:
			QtWidgets.QMessageBox.warning(self, "Invalid Input", "Please enter a valid number for Radius.")
			return

		sel = cmds.ls(sl=True, type="joint")
		if not sel:
			QtWidgets.QMessageBox.warning(self, "No Selection", "Please select at least one joint to set radius.")
			return

		for jnt in sel:
			cmds.setAttr(f"{jnt}.radius", radius_value)

		cmds.inViewMessage(amg=f"<hl>Radius set to:</hl> {radius_value}", pos='midCenter', fade=True)

	
	def ConnectLRA(self):
		sel = cmds.ls(sl=True, type="joint")
		if not sel:
			QtWidgets.QMessageBox.warning(self, "No Selection", "Please select at least one joint to enable LRA.")
			return
		
		for jnt in sel:
			cmds.setAttr(f"{jnt}.displayLocalAxis", 1)

	def OffLRA(self):
		sel = cmds.ls(sl=True, type="joint")
		if not sel:
			QtWidgets.QMessageBox.warning(self, "No Selection", "Please select at least one joint to disable LRA.")
			return

		for jnt in sel:
			cmds.setAttr(f"{jnt}.displayLocalAxis", 0)

	def RunRotateAxes(self):
		RunRotate.RunRotateAxes(self)


	def SelectLRAMode(self):
		try:
			import maya.cmds as cmds
			is_component = cmds.selectMode(q=True, component=True)

			if not is_component:

				cmds.selectMode(component=True)
				cmds.selectType(joint=True)
				self.componentButton.setStyleSheet("background-color: #3BA55D; color: white; font-weight: bold;")
				cmds.inViewMessage(amg='<hl>Component Mode:</hl> Joint LRA Active', pos='midCenter', fade=True)
			else:

				cmds.selectMode(object=True)
				self.componentButton.setStyleSheet("")  # กลับเป็นสีปกติ
				cmds.inViewMessage(amg='<hl>Object Mode:</hl> Joint Selection Active', pos='midCenter', fade=True)

		except Exception as e:
			QtWidgets.QMessageBox.warning(self, "Error", f"Cannot toggle component mode:\n{e}")



	def RunOrient(self):
		sel = cmds.ls(sl=True, type="joint")
		OJoint.run_orient_joint()


	def CheckBoxMis(self):
		self.MScheckBox.isChecked()
		MSMode.RunMiscella2(self)


	def RunSelectHierarchy(self):
		SelectH.select_hierarchy()  

	####################### TAB 2 #########################	

	def RunCalculate(self):
		try:
			joint_count = self.slider_value.value()
			radius = float(self.RDLineEdit.text())
		except ValueError:
			QtWidgets.QMessageBox.warning(self, "Invalid Input", "Please enter a valid radius value.")
			return

		try:
			RunCJ.RunCreateJointOnCluster(joint_count, radius)
		except Exception as e:
			QtWidgets.QMessageBox.critical(self, "Error", f"Failed to run calculation:\n{e}")

	#########################################################

	def mirrorJoint(self):
		mirrorJ.run_mirror_joint_options(self)


def run():
	global ui

	try:
		ui.close()
	except:
		pass
	ptr = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
	ui = JointWindowDialog(parent=ptr)
	ui.show()


