import maya.cmds as cmds


def run_orient_joint():
	sel = cmds.ls(sl=True, type="joint")

	if not sel:
		QtWidgets.QMessageBox.warning(None, "No Selection", "Please select at least one joint to orient.")
		return

	try:
		for jnt in sel:
			children = cmds.listRelatives(jnt, c=True, type="joint")
			if children:
				cmds.joint(jnt, e=True, orientJoint='xyz', secondaryAxisOrient='yup', children=True, zeroScaleOrient=True)
			else:
				cmds.setAttr(f"{jnt}.jointOrientX", 0)
				cmds.setAttr(f"{jnt}.jointOrientY", 0)
				cmds.setAttr(f"{jnt}.jointOrientZ", 0)

		cmds.inViewMessage(amg='<hl>Joint Orientation Completed!</hl>', pos='midCenter', fade=True)
		QtWidgets.QMessageBox.information(None, "Orient Complete", "Joint orientation applied successfully!")

	except Exception as e:
		QtWidgets.QMessageBox.warning(None, "Error", f"Cannot orient joint:\n{e}")
