def clusterToVertex(clusterHandle):
	import maya.cmds as cmds


	history = cmds.listHistory(clusterHandle) or []


	clusterDeformers = cmds.ls(history, type='cluster')
	if not clusterDeformers:
		cmds.warning(f"No cluster deformer found for {clusterHandle}")
		return []

	clusterDeformer = clusterDeformers[0]  


	verts = cmds.percent(clusterDeformer, q=True, v=True)
	if not verts:
		cmds.warning(f"No vertices found for {clusterDeformer}")
		return []


	positions = [cmds.xform(v, q=True, t=True, ws=True) for v in verts]
	return positions
