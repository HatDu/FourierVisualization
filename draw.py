import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpl_toolkits.axisartist as axisartist
from matplotlib.ticker import FuncFormatter

def draw_axis():
    
    #创建画布
    fig = plt.figure(figsize=(8, 8), facecolor='w')
    #使用axisartist.Subplot方法创建一个绘图区对象ax
    ax = axisartist.Subplot(fig, 111, facecolor='w')  
    fig.add_axes(ax)
    # 坐标轴设置
    ax.axis[:].set_visible(False)
    ax.axis["x"] = ax.new_floating_axis(0,0)
    ax.axis["x"].set_axisline_style("->", size = 1.0)
    
    ax.axis["y"] = ax.new_floating_axis(1,0)
    ax.axis["y"].set_axisline_style("->", size = 1.0)
    plt.xticks([])
    plt.yticks([])
    ax = plt.gca() # 获取当前的axes
    # ax.axis["x"].set_axis_direction("top")
    # ax.axis["y"].set_axis_direction("right")
    # ax.axis[:].major_ticks.set_color("r")
    
    #将绘图区对象添加到画布中
    
    
    #生成x步长为0.1的列表数据
    # x = fft.real
    # y = fft.imag
    # xmax = np.max(x)
    # xmin = np.min(x)
    # deltax = xmax - xmin
    # ymax = np.max(y)
    # ymin = np.min(y)
    # deltay = ymax - ymin

    # plt.xlim(xmin - deltax*0.2, xmax + deltax*0.2)
    # plt.ylim(ymin - deltay*0.2, ymax + deltay*0.2)
    # #绘制图形
    
    return fig
def draw_vector_circle(vectors: list):
    x = vectors.real
    y = vectors.imag
    x = np.concatenate(([0.], x))
    y = np.concatenate(([0.], y))
    for i in range(1, len(x)):
        # r = np.sqrt(x[i]**2 + y[i]**2)
        x[i] += x[i-1]
        y[i] += y[i-1]
        # circle = plt.Circle((x[i-1], y[i-1]), r, color='b', fill=False)
        # plt.gcf().gca().add_artist(circle)
    
    vector_ani, = plt.plot(x, y, "-*")
    return vector_ani

def get_fft_vectors(vectors: list):
    tmp = vectors / len(vectors)
    x = tmp.real
    y = tmp.imag
    x = np.concatenate(([0.], x))
    y = np.concatenate(([0.], y))
    for i in range(1, len(x)):
        # r = np.sqrt(x[i]**2 + y[i]**2)
        x[i] += x[i-1]
        y[i] += y[i-1]
    return x, y
    
def step(data):
    fft, n, point_ani, vector_ani, circle_anis, circles_points, trajectories_ani, trajectories = data
    N = len(fft)
    
    base = np.arange(N)*2*np.pi*n/N * complex(0, 1)
    base = np.exp(base)

    # point
    xn = np.sum(fft*base)/N
    
    # line
    rot = n*2*np.pi/N*np.arange(N) * complex(0, 1)
    rot = np.exp(rot)
    line_fft = fft*rot
    fft_vectors = get_fft_vectors(line_fft)
    vector_ani.set_data(fft_vectors[0], fft_vectors[1])

    # circles
    for i in range(len(circle_anis)):
        circle_data = circles_points[i]
        circle_anis[i].set_data(circle_data[0]+fft_vectors[0][i], circle_data[1]+fft_vectors[1][i])

    # trajectories
    trajectories[0].append(xn.real)
    trajectories[1].append(xn.imag)
    trajectories_ani.set_data(trajectories[0], trajectories[1])
    # print(len(trajectories[0]))
    point_ani.set_data(xn.real, xn.imag)
    if n == N - 1:
        trajectories[0].clear()
        trajectories[1].clear()
    return [point_ani, vector_ani] + circle_anis + [trajectories_ani]

def get_circle_points(r, num):
    points = []
    x = np.linspace(-r, r, int(num)//2)
    y_up = np.sqrt(r**2-x**2)
    y_down = - y_up
    y = np.concatenate((y_down, y_up[::-1]))
    x = np.concatenate((x, x[::-1]))
    points = np.array([x, y])
    return points
def get_vector_circles(fft):
    tmp = fft/len(fft)
    x, y = tmp.real, tmp.imag
    r = np.sqrt(x**2 +y**2)
    r_points_ratio = r/np.max(r)
    circles = []
    for i in range(len(x)):
        circle_points = get_circle_points(r[i], int(len(x)*10*r_points_ratio[i]))
        circles.append(np.array(circle_points))
    return circles
def fourier_draw(x: list, y: list):
    complex_data = np.array([complex(i, j) for i, j in zip(x, y)])
    
    fft = np.fft.fft(complex_data)
    # print(fft)
    # fft /= len(fft)
    
    # 设置坐标轴
    fig = draw_axis()
    # 绘制原始形状
    plt.plot(x, y, c='y', alpha=0.15)

    # 绘制箭头
    fft_vectors = get_fft_vectors(fft)
    vector_ani, = plt.plot(fft_vectors[0], fft_vectors[1], "-", linewidth = 0.8, alpha=0.75)
    # 绘制端点
    point_ani, = plt.plot(x[0], y[0], 'ro', c='r')

    # 绘制圆圈
    circles_points = get_vector_circles(fft)
    circle_anis = [plt.plot(circle[0]+fft_vectors[0][i], circle[1]+fft_vectors[1][i], '-', alpha=.5, linewidth = 0.5)[0] \
        for i, circle in enumerate(circles_points)]
    # 绘制轨迹
    trajectories = [[x[0]], [y[0]]]
    trajectories_ani,  = plt.plot(trajectories[0], trajectories[1], '-', color='g')
    
    ani = animation.FuncAnimation(fig, step, [(fft, i, point_ani, vector_ani, circle_anis, circles_points, trajectories_ani, trajectories) for i in range(len(x))], interval=10, blit=True)
    # draw_vector_circle(fft)
    # plt.plot([0, 1], [0, 1], c='y', alpha=0.3)
    return ani

if __name__ == '__main__':
    t = np.linspace(np.pi/2, 2.5*np.pi, 200)
    p = (1-np.sin(t))
    x = p*np.cos(t)
    y = p*np.sin(t)
    ani = fourier_draw(x, y)
    # ani.save('fourier.gif', writer='imagemagick', fps=25)
    plt.show()