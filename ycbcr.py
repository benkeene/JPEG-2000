import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

step = 15
y, cb, cr = np.meshgrid(np.arange(16, 236, step), np.arange(16, 241, step), np.arange(16, 241, step))

y = y.flatten()
cb = cb.flatten()
cr = cr.flatten()

r = y + 1.402 * (cr - 128)
g = y - 0.34414 * (cb - 128) - 0.71414 * (cr - 128)
b = y + 1.772 * (cb - 128)


r = np.clip(r, 0, 255)
g = np.clip(g, 0, 255)
b = np.clip(b, 0, 255)  

colors = np.stack([r, g, b], axis=1) / 255  # Normalize to [0, 1]
scatter = ax.scatter(y, cb, cr, c=colors, marker='o')

ax.set_xlabel('Y Channel')
ax.set_ylabel('Cb Channel')
ax.set_zlabel('Cr Channel')
ax.set_title('YCbCr Color Space')
ax.grid(False)

def update(frame):
    ax.view_init(elev=20., azim=frame)
    return scatter,

ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 1), interval=50)
ani.save('ycbcr_animation.gif', writer=PillowWriter(fps=30))
plt.show()