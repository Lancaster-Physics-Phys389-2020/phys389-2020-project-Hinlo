import numpy as np
import pandas as pd
import math
import copy
from scipy import constants



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

def ForceDirectionCheck(DirectionListComponent,AccelerationComponent):
    if DirectionListComponent >= 0:
        return(AccelerationComponent)
    else: 
        return(-AccelerationComponent)

