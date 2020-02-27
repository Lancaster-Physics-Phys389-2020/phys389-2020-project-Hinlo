import numpy as np
import pandas as pd
import math
import copy
from scipy import constants


from Particle import Particle
from Particle import Charticle



Proton = Charticle([0,0,0], [0,2.5E8,0], [0,0,0],'Proton', 1.67E-27, 1)


def StoppingForce(eDensity,charge,beta,V_excitation): # Note beta is different for each x, y, z direction
    t1 = (4*math.pi)/(constants.electron_mass*constants.speed_of_light*constants.speed_of_light)
    t2 = (eDensity*charge*charge)/(beta*beta)
    t3 = (constants.elementary_charge*constants.elementary_charge)/(4*math.pi*constants.epsilon_0)
    ln = np.log((2*constants.electron_mass*constants.speed_of_light*constants.speed_of_light*beta*beta)/(V_excitation*(1-beta*beta)))
    t4 = ln - beta*beta
    StoppingForce = -t1*t2*t3*t3*t4
    return(StoppingForce)

def Direction(VelocityVector):
    DirectionList = []
    for i in range(len(VelocityVector)):
        if VelocityVector[i] >= 0:
            DirectionList.append(1)
        else:
            DirectionList.append(-1)
    return(DirectionList)

def ForceDirectionCheck(DirectionList,Acceleration):
    for i in range(len(DirectionList)):
        if DirectionList[i] == 1:
            return(Acceleration)
        else: 
            return(-Acceleration)


def Atmosphere(CosmicRay,RunTime):
    
    #Initialise values
    time = 0.0
    deltaT = 0.1*RunTime

    PositionList = [[],[],[]]
    VelocityList = [[],[],[]]
    AccerlerationList = [[],[],[]]
    TimeList = []

    #Get direction of motion
    ListofDirections = Direction(CosmicRay.velocity)
    
    #Begin simulation over Run time
    for _ in np.arange(0, RunTime, deltaT):
        
        
        
        TimeList.append(time)

        
        beta = CosmicRay.beta()

        for i in range(len(CosmicRay.velocity)):
            PositionList[i].append(CosmicRay.position[i])
            VelocityList[i].append(CosmicRay.velocity[i])
            AccerlerationList[i].append(CosmicRay.acceleration[i])
            if CosmicRay.velocity[i] == 0:
                continue
            else:
                Force = StoppingForce(2.5E25,CosmicRay.charge,beta[i],1.29E-17)
                CosmicRay.acceleration[i] = (Force/CosmicRay.mass)
                CosmicRay.acceleration[i] = ForceDirectionCheck(ListofDirections,CosmicRay.acceleration[i])
                CosmicRay.update(deltaT)

                if ListofDirections[i] == 1 and CosmicRay.velocity[i] < 0:
                    CosmicRay.velocity[i] = 0
                    CosmicRay.acceleration[i] = 0 
                elif ListofDirections[i] == -1 and CosmicRay.velocity[i] > 0:
                    CosmicRay.velocity[i] = 0
                    CosmicRay.acceleration[i] = 0 
                else:
                    continue
        
        time += deltaT



    CosmicRayData = {'Time':TimeList, 'X Position':PositionList[0], 'Y Position':PositionList[1],'Z Position':PositionList[2],
                     'X Velocity':VelocityList[0], 'Y Velocity':VelocityList[1], 'Z Velocity':VelocityList[2],
                     'X Acceleration':AccerlerationList[0], 'Y Acceleration':AccerlerationList[1], 'Z Acceleration':AccerlerationList[2]}
    CosmicRayDataFrame = pd.DataFrame(CosmicRayData)
    CosmicRayDataFrame.to_pickle('Cosmic_Ray_Data.csv')
    

    
Atmosphere(Proton, 0.0001)