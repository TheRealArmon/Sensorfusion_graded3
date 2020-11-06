from typing import List, Optional

from scipy.io import loadmat
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import animation
from scipy.stats import chi2
import scipy.linalg as la
import utils

# Load data
simSLAM_ws = loadmat("simulatedSLAM")

z = [zk.T for zk in simSLAM_ws["z"].ravel()]

landmarks = simSLAM_ws["landmarks"].T
odometry = simSLAM_ws["odometry"].T
poseGT = simSLAM_ws["poseGT"].T

K = len(z)
M = len(landmarks)

# print(len(landmarks))
# print(landmarks[30])
# print(len(odometry))
# print(odometry[30])
# print(len(poseGT))
# print(poseGT[30])
# print(poseGT[31])

errPos = 0
errX = 0
errY = 0
errPsi = 0


#err = [  for i in range(K)]
for i in range(1,K+1):
    rot = utils.rotmat2d(poseGT[i][2])
    delta_pos = poseGT[i][:2] - (poseGT[i-1][:2] + rot @ odometry[i-1][:2])
    errPos += la.norm(delta_pos)
    errX += abs(delta_pos[0])
    errY += abs(delta_pos[1])
    errPsi += (poseGT[i][2] - (poseGT[i-1][2] + odometry[i-1][2]))**2

xRMSE = np.sqrt(np.mean(errX)/1000)
yRMSE = np.sqrt(np.mean(errY)/1000)
psiRMSE = np.sqrt(np.mean(errPsi)/1000)

#print(errPos/K)
print(f"Pos error: {np.round(errPos/K, 4)}")
print(f"X error: {np.round(xRMSE, 4)}")
print(f"Y error: {np.round(yRMSE, 4)}")
print(f"Psi error: {np.round(psiRMSE, 4)}")

print(np.mean(errY))
print(errY/1000)
# print(print(poseGT[200:210]))