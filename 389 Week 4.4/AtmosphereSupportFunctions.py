import numpy as np
import pandas as pd
import math
import copy
from scipy import constants

from CosmicRayClass import CosmicRay

def BunchFunction(NumberofParticles):
    PList = []
    for i in range(NumberofParticles):
        theta = 2*math.pi*(i/NumberofParticles)
        # Proton = CosmicRay([6.6E4,8E4,6.6E4], [(-0.5 + (1*i)/NumberofParticles)*constants.speed_of_light,-(0.43 + (0.556*i)/NumberofParticles)*constants.speed_of_light,0.5*constants.speed_of_light], [0,0,0],'Proton %s'%(i+1), 1.67E-27, 1) # 80E4 is top of mesosphere, cosmic ray speed range 0.43c - 0.996c
        Proton = CosmicRay([0,8E4,0], [0.5*constants.speed_of_light*np.cos(theta), -(0.43 + (0.556*i)/NumberofParticles)*constants.speed_of_light, 0.5*constants.speed_of_light*np.sin(theta)], [0,0,0],'Proton %s'%(i+1), 1.67E-27, 1)
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
    
