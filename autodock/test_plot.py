import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-10, 10, 100)

y = x**2 + 5

plt.plot(x, y)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('graph')

plt.show()
