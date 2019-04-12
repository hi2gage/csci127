import numpy as np
import matplotlib.pyplot as plt

scores = np.random.randint(0,101,10)
ids = np.random.randint(0,11,10)

print(scores)
print(ids)

plt.plot(ids, scores)
plt.axes([0,10,0,100])
plt.show()
