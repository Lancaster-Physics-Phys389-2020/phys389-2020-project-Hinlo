import numpy as np
import pandas as pd
import math
import copy
from scipy import constants

from Particle import Particle
from Particle import Charticle

#This file only works at relativistic speeds, at lower speeds, stoppingforce eqn breaks down.
Proton = Charticle([0,2.5E4,0], [2.5E8,-2.5E8,0], [0,0,0],'Proton', 1.67E-27, 1)

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
    
def ForceDirectionCheck(VelcoityComponent,AccelerationComponent):
    if VelcoityComponent >= 0:
        return(AccelerationComponent)
    else: 
        return(-AccelerationComponent)

def Atmosphere(CosmicRay,RunTime):
    
    #Initialise values
    time = 0.0
    deltaT = 0.05*RunTime

    PositionList = [[],[],[]]
    VelocityList = [[],[],[]]
    AccerlerationList = [[],[],[]]
    TimeList = []

    #Get direction of motion
    ListofDirections = Direction(CosmicRay.velocity)
    print(ListofDirections)
    #Begin simulation over Run time
    for _ in np.arange(0, RunTime, deltaT):
        
        TimeList.append(time)
        beta = CosmicRay.beta()

        for i in range(len(CosmicRay.velocity)):
            PositionList[i].append(CosmicRay.position[i])
            VelocityList[i].append(CosmicRay.velocity[i])
            if CosmicRay.velocity[i] == 0:
                AccerlerationList[i].append(CosmicRay.acceleration[i])
            else:
                Force = StoppingForce(2.5E25,CosmicRay.charge,beta[i],1.29E-17)
                AccelerationCalc = (Force/CosmicRay.mass)
                CosmicRay.acceleration[i] = ForceDirectionCheck(CosmicRay.velocity[i],AccelerationCalc)
                AccerlerationList[i].append(CosmicRay.acceleration[i])
                
                CosmicRay.update(i,deltaT)

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
    print(CosmicRayDataFrame)
    CosmicRayDataFrame.to_pickle('Cosmic_Ray_Data.csv')
    
    
Atmosphere(Proton, 0.0001)