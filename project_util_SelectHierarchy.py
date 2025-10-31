import maya.cmds as cmds

def select_hierarchy():
	try:
		sel = cmds.ls(sl=True)
		if not sel:
			QtWidgets.QMessageBox.warning(None, "No Selection", "Please select a root joint or object first.")
			return


		cmds.select(sel, hi=True)


		cmds.inViewMessage(amg='<hl>Hierarchy selected.</hl>', pos='midCenter', fade=True)
	except Exception as e:
		QtWidgets.QMessageBox.warning(None, "Error", f"Cannot select hierarchy:\n{e}")
