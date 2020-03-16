import numpy as np
import pandas as pd
import math
import copy
from scipy import constants

from CosmicRayClass import CosmicRay

def BunchFunction(NumberofParticles):
    PList = []
    for i in range(1,NumberofParticles+1):
        theta = 2*math.pi*(i/NumberofParticles)
        Proton = CosmicRay([0,8E4,0], [0.4*constants.speed_of_light*np.cos(theta), -(0.43 + (0.48*i)/NumberofParticles)*constants.speed_of_light, 0.4*constants.speed_of_light*np.sin(theta)], [0,0,0],'Proton %s'%(i),constants.proton_mass, constants.proton_mass, 1, 0, 1.0) # 80E4 is top of mesosphere, cosmic ray speed range 0.43c - 0.996c
        PList.append(Proton)
    return(PList)

def Direction(VelocityVector):
    DirectionList = []
    for i in range(len(VelocityVector)):
        if VelocityVector[i] >= 0:
            DirectionList.append(1)
        else:
            DirectionList.append(-1)
    return(DirectionList)
    
def Interacted(InteractionValue):
    if InteractionValue >= 50:
        Interacted = 'Yes'
    else:
        Interacted = 'No'
    return(Interacted)