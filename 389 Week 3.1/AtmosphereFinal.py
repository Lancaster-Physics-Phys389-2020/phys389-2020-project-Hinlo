import numpy as np
import pandas as pd
import math
import copy
from scipy import constants

from Particle import Particle
from Particle import Charticle
# from ParticleBunchClass import ParticleBunch
from AtmosphereSupportFunctions import BunchFunction, StoppingForce, NonRelativisticStoppingForce, Direction, ForceDirectionCheck



def Atmosphere(RunTime, NumberofCosmicRays):

    Bunch = BunchFunction(NumberofCosmicRays)
    

    for j in range(NumberofCosmicRays):

        time = 0.0
        deltaT = 0.01*RunTime
        PositionList = [[],[],[]]
        VelocityList = [[],[],[]]
        AccerlerationList = [[],[],[]]
        TimeList = []
        ListofDirections = Direction(Bunch[j].velocity)
        print(Bunch[j])

        for _ in np.arange(0, RunTime, deltaT):
            
            TimeList.append(time)
            beta = Bunch[j].beta()

            for i in range(len(Bunch[j].velocity)):
                PositionList[i].append(Bunch[j].position[i])
                VelocityList[i].append(Bunch[j].velocity[i])
                if np.abs(Bunch[j].velocity[i]) <= 2.74E6: # minimum speed before bethe stopping power eqn breaks due to -ve ln.
                    AccerlerationList[i].append(Bunch[j].acceleration[i])

                else:
                    if np.abs(Bunch[j].velocity[i]) >= 1E7:
                        Force = StoppingForce(5.3E25,Bunch[j].charge,beta[i],1.36E-17) # using stratosphere eDensity for now.                 
                    else:
                        Force = NonRelativisticStoppingForce(5.3E25,Bunch[j].charge,Bunch[j].velocity[i],1.36E-17) # using stratosphere eDensity for now.                    

                    AccelerationCalc = (Force/Bunch[j].mass)
                    Bunch[j].acceleration[i] = ForceDirectionCheck(ListofDirections[i],AccelerationCalc)                
                    AccerlerationList[i].append(Bunch[j].acceleration[i])
                    Bunch[j].Velocityupdate(i,deltaT)
                    
                    if ListofDirections[i] == 1 and Bunch[j].velocity[i] < 0:
                        Bunch[j].velocity[i] = 0
                        Bunch[j].acceleration[i] = 0 
                        Bunch[j].Positionupdate(i,deltaT)
                    elif ListofDirections[i] == -1 and Bunch[j].velocity[i] > 0:
                        Bunch[j].velocity[i] = 0
                        Bunch[j].acceleration[i] = 0 
                        Bunch[j].Positionupdate(i,deltaT)
                    else:
                        Bunch[j].Positionupdate(i,deltaT)
            time += deltaT

        CosmicRayData = {'Particle Number':j+1, 'Time':TimeList, 'X Position':PositionList[0], 'Y Position':PositionList[1],'Z Position':PositionList[2],
                        'X Velocity':VelocityList[0], 'Y Velocity':VelocityList[1], 'Z Velocity':VelocityList[2],
                        'X Acceleration':AccerlerationList[0], 'Y Acceleration':AccerlerationList[1], 'Z Acceleration':AccerlerationList[2]}
        CosmicRayDataFrame = pd.DataFrame(CosmicRayData)
        CosmicRayDataFrame.to_pickle('Cosmic_Ray_Data_%s.csv' %(j+1))
    return(Bunch)
    

Atmosphere(0.0001,10)
