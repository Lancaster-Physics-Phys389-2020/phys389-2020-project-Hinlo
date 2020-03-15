import numpy as np
import pandas as pd
import math
import copy
from scipy import constants
from pytest import approx

from Particle import Particle
from Particle import Charticle
from AtmosphereSupportFunctions import BunchFunction, Direction
from CosmicRaySupportFunctions import StoppingForce, NonRelativisticStoppingForce, ForceDirectionCheck
from AtmosphereFinal import Atmosphere

# To test: do pytest for each function in AtmosphereFinal, small tests to assert that each gives the expected value. With atmosphere function, calculate/find a database with the values we expect after the first time step of in the data frame, assert that these correct values equal those of the dataframe given by python.
# To initialise test: open terminal: view -> Terminal, once terminal loads, type in pytest, this runs pytest across all files in the folder. Currently not running my test. Fix this.
TestProton = Charticle([0,8E4,0], [0.6*constants.speed_of_light,-0.7*constants.speed_of_light,0], [0,0,0],'Proton', 1.67E-27, 1)
StationaryProton = Charticle([0,8E4,0], [0,0,0], [0,0,0],'Proton', 1.67E-27, 1)




def test_Stoppingforce(): # check that relativistic stopping force gives correct value for a given input
    assert StoppingForce(5.3E25,1,0.9,1.36E-17)*1E15 == approx(-5.33, rel = 0.01) # Multiply by 1e15 as approx only has accuracy of 1E-12

def test_NonRelativisticStoppingforce(): # check that non-relativistic stopping force gives correct value for a given input
    assert NonRelativisticStoppingForce(5.3E25,1,5E6,1.36E-17)*1E12 == approx(-1.87, rel = 0.01) # Multiply by 1e15 as approx only has accuracy of 1E-12

def test_Direction (): # check that particles direction is correctly identified
    assert Direction(TestProton.velocity) == [1,-1,1]

def test_ForceDirectionCheck(): # check that forcedirection is only switched if particle moves in the negative direction along a given axis
    assert ForceDirectionCheck(1,1) == 1
    assert ForceDirectionCheck(-1,1) == -1



