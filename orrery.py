import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Create a figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Circle parameters
r = 1  # radius of the circle
num_points = 100  # number of points to define the circle
theta = np.linspace(0, 2 * np.pi, num_points)
circle_x = r * np.cos(theta)
circle_y = r * np.sin(theta)
circle_z = np.zeros_like(theta)  # Circle lies in the XY-plane initially

# Initial plot setup
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-1.5, 1.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Function to apply rotations to the circle and the colored spot
def rotate_circle(frame):
    # Z-axis rotation matrix
    angle_z = np.radians(frame)  # Rotate by 'frame' degrees around Z-axis
    rotation_matrix_z = np.array([
        [np.cos(angle_z), -np.sin(angle_z), 0],
        [np.sin(angle_z), np.cos(angle_z), 0],
        [0, 0, 1]
    ])

    # X-axis rotation matrix
    angle_x = np.radians(frame / 2)  # Rotate by 'frame/2' degrees around X-axis
    rotation_matrix_x = np.array([
        [1, 0, 0],
        [0, np.cos(angle_x), -np.sin(angle_x)],
        [0, np.sin(angle_x), np.cos(angle_x)]
    ])

    # Combine both rotations: First Z-rotation, then X-rotation
    rotated_points = np.vstack((circle_x, circle_y, circle_z))

    # Apply Z-axis rotation first
    rotated_points = np.dot(rotation_matrix_z, rotated_points)

    # Apply X-axis rotation second
    rotated_points = np.dot(rotation_matrix_x, rotated_points)

    # Extract the rotated coordinates
    x_rot = rotated_points[0, :]
    y_rot = rotated_points[1, :]
    z_rot = rotated_points[2, :]

    # Track the colored spot on the circle (start at (r, 0, 0) in the XY-plane)
    spot_angle = np.radians(frame)  # Same angle as the Z-axis rotation
    spot_x = r * np.cos(spot_angle)
    spot_y = r * np.sin(spot_angle)
    spot_z = 0  # The spot stays on the XY-plane

    # Clear previous plot and plot new circle and spot
    ax.cla()
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_zlim(-1.5, 1.5)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Plot the rotated circle
    ax.plot(x_rot, y_rot, z_rot, 'b-', lw=2)

    # Plot the colored spot on the circle
    ax.scatter(spot_x, spot_y, spot_z, color='r', s=100, label="Spot")  # Red spot

# Create the animation
ani = FuncAnimation(fig, rotate_circle, frames=60, interval=10)

# Show the animation
plt.show()