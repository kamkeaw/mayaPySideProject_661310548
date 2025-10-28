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

ROOT_RESOURCE_DIR = 'C:/Users/SIPHAT/OneDrive/เอกสาร/maya/2024/scripts/mayaPySideProject_661310548/Image'

class JointWindowDialog(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		

		self.resize(400,700)
		self.setWindowTitle('Joint Window')

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)
		self.setStyleSheet('background-color: qLineargradient(x0:0,y0:0,x2:1, stop:0 black, stop:1 black);')

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
		self.createButton.setIcon(QtGui.QIcon(f"{ROOT_RESOURCE_DIR}/resource/Icon/CreateJoint.png"))
		self.createButton.setIconSize(QtCore.QSize(64, 64))
		self.createButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
		self.createButton.setFixedSize(80, 80)
		self.createButton.clicked.connect(self.create_joint_with_radius)

		self.InsertButton = QtWidgets.QToolButton()
		self.InsertButton.setText("InsertJoint")
		self.InsertButton.setIcon(QtGui.QIcon(f"{ROOT_RESOURCE_DIR}/resource/Icon/InsertJoint.png"))
		self.InsertButton.setIconSize(QtCore.QSize(64, 64))
		self.InsertButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
		self.InsertButton.setFixedSize(80, 80)
		self.InsertButton.clicked.connect(self.insert_joint_with_radius)

		self.MirrorButton = QtWidgets.QToolButton()
		self.MirrorButton.setText("MirrorJoint")
		self.MirrorButton.setIcon(QtGui.QIcon(f"{ROOT_RESOURCE_DIR}/resource/Icon/MirrorJoint.png"))
		self.MirrorButton.setIconSize(QtCore.QSize(64, 64))
		self.MirrorButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
		self.MirrorButton.setFixedSize(80, 80)
		self.MirrorButton.clicked.connect(cmds.mirrorJoint)



		self.OrientButton = QtWidgets.QToolButton()
		self.OrientButton.setText("OrientJoint")	
		self.OrientButton.setIcon(QtGui.QIcon(f"{ROOT_RESOURCE_DIR}/resource/Icon/OrientJoint.jpg"))
		self.OrientButton.setIconSize(QtCore.QSize(64, 64))
		self.OrientButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
		self.OrientButton.setFixedSize(80, 80)
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
		self.ClusterButton = QtWidgets.QPushButton('ClusterJoint')
		self.ClusterButton.setFixedWidth(70)
		self.ClusterButton.setFixedHeight(70)
		self.ClusterButton.clicked.connect(cmds.cluster)
		self.ClusterLayout.addWidget(self.ClusterButton)
		############################################################
		self.tool_button_layout = QtWidgets.QHBoxLayout()
		self.HierarchyButton = QtWidgets.QPushButton('HierarchyJoint')
		self.HierarchyButton.setFixedWidth(70)	
		self.HierarchyButton.setFixedHeight(60)	
		self.HierarchyButton.clicked.connect(self.RunSelectHierarchy)
		self.ParentButton = QtWidgets.QPushButton('ParentJoint')
		self.ParentButton.setFixedWidth(70)
		self.ParentButton.setFixedHeight(60)
		self.ParentButton.clicked.connect(cmds.parent)
		self.ConstaintButton = QtWidgets.QPushButton('ConstaintJoint')
		self.ConstaintButton.setFixedWidth(70)
		self.ConstaintButton.setFixedHeight(60)
	
		self.tool_button_layout.addWidget(self.HierarchyButton)
		self.tool_button_layout.addWidget(self.ParentButton)
		self.tool_button_layout.addWidget(self.ConstaintButton)
		##############################################################
		self.RadiusLayout = QtWidgets.QHBoxLayout()
		self.nameR_Label = QtWidgets.QLabel('Radius:')


		self.nameR_LineEdit = QtWidgets.QLineEdit()
		self.nameR_LineEdit.setFixedWidth(60)
		self.RunRDButton = QtWidgets.QPushButton('RUN')
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
		self.componentButton.clicked.connect(self.SelectLRAMode)
		self.MiscellaneousLabel = QtWidgets.QLabel('Miscellaneous')
		self.MScheckBox = QtWidgets.QCheckBox()
		self.MScheckBox.clicked.connect(self.RunMiscella)
		self.component_button_layout.addWidget(self.componentButton)
		self.component_button_layout.addWidget(self.MiscellaneousLabel)
		self.component_button_layout.addWidget(self.MScheckBox)
		self.component_button_layout.addStretch()
		#############################################################
		self.LRALayout = QtWidgets.QHBoxLayout()
		self.LRALabel = QtWidgets.QLabel('Location Rotation Axes')
		self.LRAOnButton = QtWidgets.QPushButton('ON')
		self.LRAOnButton.clicked.connect(self.ConnectLRA)
		self.LRAOnButton.setFixedWidth(70)	
		self.LRAOnButton.setFixedHeight(30)
		self.LRAOffButton = QtWidgets.QPushButton('OFF')
		self.LRAOffButton.clicked.connect(self.OffLRA)	
		self.LRAOffButton.setFixedWidth(70)	
		self.LRAOffButton.setFixedHeight(30)

		self.LRALayout.addWidget(self.LRALabel)
		self.LRALayout.addWidget(self.LRAOnButton)
		self.LRALayout.addWidget(self.LRAOffButton)
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
		self.NameRUN_Button.clicked.connect(self.RenameCreateJoint)
		self.NameCLOSE_Button = QtWidgets.QPushButton('CLOSE')
		self.NameCLOSE_Button.clicked.connect(self.close)
		self.Name_Button.addWidget(self.NameRUN_Button)
		self.Name_Button.addWidget(self.NameCLOSE_Button)
		

		self.NameAll_Layout.addLayout(self.Name_Layout)
		self.NameAll_Layout.addLayout(self.NameP_Layout)
		self.NameAll_Layout.addLayout(self.NameS_Layout)
		self.NameAll_Layout.addLayout(self.Name_Button)
		##############################################################

				# ===== ใส่ Frame ครอบ Layout นี้ =====
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
				background: Black;
				margin: 2px 0;
				border-radius: 3px;
			}
			QSlider::handle:horizontal {
				background: white;
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
		self.RadiusLayoutS.addWidget(self.RadiusNameS)
		self.RadiusLayoutS.addWidget(self.RDLineEdit)


		##########################################################
		self.Tool_Button = QtWidgets.QHBoxLayout()
		self.ToolRUN_Button = QtWidgets.QPushButton('RUN')
		self.ToolRUN_Button.clicked.connect(self.RunCalculate)
		self.ToolCLOSE_Button = QtWidgets.QPushButton('CLOSE')
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

		#####################################################
	def create_joint_with_radius(self):
		"""สร้าง joint พร้อม radius จากช่อง DefaultRadius"""
		try:
			radius_value = float(self.nameLineEdit.text())
		except ValueError:
			QtWidgets.QMessageBox.warning(self, "Invalid Input", "Please enter a valid number for Default Radius.")
			return
		
		jnt = cmds.joint(radius=radius_value)
		cmds.select(jnt)

	def insert_joint_with_radius(self):
		"""แทรก joint พร้อม radius จากช่อง DefaultRadius"""
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
			# ✅ ดึงค่าจากช่องป้อน Radius (ไม่ใช่ปุ่ม)
			radius_value = float(self.nameR_LineEdit.text())
		except ValueError:
			QtWidgets.QMessageBox.warning(self, "Invalid Input", "Please enter a valid number for Radius.")
			return

		sel = cmds.ls(sl=True, type="joint")
		if not sel:
			QtWidgets.QMessageBox.warning(self, "No Selection", "Please select at least one joint to set radius.")
			return

		# ✅ ตั้ง radius ให้ joint ที่เลือก
		for jnt in sel:
			cmds.setAttr(f"{jnt}.radius", radius_value)

		cmds.inViewMessage(amg=f"<hl>Radius set to:</hl> {radius_value}", pos='midCenter', fade=True)

	def convertSelectedClusterToVertex(self):
		sels = cmds.ls(sl=True)
		if not sels:
			cmds.warning("Select cluster handle(s) first")
			return
		positions = []
		for c in sels:
			pos = CTVertex.clusterToVertex(c)
			positions.append(pos)
		cmds.select(clear=True)
		for i, p in enumerate(positions):
			loc = cmds.spaceLocator()[0]
			cmds.xform(loc, t=p, ws=True)


	
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


	def RunMiscella(self):
		MSMode.ToggleMiscellaneousMode(self)



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


def run():
	global ui

	try:
		ui.close()
	except:
		pass
	ptr = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
	ui = JointWindowDialog(parent=ptr)
	ui.show()


