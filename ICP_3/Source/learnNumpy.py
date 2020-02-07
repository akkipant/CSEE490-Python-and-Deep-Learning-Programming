import numpy as np

num = np.random.randint(1,20,15)
print(num)
newNum = np.reshape(num, (3, 5))
print(newNum)

print(np.max(newNum, axis=1).reshape(-1,1))


print(np.where(newNum == np.max(newNum, axis=1).reshape(-1,1), 0, newNum))