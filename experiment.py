import numpy as np

a = np.array([-1,-3,0,0])
# print(np.isnan(a).sum())
a=a.reshape(2,2)
print(np.mod(a,2))
