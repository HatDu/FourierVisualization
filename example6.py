import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
def update_points(num):
    '''
    更新数据点
    '''
    point_ani.set_data(z[:num], y[:num])
    point_p.set_data(z[num], y[num])
    arrow_p.set_data([0, z[num]], [0, y[num]])
    return point_ani, point_p, arrow_p

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
z = np.cos(x)

fig = plt.figure(tight_layout=False)
plt.plot(z,y)
point_ani, = plt.plot(z[:0], y[:0])
point_p, = plt.plot(z[0], y[0], "ro")
arrow_p,  = plt.plot([0, 1], [0, 0])
plt.grid(ls="--")
# 开始制作动画
ani = animation.FuncAnimation(fig, update_points, np.arange(0, 100), interval=10, blit=True)

# ani.save('sin_test2.gif', writer='imagemagick', fps=10)
plt.show()