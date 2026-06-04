import numpy as np
import matplotlib.pyplot as plt

x = np.array([100, 10000, 20000, 30000, 40000, 50000, 60000])
y = np.array([0.056, 0.161, 0.169, 0.172, 0.194, 0.258, 0.264])

plt.plot(x, y)

plt.xlabel("size of the message")
plt.ylabel("milliseconds")

plt.show()
