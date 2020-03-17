import numpy as np
import pandas as pd
import math
import copy
import random
from scipy import constants
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""
Functions utilised in running the RunSimulation file. 

Functions:

- DataRead:
    Parameters:
    - Number of Particles (int): The number of cosmic rays in the simulation.
    - Dataframes (List): Contains the dataframe of each cosmic ray in the simulation.
    DataMembers:
    - Data (DataFrame): The dataframe of a given particle. This is appended to the DataFrames list.
    - DataReadPercent (float): percentage complete value printed to show how much of the data read has been completed.
    
- DataFrameShow:
    Parameters:
    - Dataframes (List): Contains the dataframe of each cosmic ray in the simulation.
    DataMembers:
    - Answer (str, User Input): A statment allowing the user to decide whether or not to look at any cosmic ray dataframe.
    - ParticleNumber (int, User Input): A value allowing the user to select which cosmic ray dataframe they would like to look at.

- TrajectoryPlot, DecelerationPlot, EnergyLossPlot:
    Parameters:
    - Dataframes (List): Contains the dataframe of each cosmic ray in the simulation.
    - Number of Particles (int): The number of cosmic rays in the simulation.
    - SaveDetail (str): A statement used to identify the plots as for interacting or non-interacting cosmic rays when saving.
    DataMembers:
    - DistanceList (List): Contains the final verticle positions of each particle in the simulation, these are used to set the graph axis limits.

"""


def DataRead(NumberofParticles, DataFrames):
    for j in range(NumberofParticles):
        Data = pd.read_pickle('Data/Cosmic_Ray_Data_%s.csv' %(j+1))
        DataFrames.append(Data)
        DataReadPercent = round((j+1)/(NumberofParticles)*100, 1) 
        print('Data Read is %s %% complete' %(DataReadPercent))

def DataFrameShow(DataFrames):
    pd.options.display.max_rows = 150
    pd.options.display.max_columns = 150
    pd.options.display.width = 50000 
    Answer = str(input('Would you like to look at the data frames for any particles?\n [Type Y/N]\n')) # This loop allows the user to look at as many dataframes as they would like.
    if Answer == 'Y' or Answer == 'y':
        Repeat = 'Y'
        while Repeat == 'Y' or Repeat == "y":
            ParticleNumber = int(input('Which Particle would you like to look at?\n [Input only its number]\n'))      
            print(DataFrames[ParticleNumber-1])
            Repeat = str(input('\nWould you like to look at any more Particles?\n [Type Y/N]\n '))
        
def TrajectoryPlot(DataFrames, NumberofParticles, SaveDetail):
    DistanceList = []
    ax = plt.axes(projection='3d')
    for i in range(len(DataFrames)):
        DistanceList.append(DataFrames[i]['Y Position [m]'][999])
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

def DecelerationPlot(DataFrames, NumberofParticles, SaveDetail):
    for i in range(len(DataFrames)):
        plt.plot(DataFrames[i]['Time [s]'], -DataFrames[i]['Y Velocity [m/s]'])
    plt.xlabel('Time [s]')
    plt.ylabel('Y-Velocity [m/s]')
    plt.savefig('Figures/Deceleration_Plot_%s_%s_Cosmic_Rays.png'%(NumberofParticles, SaveDetail),bbox_inches = 'tight')
    plt.show()


def EnergyLossPlot(DataFrames, NumberofParticles, SaveDetail):
    for i in range(len(DataFrames)):
        plt.plot(DataFrames[i]['Time [s]'], DataFrames[i]['Particle Energy [J]'])
    plt.xlabel('Time [s]')
    plt.ylabel('Particle Energy [J]')
    plt.savefig('Figures/EnergyLoss_Plot_%s_%s_Cosmic_Rays.png'%(NumberofParticles, SaveDetail),bbox_inches = 'tight')
    plt.show()