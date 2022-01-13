#EXERCISE 3
""" 2. Draw a plot for the following data:
Temperature in degree Celsius	Sales
12	100
14	200
16	250
18	400
20	300
22	450
24	500
"""

import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([12,14,16,18,20,22,24])
ypoints = np.array([100,200,250,400,300,450,500])
plt.plot(xpoints,ypoints,'s-.b',ms=5)

plt.xlabel("Temperature in degree Celsius")
plt.ylabel("Sales")
plt.title("TEMPERATURE")

plt.grid(color="brown",linestyle="--")
plt.show()
