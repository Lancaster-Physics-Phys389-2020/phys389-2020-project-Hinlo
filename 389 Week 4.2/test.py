import numpy as np
import pandas as pd
import math
import copy
from scipy import constants

from Particle import Particle
from Particle import Charticle
from AtmosphereSupportFunctions import StoppingForce, NonRelativisticStoppingForce, Direction, ForceDirectionCheck
from ParticleBunchClass import ParticleBunch



particles = ParticleBunch.BunchFunction(10)


print(particles)




