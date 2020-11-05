import numpy as np


def wrapToPi(angle):
    return (angle + np.pi) % (2*np.pi) - np.pi

def rotmat2d(angle):
    return np.array([[np.cos(angle), -np.sin(angle)],
                     [np.sin(angle),  np.cos(angle)]])

# g = np.array([[1,2,3], [4,5,6]]).T
# x = np.array([1,1])

# y = np.array([1,1,1])
# x = np.array([3,3,3])
# print(np.concatenate((x.T, y.T), axis=1))

x = [1,2,3,4,5,6,7]
print(x[0::2])
