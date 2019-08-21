import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

fig = plt.figure(tight_layout=True)
plt.plot(x,y)
plt.grid(ls="--")
plt.show()