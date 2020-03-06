import numpy as np
import math
import copy
from scipy import constants

class ParticleBunch:

    
    ListofParticles =[]
    def __init__(self, Particles):
        self.ListofParticles = Particles
        
    def __repr__(self):
        V_tot = 0
        Pnumber = 0 
        for i in range(len(self.ListofParticles)):
            V_tot  += self.ListofParticles[i].velocity
            Pnumber += 1
        V_Average = V_tot/Pnumber

        BunchDetails = ('Average Velocity = %s' %(V_Average))
        return(BunchDetails)
            
            
        


    