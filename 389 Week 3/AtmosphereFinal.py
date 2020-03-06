import numpy as np
import pandas as pd
import math
import copy
from scipy import constants

from Particle import Particle
from Particle import Charticle
from AtmosphereSupportFunctions import StoppingForce, NonRelativisticStoppingForce, Direction, ForceDirectionCheck

Proton = Charticle([0,8E4,0], [0.6*constants.speed_of_light,-0.7*constants.speed_of_light,0], [0,0,0],'Proton', 1.67E-27, 1) # 80E4 is top of mesosphere, cosmic ray speed range 0.43c - 0.996c

def Atmosphere(CosmicRay,RunTime):
    
    time = 0.0
    deltaT = 0.01*RunTime
    PositionList = [[],[],[]]
    VelocityList = [[],[],[]]
    AccerlerationList = [[],[],[]]
    TimeList = []
    ListofDirections = Direction(CosmicRay.velocity)

    for _ in np.arange(0, RunTime, deltaT):
        
        TimeList.append(time)
        beta = CosmicRay.beta()

        for i in range(len(CosmicRay.velocity)):
            PositionList[i].append(CosmicRay.position[i])
            VelocityList[i].append(CosmicRay.velocity[i])
            if np.abs(CosmicRay.velocity[i]) <= 2.74E6: # minimum speed before bethe stopping power eqn breaks due to -ve ln.
                AccerlerationList[i].append(CosmicRay.acceleration[i])

            else:
                if np.abs(CosmicRay.velocity[i]) >= 1E7:
                    Force = StoppingForce(5.3E25,CosmicRay.charge,beta[i],1.36E-17) # using stratosphere eDensity for now.                 
                else:
                    Force = NonRelativisticStoppingForce(5.3E25,CosmicRay.charge,CosmicRay.velocity[i],1.36E-17) # using stratosphere eDensity for now.                    

                AccelerationCalc = (Force/CosmicRay.mass)
                CosmicRay.acceleration[i] = ForceDirectionCheck(ListofDirections[i],AccelerationCalc)                
                AccerlerationList[i].append(CosmicRay.acceleration[i])
                CosmicRay.Velocityupdate(i,deltaT)
                
                if ListofDirections[i] == 1 and CosmicRay.velocity[i] < 0:
                    CosmicRay.velocity[i] = 0
                    CosmicRay.acceleration[i] = 0 
                    CosmicRay.Positionupdate(i,deltaT)
                elif ListofDirections[i] == -1 and CosmicRay.velocity[i] > 0:
                    CosmicRay.velocity[i] = 0
                    CosmicRay.acceleration[i] = 0 
                    CosmicRay.Positionupdate(i,deltaT)
                else:
                    CosmicRay.Positionupdate(i,deltaT)
        time += deltaT

    CosmicRayData = {'Time':TimeList, 'X Position':PositionList[0], 'Y Position':PositionList[1],'Z Position':PositionList[2],
                     'X Velocity':VelocityList[0], 'Y Velocity':VelocityList[1], 'Z Velocity':VelocityList[2],
                     'X Acceleration':AccerlerationList[0], 'Y Acceleration':AccerlerationList[1], 'Z Acceleration':AccerlerationList[2]}
    CosmicRayDataFrame = pd.DataFrame(CosmicRayData)
    CosmicRayDataFrame.to_pickle('Cosmic_Ray_Data.csv')
    return(CosmicRay)
    

Atmosphere(Proton, 0.0001)
