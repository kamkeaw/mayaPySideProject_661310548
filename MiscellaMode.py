import maya.cmds as cmds
import maya.mel as mel

def RunMiscella2(self):
	in_component = cmds.selectMode(q=True, component=True)

	if self.MScheckBox.isChecked():
		if not in_component:
			cmds.selectMode(component=True)
			cmds.selectType(joint=True)
		mel.eval('setComponentPickMask "Other" true;')
		mel.eval('updateObjectSelectionMasks;')
		mel.eval('updateComponentSelectionMasks;')
		mel.eval('dR_selTypeChanged("");')
		cmds.inViewMessage(amg='<hl>Miscella Mode:</hl> Enabled', pos='midCenter', fade=True)
		print("✅ Miscella Mode ON")
	else:
		mel.eval('setComponentPickMask "Other" false;')
		mel.eval('updateObjectSelectionMasks;')
		mel.eval('updateComponentSelectionMasks;')
		mel.eval('dR_selTypeChanged("");')

		cmds.inViewMessage(amg='<hl>Miscella Mode:</hl> Disabled', pos='midCenter', fade=True)
		print("❎ Miscella Mode OFF")


	cmds.refresh(f=True)
