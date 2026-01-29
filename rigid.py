import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Cube vertices
cube = np.array([
    [0,0,0,1],
    [1,0,0,1],
    [1,1,0,1],
    [0,1,0,1],
    [0,0,1,1],
    [1,0,1,1],
    [1,1,1,1],
    [0,1,1,1]
])

# Shear factors
shy = 1.0   # shear in y based on x
shz = 0.5   # shear in z based on x

# Shear along Y-Z plane matrix
Shear_yz = np.array([
    [1,   0,   0,   0],
    [shy, 1,   0,   0],
    [shz, 0,   1,   0],
    [0,   0,   0,   1]
])

# Apply shear
sheared_cube = (Shear_yz @ cube.T).T

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(cube[:,0], cube[:,1], cube[:,2], c='b', label='Original')
ax.scatter(sheared_cube[:,0], sheared_cube[:,1], sheared_cube[:,2], c='r', label='Sheared')

# Draw edges
edges = [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)]
for i,j in edges:
    ax.plot([cube[i,0], cube[j,0]],[cube[i,1], cube[j,1]],[cube[i,2], cube[j,2]],'b')
    ax.plot([sheared_cube[i,0], sheared_cube[j,0]],[sheared_cube[i,1], sheared_cube[j,1]],[sheared_cube[i,2], sheared_cube[j,2]],'r')

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()
plt.title("3D Shear along Y-Z plane")
plt.show()
