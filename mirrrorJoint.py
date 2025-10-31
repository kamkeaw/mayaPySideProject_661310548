try:
	from PySide6 import QtWidgets
except ImportError:
	try:
		from PySide2 import QtWidgets
	except ImportError:
		pass 
		
import maya.cmds as cmds


def run_mirror_joint_options(self):
		"""
		แสดงกล่องข้อความให้ผู้ใช้เลือก Mirror Plane (ซ้าย/ขวา หรือ หน้า/หลัง) 
		แล้วทำการ Mirror Joint ที่เลือก
		"""
		
		sel = cmds.ls(sl=True, type="joint")
		if not sel:
			QtWidgets.QMessageBox.warning(self, "No Selection", "Please select a joint to mirror.")
			return

		# 1. สร้างกล่องข้อความสำหรับเลือก Mirror Plane
		msg = QtWidgets.QMessageBox()
		msg.setWindowTitle("Mirror Plane Selection")
		msg.setText("Select the Mirror Plane:")
		msg.setIcon(QtWidgets.QMessageBox.Question)
		
		# กำหนดปุ่มสำหรับตัวเลือก
		side_to_side = msg.addButton("Side-to-Side (YZ Plane)", QtWidgets.QMessageBox.ActionRole)
		front_to_back = msg.addButton("Front-to-Back (XY Plane)", QtWidgets.QMessageBox.ActionRole)
		msg.setStandardButtons(QtWidgets.QMessageBox.Cancel)

		msg.exec_()
		
		# 2. ตรวจสอบการเลือกของผู้ใช้
		clicked_button = msg.clickedButton()
		mirror_plane_flag = None
		plane_name = ""
		search_replace = None

		if clicked_button == side_to_side:
########################Mirror ซ้าย-ขวา ##################################################
			mirror_plane_flag = 'mirrorYZ'
			plane_name = "Side-to-Side (YZ Plane)"
			search_replace = ('_L', '_R') 
		elif clicked_button == front_to_back:
########################Mirror ซ้าย-ขวา ##################################################
			mirror_plane_flag = 'mirrorXY'
			plane_name = "Front-to-Back (XY Plane)"
			search_replace = ('_Front', '_Back')
		else:
			# ผู้ใช้ยกเลิก
			return

		# 3. ทำการ Mirror
		try:
			kwargs = {
				mirror_plane_flag: True,
				'mirrorBehavior': True, 
				'searchReplace': search_replace
			}

			# ทำการ Mirror Joint ที่ถูกเลือกตัวแรก
			cmds.mirrorJoint(sel[0], **kwargs) 
			
			QtWidgets.QMessageBox.information(self, "Success", f"Mirror Joint successful using: {plane_name}")
			
		except Exception as e:
			QtWidgets.QMessageBox.critical(self, "Error", f"Mirror Joint Failed:\n{e}")