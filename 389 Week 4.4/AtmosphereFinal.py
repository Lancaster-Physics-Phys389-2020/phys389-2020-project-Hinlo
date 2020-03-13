import numpy as np
import pandas as pd
import math
import copy
import random
from scipy import constants
from CosmicRayClass import CosmicRay
from AtmosphereSupportFunctions import BunchFunction, Direction



def Atmosphere(RunTime, NumberofCosmicRays):
    Bunch = BunchFunction(NumberofCosmicRays)
    InteractionOnOff = str(input('Would you like: \n - Non-Interacting Primary Cosmic Rays? [Input N] \n - Interacting Cosmic Rays [Input I] \n')) # \n Both Types [Input B] '))
    if InteractionOnOff == 'I' or InteractionOnOff == 'i':
        Update = 1
    else:
        Update = 0
    
    for j in range(NumberofCosmicRays):

        time = 0.0
        deltaT = 0.01*RunTime
        TimeList = []
        Bunch[j].interact = 0
        PositionList = [[],[],[]]
        VelocityList = [[],[],[]]
        AccelerationList = [[],[],[]]
        ListofDirections = Direction(Bunch[j].velocity)

        for _ in np.arange(0, RunTime, deltaT):
            
            TimeList.append(time)
            if Update == 1:
                # Bunch[j].InteractionCheck(...)
                Bunch[j].CosmicRayInteractionUpdate(deltaT, PositionList, VelocityList, AccelerationList, ListofDirections)
            else:  
                Bunch[j].CosmicRayUpdate(deltaT, PositionList, VelocityList, AccelerationList, ListofDirections)
            time += deltaT
        # print(len(PositionList[0]),len(PositionList[1]),len(PositionList[2]), len(VelocityList[0]),len(VelocityList[1]),len(VelocityList[2]),len(AccelerationList[0]),len(AccelerationList[1]),len(AccelerationList[2]))
        CosmicRayData = {'Particle Number':j+1, 'Time':TimeList, 'X Position':PositionList[0], 'Y Position':PositionList[1],'Z Position':PositionList[2],
                        'X Velocity':VelocityList[0], 'Y Velocity':VelocityList[1], 'Z Velocity':VelocityList[2],
                        'X Acceleration':AccelerationList[0], 'Y Acceleration':AccelerationList[1], 'Z Acceleration':AccelerationList[2]}
        CosmicRayDataFrame = pd.DataFrame(CosmicRayData)
        CosmicRayDataFrame.to_pickle('Data/Cosmic_Ray_Data_%s.csv' %(j+1))
        percent = round((j+1)/(len(Bunch))*100, 1)
        print('Simulation is %s %% complete' %(percent))
    return(Bunch)
    
