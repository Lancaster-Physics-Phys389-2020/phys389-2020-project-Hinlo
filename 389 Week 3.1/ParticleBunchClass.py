import numpy as np
import math
import copy
from scipy import constants
from Particle import Charticle

class ParticleBunch(Charticle): #needs to inherit charticle - maybe just use list for bunch...

    
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
            
            
    def BunchFunction(self, NumberofParticles):
        self.PList = []
        for i in range(NumberofParticles):
            self.Proton = Charticle([0,8E4,0], [(0.1 + (0.5*i)/NumberofParticles)*constants.speed_of_light,-(0.43 + (0.556*i)/NumberofParticles)*constants.speed_of_light,0], [0,0,0],'Proton %s'%(i), 1.67E-27, 1) # 80E4 is top of mesosphere, cosmic ray speed range 0.43c - 0.996c
            self.PList.append(self.Proton)
        return(self.PList)
        


    