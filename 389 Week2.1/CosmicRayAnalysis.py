import numpy as np
import pandas as pd
import math
import copy
from scipy import constants
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

CosmicRayData = pd.read_pickle('Cosmic_Ray_Data.csv')


def TrajectoryPlot(Data):
    ax = plt.axes(projection='3d')
    ax.plot3D(Data['X Position'], Data['Y Position'], Data['Z Position'])
    ax.set_xlabel('X Position [m]')
    ax.set_ylabel('Y Position [m]')
    ax.set_zlabel('Z Position [m]')
    plt.show()


def DecelerationPlot(Data):
    plt.plot(Data['Time'], Data['Y Velocity'])
    plt.xlabel('Time [s]')
    plt.ylabel('Y-Velocity [m/s]')
    plt.show()

print(CosmicRayData)
TrajectoryPlot(CosmicRayData)
DecelerationPlot(CosmicRayData)

