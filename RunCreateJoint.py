import maya.cmds as cmds


def get_pivot_pos(handle):

    try:

        pos = cmds.xform(handle, query=True, rotatePivot=True, worldSpace=True)
        return pos
    except:
        return [0.0, 0.0, 0.0]


def get_cluster_position(cluster_handle):

    conns = cmds.listConnections(cluster_handle + '.matrix', s=True, d=False, type='cluster')
    if not conns:
        cmds.warning(f"Cannot find cluster node for {cluster_handle}. Using handle's pivot position as fallback.")
        return get_pivot_pos(cluster_handle)
    cluster_node = conns[0]


    geo = cmds.listConnections(cluster_node + '.inputGeometry', s=True, d=False)
    if not geo:
        cmds.warning(f"Cannot find geometry for cluster {cluster_node}. Using handle's pivot position as fallback.")
        return get_pivot_pos(cluster_handle)
    geo = geo[0]


    try:

        sel = om.MSelectionList()
        sel.add(geo)
        dagPath = sel.getDagPath(0)
        fnMesh = om.MFnMesh(dagPath)

        sel2 = om.MSelectionList()
        sel2.add(cluster_node)
        clusterObj = sel2.getDependNode(0)
        fnCluster = om.MFnDependencyNode(clusterObj)

        weightsPlug = fnCluster.findPlug('weightList', False)
        vtx_indices = []
        for i in range(weightsPlug.numElements()):
            weightElem = weightsPlug.elementByPhysicalIndex(i)
            wPlug = weightElem.child(0)
            if wPlug.asFloat() > 0.0001:
                vtx_indices.append(weightElem.logicalIndex())


        if not vtx_indices:
            cmds.warning(f"Cluster {cluster_node} has no weighted vertices. Using handle's pivot position as fallback.")
            return get_pivot_pos(cluster_handle)

        vtx_positions = [fnMesh.getPoint(v, om.MSpace.kWorld) for v in vtx_indices]


        avg = om.MVector(0, 0, 0)
        for v in vtx_positions:
            avg += om.MVector(v.x, v.y, v.z)
        avg /= len(vtx_positions)

        return [avg.x, avg.y, avg.z]
        
    except Exception as e:
        cmds.warning(f"Error during API Centroid calculation: {e}. Using handle's pivot position as fallback.")
        return get_pivot_pos(cluster_handle)


def get_generic_position(selection_item):

    if '.' in selection_item:
        try:

            pos_list = cmds.xform(selection_item, query=True, translation=True, worldSpace=True)
            
            if not pos_list:
                cmds.warning(f"Could not get position for selected component(s): {selection_item}")
                return [0.0, 0.0, 0.0]
                

            x_sum, y_sum, z_sum, count = 0, 0, 0, 0
            for i in range(0, len(pos_list), 3):
                x_sum += pos_list[i]
                y_sum += pos_list[i+1]
                z_sum += pos_list[i+2]
                count += 1
            
            if count > 0:
                return [x_sum / count, y_sum / count, z_sum / count]
            
        except Exception as e:
            cmds.warning(f"Error calculating centroid for components {selection_item}: {e}")
            return [0.0, 0.0, 0.0]
    

    else:
        try:

            bbox = cmds.exactWorldBoundingBox(selection_item)

            center_x = (bbox[0] + bbox[3]) / 2.0
            center_y = (bbox[1] + bbox[4]) / 2.0
            center_z = (bbox[2] + bbox[5]) / 2.0
            return [center_x, center_y, center_z]
            
        except Exception as e:
            cmds.warning(f"Error calculating bounding box center for object {selection_item}: {e}")
            return [0.0, 0.0, 0.0]
            
    return [0.0, 0.0, 0.0]



def RunCreateJointOnCluster(num=5, radius=1.0):

    sels = cmds.ls(sl=True, flatten=True) 
    
    if len(sels) < 2:
        cmds.warning("Please select 2 items (Clusters, Vertices, or Objects).")
        return

    def get_final_position(selection_item):

        is_cluster_handle = False
        if cmds.objExists(selection_item):

            cluster_test = cmds.listConnections(selection_item, type='cluster', d=True)
            if cluster_test:
                is_cluster_handle = True

        if is_cluster_handle:

            return get_cluster_position(selection_item)
        else:

            return get_generic_position(selection_item)
    posA = get_final_position(sels[0])
    posB = get_final_position(sels[1])
    

    if (posA == [0.0, 0.0, 0.0] and posB == [0.0, 0.0, 0.0]):
        cmds.error("Failed to determine valid positions for both selections. Joint creation aborted.")
        return
    

    joint_list = []
    cmds.select(clear=True) 
    
    for i in range(num):
        t = i / float(num - 1) if num > 1 else 0
        pos = [
            posA[0] + (posB[0] - posA[0]) * t,
            posA[1] + (posB[1] - posA[1]) * t,
            posA[2] + (posB[2] - posA[2]) * t,
        ]
        
        j = cmds.joint(p=pos, rad=radius) 
        joint_list.append(j)

    cmds.select(joint_list)
    cmds.inViewMessage(amg=f"<hl>Created {num} joints along selection</hl>", pos='midCenter', fade=True)
    return joint_list