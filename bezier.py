import matplotlib.pyplot as plt
import numpy as np
from draw import fourier_draw
def bezier3(P, n):
    P = np.array(P)
    points = []
    for t in np.linspace(0, 1, n):
        pt = P[0]*(1-t)**3 + 3*P[1]*t*(1-t)**2 + 3*P[2]*t**2*(1-t) + P[3]*t**3
        points.append(pt)
    return np.array(points)
def heart_line():
    P = [[0, 0], [1.5, 1.2], [1.1, -1], [0, -1.4]]
    n = 100
    points = bezier3(P, 100)
    # x, y = points[:, 0], -points[:, 1]
    # plt.plot(points[:, 0], -points[:, 1], '-')
    # plt.show()
    points_left = points.copy()
    points_left[:, 0] = -points_left[:, 0]
    points_left = points_left[::-1]
    points = np.concatenate((points, points_left))
    fourier_draw(points[:, 0], points[:, 1])
    plt.show()
    pass
def str2point(string):
    subs = string.split(' ')
    points = []
    for sub in subs:
        x, y = sub.split(',')
        points.append([float(x), float(y)])
    return np.array(points)
def convert_from_svg(svg):
    max_points = 25
    svg = svg[1:-1]
    sub_curves = svg.split('c')
    curves = []
    # start = str2point(sub_curves[0])[0]
    start = [0, 0]
    for i in range(1, len(sub_curves)):
        points = str2point(sub_curves[i])
        points += start
        curves.append({'points': np.concatenate([[start], points]), 'num':max_points})
        start = points[-1]
    return curves

if __name__ == '__main__':
    # <path id="svg_2" d="m69,304.5c0,0 6,21 6,21c69,-34 98,-172 98,-172c-62,196 54,90 54,89c0,-1 151,-8 -43,-99c207,85 91,-51 91,-51c-30,-140 -91,18 -99,38c70,-189 -66,-94 -52,-71c-101,10 -78,67 36,82c-187,-32 -87,57 -87,57c16,139 90,-49 90,-49c0,0 -18,134 -94,155z" stroke-width="1.5" stroke="#000" fill="#fff"/></g>
    # svg = 'm363,123.5c0,0 100,-1 100,-1c0,0 -70,-59 -70,-59.5c0,0.5 -30,60.5 -30,60.5z'
    svg = 'm69,304.5c0,0 6,21 6,21c69,-34 98,-172 98,-172c-62,196 54,90 54,89c0,-1 151,-8 -43,-99c207,85 91,-51 91,-51c-30,-140 -91,18 -99,38c70,-189 -66,-94 -52,-71c-101,10 -78,67 36,82c-187,-32 -87,57 -87,57c16,139 90,-49 90,-49c0,0 -18,134 -94,155z'
    curves = convert_from_svg(svg)
    graph = []
    for segm in curves:
        graph.append(bezier3(segm['points'], segm['num']))
    points = np.concatenate(graph)
    points = points
    fourier_draw(points[:, 0], -points[:, 1])
    plt.show()
[[2,14], [67,-10], [92,-163], [100,-166]]