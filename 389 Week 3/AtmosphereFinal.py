import numpy as np
import pandas as pd
import math
import copy
from scipy import constants

from Particle import Particle
from Particle import Charticle

Proton = Charticle([0,2.5E4,0], [2.3E7,-2.5E7,0], [0,0,0],'Proton', 1.67E-27, 1)

def StoppingForce(eDensity,charge,beta,V_excitation): # Note beta is different for each x, y, z direction
    t1 = (4*math.pi)/(constants.electron_mass*constants.speed_of_light*constants.speed_of_light)
    t2 = (eDensity*charge*charge)/(beta*beta)
    t3 = (constants.elementary_charge*constants.elementary_charge)/(4*math.pi*constants.epsilon_0)
    ln = np.log((2*constants.electron_mass*constants.speed_of_light*constants.speed_of_light*beta*beta)/(V_excitation*(1-beta*beta)))
    t4 = ln - beta*beta
    StoppingForce = -t1*t2*t3*t3*t4
    return(StoppingForce)

def NonRelativisticStoppingForce(eDensity,charge,ispeed,V_excitation):
    t1 = (4*math.pi*eDensity*charge*charge)/(constants.electron_mass*ispeed*ispeed)
    t2 = (constants.elementary_charge*constants.elementary_charge)/(4*math.pi*constants.epsilon_0)
    t3 = np.log((2*constants.electron_mass*ispeed*ispeed)/(V_excitation))
    NonRelStoppingForce = -t1*t2*t2*t3
    return(NonRelStoppingForce)

def Direction(VelocityVector):
    DirectionList = []
    for i in range(len(VelocityVector)):
        if VelocityVector[i] >= 0:
            DirectionList.append(1)
        else:
            DirectionList.append(-1)
    return(DirectionList)
    
def ForceDirectionCheck(DirectionListComponent,AccelerationComponent):
    if DirectionListComponent >= 0:
        return(AccelerationComponent)
    else: 
        return(-AccelerationComponent)

def Atmosphere(CosmicRay,RunTime):
    
    #Initialise values
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
            print('x = 0, y = 1, i =',i)
            PositionList[i].append(CosmicRay.position[i])
            VelocityList[i].append(CosmicRay.velocity[i])
            if np.abs(CosmicRay.velocity[i]) <= 2.7E6:
                AccerlerationList[i].append(CosmicRay.acceleration[i])

            else:
                if np.abs(CosmicRay.velocity[i]) >= 1E7:
                    Force = StoppingForce(2.5E25,CosmicRay.charge,beta[i],1.29E-17)
                    print('relativistic!')
                else:
                    Force = NonRelativisticStoppingForce(2.5E25,CosmicRay.charge,CosmicRay.velocity[i],1.29E-17)
                    print('Slow Boi!')

                AccelerationCalc = (Force/CosmicRay.mass)
                print(AccelerationCalc)
                CosmicRay.acceleration[i] = ForceDirectionCheck(ListofDirections[i],AccelerationCalc)
                print(CosmicRay.acceleration[i])
                AccerlerationList[i].append(CosmicRay.acceleration[i])
                CosmicRay.Velocityupdate(i,deltaT)
                print(CosmicRay.velocity)
                
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
    

Atmosphere(Proton, 0.000001)
