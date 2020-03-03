import numpy as np
import pandas as pd
import math
import copy
from scipy import constants

from Particle import Particle
from Particle import Charticle
from AtmosphereFinal import StoppingForce, Direction, ForceDirectionCheck, Atmosphere


# To test: do pytest for each function in AtmosphereFinal, small tests to assert that each gives the expected value. With atmosphere function, calculate/find a database with the values we expect after the first time step of in the data frame, assert that these correct values equal those of the dataframe given by python.
# To initialise test: open terminal: view -> Terminal, once terminal loads, type in pytest, this runs pytest across all files in the folder. Currently not running my test. Fix this.
TestProton = Charticle([0,2.5E4,0], [2.3E7,-2.5E7,0], [0,0,0],'Proton', 1.67E-27, 1)





# def test_Stoppingforce():
#     assert

def test_Direction ():
    assert Direction(TestProton.velocity) == [1,-1,1]

def test_ForceDirectionCheck():
    assert ForceDirectionCheck(1,1) == 1
    assert ForceDirectionCheck(-1,1) == -1

# def test_Atmosphere():
#     assert Atmosphere(TestProton, 


