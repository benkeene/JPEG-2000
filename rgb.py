import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

step = 15
r, g, b = np.meshgrid(np.arange(0, 256, step), np.arange(0, 256, step), np.arange(0, 256, step))

r = r.flatten()
g = g.flatten()
b = b.flatten()

colors = np.stack([r, g, b], axis=1) / 255  # Normalize to [0, 1]

scatter = ax.scatter(r, g, b, c=colors, marker='o')

ax.set_xlabel('Red Channel')
ax.set_ylabel('Green Channel')
ax.set_zlabel('Blue Channel')
ax.set_title('RGB Color Space')
ax.grid(False)

def update(frame):
    ax.view_init(elev=20., azim=frame)
    return scatter,

ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 1), interval=50)
ani.save('rgb_animation.gif', writer=PillowWriter(fps=30))
plt.show()