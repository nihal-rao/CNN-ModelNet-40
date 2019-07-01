import util
import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from voxelgrid import VoxelGrid

densifyN = 5000

shape_file = "/home/mancmanomyst/vase.obj"
V,E,F_ = util.parseObj(shape_file)
F = util.removeWeirdDuplicate(F_)
Vorig,Eorig,Forig = V.copy(),E.copy(),F.copy()

# sort by length (maintain a priority queue)
Elist = list(range(len(E)))
Elist.sort(key=lambda i:util.edgeLength(V,E,i),reverse=True)

# create edge-to-triangle and triangle-to-edge lists
EtoF = [[] for j in range(len(E))]
FtoE = [[] for j in range(len(F))]
for f in range(len(F)):
	v = F[f]
	util.pushEtoFandFtoE(EtoF,FtoE,E,f,v[0],v[1])
	util.pushEtoFandFtoE(EtoF,FtoE,E,f,v[0],v[2])
	util.pushEtoFandFtoE(EtoF,FtoE,E,f,v[1],v[2])
V,E,F = list(V),list(E),list(F)

# repeat densification
for z in range(densifyN):
	util.densify(V,E,F,EtoF,FtoE,Elist)
    
densifyV = np.array(V[-densifyN:])
x=densifyV[:,0]
y=densifyV[:,1]
z=densifyV[:,2]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(z,x,y,zdir='z', c='red')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()

"""
x=densifyV[:,0]/np.max(np.absolute(densifyV[:,0]))
y=densifyV[:,1]/np.max(np.absolute(densifyV[:,1]))
z=densifyV[:,2]/np.max(np.absolute(densifyV[:,2]))

d=np.column_stack((x,y,z))
a_voxelgrid = VoxelGrid(d, x_y_z=[16, 16, 16])

h=a_voxelgrid.vector
x=h.nonzero()

a_voxelgrid = VoxelGrid(d, x_y_z=[40, 40, 40])

h=a_voxelgrid.vector
x,y,z=h.nonzero()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(z,x,y,zdir='z', c='red')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
"""



"""
xyz=np.asarray(xyz)
xy=xyz.T

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(xy)

o3d.io.write_point_cloud("sync.ply", pcd)

 # Load saved point cloud and visualize it
pcd_load = o3d.io.read_point_cloud("sync.ply")
pcd_load.paint_uniform_color([0, 0, 0])
o3d.visualization.draw_geometries([pcd_load])
#22,46,84,116
h=a_voxelgrid.vector.reshape(-1)/np.max(a_voxelgrid.vector)
np.savez("test.npz",h=h)
"""