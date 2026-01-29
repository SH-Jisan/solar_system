import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Sphere
r = 3
theta = np.linspace(0, np.pi, 40)
phi = np.linspace(0, 2*np.pi, 40)
theta, phi = np.meshgrid(theta, phi)

x = r * np.sin(theta) * np.cos(phi)
y = r * np.sin(theta) * np.sin(phi)
z = r * np.cos(theta)

# Figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)
ax.set_zlim(-5,5)

# Rotation function (Z-axis)
def rotate_z(x, y, z, angle):
    x_new = x * np.cos(angle) - y * np.sin(angle)
    y_new = x * np.sin(angle) + y * np.cos(angle)
    return x_new, y_new, z

# Update function
def update(frame):
    ax.cla()
    angle = np.radians(frame)
    xr, yr, zr = rotate_z(x, y, z, angle)
    ax.plot_surface(xr, yr, zr, color='cyan')
    ax.set_xlim(-5,5)
    ax.set_ylim(-5,5)
    ax.set_zlim(-5,5)
    ax.set_title("Rotating 3D Ball (like Earth)")

ani = FuncAnimation(fig, update, frames=360, interval=50)
plt.show()
