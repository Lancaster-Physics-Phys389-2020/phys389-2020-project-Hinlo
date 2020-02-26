import numpy as np
import pandas as pd
import math
import copy
from scipy import constants
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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
        
        PositionList.append(CosmicRay.position)
        VelocityList.append(CosmicRay.velocity)
        AccerlerationList.append(CosmicRay.acceleration)
        TimeList.append(time)

        print('time =',time,'Position =', CosmicRay.position, 'velocity =', CosmicRay.velocity)
        beta = CosmicRay.beta()

        for i in range(len(CosmicRay.velocity)):

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
        #copy.copy(PositionList)
        time += deltaT
        
    print(PositionList)
    CosmicRayPositionData = pd.DataFrame(PositionList, columns = ['X Position','Y Position','Z Position'])
    CosmicRayVelocityData = pd.DataFrame(VelocityList, columns = ['X Position','Y Position','Z Position'])
    print(TimeList)
    print(CosmicRayPositionData)
    print(CosmicRayVelocityData)
    








Atmosphere(Proton, 0.0001)