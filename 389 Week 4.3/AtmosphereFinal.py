import numpy as np
import pandas as pd
import math
import copy
from scipy import constants
from CosmicRayClass import CosmicRay
from AtmosphereSupportFunctions import BunchFunction, Direction



def Atmosphere(RunTime, NumberofCosmicRays):
    Bunch = BunchFunction(NumberofCosmicRays)
    for j in range(NumberofCosmicRays):

        time = 0.0
        deltaT = 0.01*RunTime
        TimeList = []

        PositionList = [[],[],[]]
        VelocityList = [[],[],[]]
        AccelerationList = [[],[],[]]
        
        ListofDirections = Direction(Bunch[j].velocity)

        for _ in np.arange(0, RunTime, deltaT):
            
            TimeList.append(time)
            Bunch[j].CosmicRayUpdate(deltaT, PositionList, VelocityList, AccelerationList, ListofDirections)
            time += deltaT

        CosmicRayData = {'Particle Number':j+1, 'Time':TimeList, 'X Position':PositionList[0], 'Y Position':PositionList[1],'Z Position':PositionList[2],
                        'X Velocity':VelocityList[0], 'Y Velocity':VelocityList[1], 'Z Velocity':VelocityList[2],
                        'X Acceleration':AccelerationList[0], 'Y Acceleration':AccelerationList[1], 'Z Acceleration':AccelerationList[2]}
        CosmicRayDataFrame = pd.DataFrame(CosmicRayData)
        CosmicRayDataFrame.to_pickle('Data/Cosmic_Ray_Data_%s.csv' %(j+1))
        percent = round((j+1)/(len(Bunch))*100, 1)
        print('Simulation is %s %% complete' %(percent))
    return(Bunch)
    
