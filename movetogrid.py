import maya.cmds as cmds

objects = cmds.ls(selection=True)

for object in objects:
    # Get the polygonal faces of the object
    faces = cmds.ls(object, type="mesh", dag=True, shapes=True)[0] + ".f[*]"
    
    # Get the center point of the polygonal faces
    centers = cmds.xform(faces, q=True, t=True, ws=True)
    
    # Find the polygonal face closest to the floor
    min_y = float("inf")
    
    for i in range(0, len(centers), 3):
        y = centers[i + 1]
        if y < min_y:
            min_y = y
    
    # Calculate the distance between the polygonal face and the floor
    distance = abs(min_y)
    
    # Move the object above or below the floor, depending on its position
    if min_y > 0:
        # Move the object down by the distance
        cmds.move(0, -distance, 0, object, relative=True)
    else:
        # Move the object up by the distance
        cmds.move(0, distance, 0, object, relative=True)
        

