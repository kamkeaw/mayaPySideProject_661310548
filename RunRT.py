import maya.cmds as cmds

def RunRotateAxes(self):

    sel = cmds.ls(sl=True)
    if not sel:
        QtWidgets.QMessageBox.warning(None, "No Selection", "Please select at least one joint.")
        return

    joints = cmds.ls(sel, type="joint")
    if not joints:

        parents = []
        for s in sel:
            p = cmds.listRelatives(s, parent=True, type="joint")
            if p:
                parents.extend(p)
        joints = list(set(parents))


    if not joints:
        QtWidgets.QMessageBox.warning(None, "No Selection", "Please select at least one joint or its LRA handle.")
        return


    axes = []
    if self.RTcheckBoxX.isChecked(): axes.append("X")
    if self.RTcheckBoxY.isChecked(): axes.append("Y")
    if self.RTcheckBoxZ.isChecked(): axes.append("Z")

    if not axes:
        QtWidgets.QMessageBox.warning(None, "No Axis", "Please select one LRA axis (X, Y, or Z).")
        return


    deg_sum = 0
    if self.RTcheckBox90.isChecked(): deg_sum += 90
    if self.RTcheckBox180.isChecked(): deg_sum += 180
    if hasattr(self, "RTcheckBox270") and self.RTcheckBox270.isChecked(): deg_sum += 270

    if deg_sum == 0:
        QtWidgets.QMessageBox.warning(None, "No Angle", "Please select at least one rotation degree.")
        return


    for jnt in joints:
        for axis in axes:
            attr = f"{jnt}.jointOrient{axis}"
            if cmds.objExists(attr):
                current = cmds.getAttr(attr)
                cmds.setAttr(attr, current + deg_sum)

    cmds.inViewMessage(amg=f"<hl>Rotated LRA:</hl> {axes} {deg_sum}°", pos='midCenter', fade=True)
