import numpy as np
import pandas as pd
import math
import copy
from scipy import constants
from pytest import approx

from Particle import Particle
from Particle import Charticle
from AtmosphereSupportFunctions import StoppingForce,NonRelativisticStoppingForce, Direction, ForceDirectionCheck
from AtmosphereFinal import Atmosphere

# To test: do pytest for each function in AtmosphereFinal, small tests to assert that each gives the expected value. With atmosphere function, calculate/find a database with the values we expect after the first time step of in the data frame, assert that these correct values equal those of the dataframe given by python.
# To initialise test: open terminal: view -> Terminal, once terminal loads, type in pytest, this runs pytest across all files in the folder. Currently not running my test. Fix this.
TestProton = Charticle([0,2.5E4,0], [2.3E7,-2.5E7,0], [0,0,0],'Proton', 1.67E-27, 1)
StationaryProton = Charticle([0,2.5E4,0], [0,0,0], [0,0,0],'Proton', 1.67E-27, 1)




def test_Stoppingforce(): # check that relativistic stopping force gives correct value for a given input
    assert StoppingForce(2.5E25,1,0.9,1.29E-17) == approx(-2.5E-15)

def test_NonRelativisticStoppingforce(): # check that non-relativistic stopping force gives correct value for a given input
    assert NonRelativisticStoppingForce(2.5E25,1,5E6,1.29E-17) == approx(-9.2E-13)

def test_Direction (): # check that particles direction is correctly identified
    assert Direction(TestProton.velocity) == [1,-1,1]

def test_ForceDirectionCheck(): # check that forcedirection is only switched if particle moves in the negative direction along a given axis
    assert ForceDirectionCheck(1,1) == 1
    assert ForceDirectionCheck(-1,1) == -1

def test_Atmosphere(): # check particles with no initial velocity or acceleration are unchanged
    assert Atmosphere(StationaryProton, 0.001) == StationaryProton



