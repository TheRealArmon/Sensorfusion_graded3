from typing import List, Optional

from scipy.io import loadmat
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import animation
from scipy.stats import chi2
import scipy.linalg as la
import utils

def estimate_Q(simSLAM_ws):
# Load data
#simSLAM_ws = loadmat("simulatedSLAM")

    z = [zk.T for zk in simSLAM_ws["z"].ravel()]

    landmarks = simSLAM_ws["landmarks"].T
    odometry = simSLAM_ws["odometry"].T
    poseGT = simSLAM_ws["poseGT"].T

    K = len(z)

    errX = 0
    errY = 0
    errPsi = 0

    for i in range(1,K+1):
        rot = utils.rotmat2d(poseGT[i][2])
        delta_pos = poseGT[i][:2] - (poseGT[i-1][:2] + rot @ odometry[i-1][:2])

        errX += delta_pos[0]**2
        errY += delta_pos[1]**2
        errPsi += (poseGT[i][2] - (poseGT[i-1][2] + odometry[i-1][2]))**2

    xRMSE = np.sqrt(errX/K)
    yRMSE = np.sqrt(errY/K)
    psiRMSE = np.sqrt(errPsi/K)

    return xRMSE, yRMSE, psiRMSE

# print(f"X error: {np.round(xRMSE, 4)}")
# print(f"Y error: {np.round(yRMSE, 4)}")
# print(f"Psi error: {np.round(psiRMSE, 4)}")
