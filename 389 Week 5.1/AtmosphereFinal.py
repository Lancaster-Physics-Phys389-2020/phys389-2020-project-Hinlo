import numpy as np
import pandas as pd
import math
import copy
import random
from scipy import constants
from CosmicRayClass import CosmicRay
from AtmosphereSupportFunctions import BunchFunction, Direction, Interacted

"""
Imports CosmicRay class and functions from its supporting functions file and uses these to update the parameters of each cosmic ray in the initial bunch, at each time
step over a given run time. The lists of parameter values are made into a dictionary and subsequently into a dataframe which is then pickled, saving to the 'Data' Folder.

Parameters:
- RunTime (float):
- NumberofCosmicRays (int):
- InteractionOnOff (string):

DataMembers:


DataMembers:
"""

def Atmosphere(RunTime, NumberofCosmicRays, InteractionOnOff):
    Bunch = BunchFunction(NumberofCosmicRays)
    interactionOnOff = InteractionOnOff
    if interactionOnOff == 'I' or interactionOnOff == 'i':
        Update = 1
    else:
        Update = 0
    
    for j in range(NumberofCosmicRays):

        time = 0.0
        deltaT = 0.001*RunTime
        TimeList = []
        InteractList = []
        ParticleEnergyList = []
        PositionList = [[],[],[]]
        VelocityList = [[],[],[]]
        AccelerationList = [[],[],[]]
        ListofDirections = Direction(Bunch[j].velocity)

        for _ in np.arange(0, RunTime, deltaT):
            TimeList.append(time)
            Bunch[j].GammaUpdate()
            Bunch[j].MassUpdate()
            ParticleEnergyList.append(Bunch[j].ParticleEnergyUpdate())

            if Update == 1:
                InteractList.append(Interacted(Bunch[j].interact)) 
                Bunch[j].CosmicRayInteractionUpdate(deltaT, PositionList, VelocityList, AccelerationList, ListofDirections)
                Bunch[j].InteractionCheck()
            else:  
                Bunch[j].CosmicRayUpdate(deltaT, PositionList, VelocityList, AccelerationList, ListofDirections)
                InteractList.append('N/A')
            
            time += deltaT
        CosmicRayData = {'Particle Number':j+1, 'Time [s]':TimeList, 'Interacted?':InteractList, 'Particle Energy [J]':ParticleEnergyList, 
                        'X Position [m]':PositionList[0], 'Y Position [m]':PositionList[1],'Z Position [m]':PositionList[2],
                        'X Velocity [m/s]':VelocityList[0], 'Y Velocity [m/s]':VelocityList[1], 'Z Velocity [m/s]':VelocityList[2],
                        'X Acceleration [m/s^2]':AccelerationList[0], 'Y Acceleration [m/s^2]':AccelerationList[1], 'Z Acceleration [m/s^2]':AccelerationList[2]}
        CosmicRayDataFrame = pd.DataFrame(CosmicRayData)
        CosmicRayDataFrame.to_pickle('Data/Cosmic_Ray_Data_%s.csv' %(j+1))
        percent = round((j+1)/(len(Bunch))*100, 1)
        print('Simulation is %s %% complete' %(percent))
    return(Bunch)
    
