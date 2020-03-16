import numpy as np
import pandas as pd
import math
import copy
import random
from scipy import constants
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from RunSimulationSupportingFunctions import DataRead, DataFrameShow, TrajectoryPlot, DecelerationPlot, EnergyLossPlot
from AtmosphereFinal import Atmosphere


NumberofParticles = int(input('How many Cosmic Rays would you like?\n')) # Simulation Runs entirely from this file now!
InteractionOnOff = str(input('Would you like: \n - Non-Interacting Primary Cosmic Rays? [Input N] \n - Interacting Cosmic Rays [Input I] \n'))
if InteractionOnOff == 'I' or InteractionOnOff == 'i':
    SaveDetail = 'Interacting'
else:
    SaveDetail = 'Non_Interacting'
dataframelist = []

Atmosphere(0.000184, NumberofParticles, InteractionOnOff)
DataRead(NumberofParticles,dataframelist)
DataFrameShow(dataframelist)
TrajectoryPlot(dataframelist, NumberofParticles, SaveDetail)
DecelerationPlot(dataframelist, NumberofParticles, SaveDetail)
EnergyLossPlot(dataframelist, NumberofParticles, SaveDetail)


