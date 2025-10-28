import maya.cmds as cmds


def ToggleMiscellaneousMode(self):

    global _original_select_masks
    state = self.MScheckBox.isChecked()

    if state:
        sel = cmds.ls(sl=True, type="joint")
        if not sel:
            QtWidgets.QMessageBox.warning(
                self, "No Selection",
                "Please select at least one joint before enabling LRA edit mode."
            )
            self.MScheckBox.setChecked(False)
            return

        _original_select_masks = {
            'allObjects': cmds.selectType(query=True, allObjects=True),
            'allComponents': cmds.selectType(query=True, allComponents=True),
            'joint': cmds.selectType(query=True, joint=True),
            'cluster': cmds.selectType(query=True, cluster=True),
        }


        for jnt in sel:
            if cmds.objExists(f"{jnt}.displayLocalAxis"):
                cmds.setAttr(f"{jnt}.displayLocalAxis", True)
 
        cmds.selectMode(component=True)
        
        cmds.selectType(allObjects=False, allComponents=False)

        cmds.selectType(joint=True, lra=True)
        
        cmds.setToolTo('RotateSuperContext') 

        cmds.select(sel, replace=True)


        cmds.inViewMessage(
            amg='<hl>LRA Edit Mode ON:</hl> Rotate Gizmo to adjust Local Rotation Axis',
            pos='midCenter',
            fade=True
        )

    else:
        # ปิดโหมด LRA
        
        # 1. ปิดการแสดงแกน LRA 
        sel = cmds.ls(sl=True, type="joint") or cmds.ls(type="joint") 
        for jnt in sel:
            if cmds.objExists(f"{jnt}.displayLocalAxis"):
                cmds.setAttr(f"{jnt}.displayLocalAxis", False)
        
        cmds.selectType(lra=False) 
        
        cmds.selectType(allObjects=False, allComponents=False, **_original_select_masks)
        
        cmds.setToolTo('selectSuperContext') 

        cmds.selectMode(object=True)
               
        cmds.inViewMessage(
            amg='<hl>LRA Edit Mode OFF:</hl> Returned to Select Tool',
            pos='midCenter',
            fade=True
        )