import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
def update_points(num):
    '''
    更新数据点
    '''
    point_ani.set_data(z[num], y[num])
    return point_ani,

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
z = np.cos(x)

fig = plt.figure(tight_layout=True)
plt.plot(x-3,y)
point_ani, = plt.plot(x[0], y[0], "ro")
plt.grid(ls="--")
# 开始制作动画
ani = animation.FuncAnimation(fig, update_points, np.arange(0, 100), interval=10, blit=True)

# ani.save('sin_test2.gif', writer='imagemagick', fps=10)
plt.show()