import numpy as np
import pandas as pd
import math
import copy
from scipy import constants
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


NumberofCosmicRays = int(input('How Many Cosmic Rays are in the bunch?'))
dataframelist = []
for j in range(NumberofCosmicRays):
    Data = pd.read_pickle('Cosmic_Ray_Data_%s.csv' %(j+1))
    dataframelist.append(Data)
print(dataframelist)

        
        


def TrajectoryPlot(DataFrames):   
    ax = plt.axes(projection='3d')
    for i in range(len(DataFrames)):
        ax.plot3D(DataFrames[i]['X Position'], DataFrames[i]['Z Position'], DataFrames[i]['Y Position'])
    ax.set_xlabel('X Position [m]')
    ax.set_ylabel('Z Position [m]')
    ax.set_zlabel('Y Position [m]')
    plt.show()


def DecelerationPlot(DataFrames):
    for i in range(len(DataFrames)):
        plt.plot(DataFrames[i]['Time'], -DataFrames[i]['Y Velocity'])
    plt.xlabel('Time [s]')
    plt.ylabel('Y-Velocity [m/s]')
    plt.show()



TrajectoryPlot(dataframelist)
DecelerationPlot(dataframelist)

