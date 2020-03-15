import numpy as np
import pandas as pd
import math
import copy
import random
from scipy import constants
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from AtmosphereFinal import Atmosphere


NumberofParticles = int(input('How many Cosmic Rays would you like?\n')) # Simulation Runs entirely from this file now!
Atmosphere(0.000136,NumberofParticles)



dataframelist = []
for j in range(NumberofParticles):
    Data = pd.read_pickle('Data/Cosmic_Ray_Data_%s.csv' %(j+1))
    dataframelist.append(Data)
    DataReadPercent = round((j+1)/(NumberofParticles)*100, 1)
    print('Data Read is %s %% complete' %(DataReadPercent))



def DataFrameShow():
    print(len(dataframelist))
    pd.options.display.max_rows = 150
    pd.options.display.max_columns = 15
    pd.options.display.width = 1000
    Answer = str(input('Would you like to look at the data frames for any particles?\n [Type Y/N]\n'))
    if Answer == 'Y' or Answer == 'y':
        Repeat = 'Y'
        while Repeat == 'Y' or Repeat == "y":
            ParticleNumber = int(input('Which Particle would you like to look at?\n [Input only its number]\n'))      
            print(dataframelist[ParticleNumber-1])
            Repeat = str(input('\nWould you like to look at any more Particles?\n [Type Y/N]\n '))
        

def TrajectoryPlot(DataFrames):
    DistanceList = []
    ax = plt.axes(projection='3d')
    for i in range(len(DataFrames)):
        DistanceList.append(DataFrames[i]['Y Position'][99])
        ax.plot3D(DataFrames[i]['X Position'], DataFrames[i]['Z Position'], DataFrames[i]['Y Position'])
        TrajectoryPercent = round((i+1)/(len(DataFrames))*100, 1)
        print('Data Plots are %s %% complete' %(TrajectoryPercent))
    
    MinYposition = min(DistanceList)
    MaxYposition = DataFrames[0]['Y Position'][0]
    difference = (MaxYposition - MinYposition)/2
    
    
    ax.set_xlim3d(-difference, difference)
    ax.set_ylim3d(-difference, difference)
    ax.set_zlim3d(MinYposition, MaxYposition) # this is y data; have put on x axis to show cosmic rays fall from the sky.
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


DataFrameShow()
TrajectoryPlot(dataframelist)
DecelerationPlot(dataframelist)
