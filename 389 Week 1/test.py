import numpy as np
import math
import copy
from scipy import constants
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from Particle import Particle
from Particle import Charticle


proton = Charticle([0,0,0], [2.996E8,0,0], [0,0,0],'Proton', 1.67E-27, 1E-19)
print(proton.gamma())
print(proton.RelativisticKineticEnergy())
beta = (np.linalg.norm(proton.velocity)/constants.speed_of_light)
print(beta)
#stopping power equation -  this is energy loss per metre, need to find how to approximate energy loss per time step by working out distance travelled in each time step. 
dEbydx = -(((4*math.pi)/(constants.electron_mass*constants.speed_of_light*constants.speed_of_light))*
((2.5E25*proton.charge*constants.speed_of_light)/(beta*beta))*
((constants.elementary_charge*constants.elementary_charge)/(4*math.pi*constants.epsilon_0)*
(constants.elementary_charge*constants.elementary_charge)/(4*math.pi*constants.epsilon_0))*
(math.log((2*constants.elementary_charge*constants.speed_of_light*constants.speed_of_light*beta*beta)/(1.29E-17*(1-beta*beta)))-beta*beta)*
np.linalg.norm(proton.velocity))
print(constants.epsilon_0)
print(constants.electron_mass)
print(constants.elementary_charge)
print(dEbydx)
