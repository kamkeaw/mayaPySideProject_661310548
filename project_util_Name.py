import maya.cmds as cmds

def renameSelection(name, prefix, suffix):
	print('NAME :', name)
	print('PREFIX :', prefix)
	print('SUFFIX :', suffix)

	sels = cmds.ls(sl=True)
	if not sels: 
		return

	for i in range(len(sels)):
		newname = prefix +'_'+ name +'_'+ suffix
		cmds.rename(newname)