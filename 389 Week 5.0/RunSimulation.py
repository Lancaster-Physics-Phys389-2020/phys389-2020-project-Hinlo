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
InteractionOnOff = str(input('Would you like: \n - Non-Interacting Primary Cosmic Rays? [Input N] \n - Interacting Cosmic Rays [Input I] \n'))
if InteractionOnOff == 'I' or InteractionOnOff == 'i':
    SaveDetail = 'Interacting'
else:
    SaveDetail = 'Non_Interacting'
dataframelist = []

def DataRead():
    for j in range(NumberofParticles):
        Data = pd.read_pickle('Data/Cosmic_Ray_Data_%s.csv' %(j+1))
        dataframelist.append(Data)
        DataReadPercent = round((j+1)/(NumberofParticles)*100, 1)
        print('Data Read is %s %% complete' %(DataReadPercent))

def DataFrameShow():
    pd.options.display.max_rows = 150
    pd.options.display.max_columns = 150
    pd.options.display.width = 50000 
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
        DistanceList.append(DataFrames[i]['Y Position [m]'][99])
        ax.plot3D(DataFrames[i]['X Position [m]'], DataFrames[i]['Z Position [m]'], DataFrames[i]['Y Position [m]'])
        TrajectoryPercent = round((i+1)/(len(DataFrames))*100, 1)
        print('Data Plots are %s %% complete' %(TrajectoryPercent))
    MinYposition = min(DistanceList)
    MaxYposition = DataFrames[0]['Y Position [m]'][0]
    difference = (MaxYposition - MinYposition)/2
    ax.set_xlim3d(-difference, difference)
    ax.set_ylim3d(-difference, difference)
    ax.set_zlim3d(MinYposition, MaxYposition) # this is y data; have put on z axis to show cosmic rays fall from the sky.
    ax.set_xlabel('X Position [m]')
    ax.set_ylabel('Z Position [m]')
    ax.set_zlabel('Y Position [m]')
    plt.savefig('Figures/Trajectory_Plot_%s_%s_Cosmic_Rays.png'%(NumberofParticles, SaveDetail),bbox_inches = 'tight')
    plt.show()

def DecelerationPlot(DataFrames):
    for i in range(len(DataFrames)):
        plt.plot(DataFrames[i]['Time [s]'], -DataFrames[i]['Y Velocity [m/s]'])
    plt.xlabel('Time [s]')
    plt.ylabel('Y-Velocity [m/s]')
    plt.savefig('Figures/Deceleration_Plot_%s_%s_Cosmic_Rays.png'%(NumberofParticles, SaveDetail),bbox_inches = 'tight')
    plt.show()


def EnergyLossPlot(DataFrames):
    for i in range(len(DataFrames)):
        plt.plot(DataFrames[i]['Time [s]'], DataFrames[i]['Particle Energy [J]'])
    plt.xlabel('Time [s]')
    plt.ylabel('Particle Energy [J]')
    plt.savefig('Figures/EnergyLoss_Plot_%s_%s_Cosmic_Rays.png'%(NumberofParticles, SaveDetail),bbox_inches = 'tight')
    plt.show()



Atmosphere(0.000184, NumberofParticles, InteractionOnOff)
DataRead()
DataFrameShow()
TrajectoryPlot(dataframelist)
DecelerationPlot(dataframelist)
EnergyLossPlot(dataframelist)


