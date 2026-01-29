import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

class CelestialBody:
    def __init__(self, name, radius, color, orbit_radius, orbit_speed, rotation_speed):
        self.name = name
        self.radius = radius
        self.color = color
        self.orbit_radius = orbit_radius
        self.orbit_speed = orbit_speed
        self.rotation_speed = rotation_speed
        
        # Meshgrid for sphere
        self.theta = np.linspace(0, np.pi, 20)
        self.phi = np.linspace(0, 2*np.pi, 20)
        self.theta, self.phi = np.meshgrid(self.theta, self.phi)
        
        # Initial base coordinates (centered at 0,0,0)
        self.x_base = self.radius * np.sin(self.theta) * np.cos(self.phi)
        self.y_base = self.radius * np.sin(self.theta) * np.sin(self.phi)
        self.z_base = self.radius * np.cos(self.theta)
        
    def get_position(self, frame):
        # Orbit position
        orbit_angle = np.radians(frame * self.orbit_speed)
        x_orbit = self.orbit_radius * np.cos(orbit_angle)
        y_orbit = self.orbit_radius * np.sin(orbit_angle)
        z_orbit = 0
        
        # Self-rotation (simplified as rotation of the mesh points if needed, 
        # but for sphere uniformity without texture, it's hard to see. 
        # We'll just move the sphere for now. To make it distinct, let's keep it simple)
        
        return x_orbit, y_orbit, z_orbit
    
    def get_surface(self, frame):
        x_center, y_center, z_center = self.get_position(frame)
        
        # Just translate the base sphere to the orbit position
        return (self.x_base + x_center, 
                self.y_base + y_center, 
                self.z_base + z_center)

class SolarSystem:
    def __init__(self):
        self.bodies = []
        self.fig = plt.figure(figsize=(10, 10))
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.set_facecolor('black')
        self.ax.grid(False)
        self.ax.xaxis.pane.fill = False
        self.ax.yaxis.pane.fill = False
        self.ax.zaxis.pane.fill = False
        
    def add_body(self, body):
        self.bodies.append(body)
        
    def update(self, frame):
        self.ax.cla()
        # Keep axis fixed
        self.ax.set_xlim(-15, 15)
        self.ax.set_ylim(-15, 15)
        self.ax.set_zlim(-15, 15)
        self.ax.set_axis_off() # Hide axes for better look
        
        for body in self.bodies:
            X, Y, Z = body.get_surface(frame)
            self.ax.plot_surface(X, Y, Z, color=body.color, alpha=0.9)
            
        self.ax.set_title("Solar System Simulation", color='white')

    def animate(self):
        return FuncAnimation(self.fig, self.update, frames=360, interval=50)

if __name__ == "__main__":
    system = SolarSystem()
    
    # Sun
    sun = CelestialBody("Sun", radius=3, color='yellow', orbit_radius=0, orbit_speed=0, rotation_speed=0)
    system.add_body(sun)
    
    # Earth (Blue planet)
    earth = CelestialBody("Earth", radius=1, color='blue', orbit_radius=8, orbit_speed=1, rotation_speed=5)
    system.add_body(earth)
    
    # Mars (Red planet)
    mars = CelestialBody("Mars", radius=0.8, color='red', orbit_radius=12, orbit_speed=0.6, rotation_speed=4)
    system.add_body(mars)
    
    ani = system.animate()
    plt.show()
