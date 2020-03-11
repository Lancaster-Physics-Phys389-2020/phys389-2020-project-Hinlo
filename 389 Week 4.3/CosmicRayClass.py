import numpy as np
import math
import copy
from scipy import constants
from Particle import Particle, Charticle
from CosmicRaySupportFunctions import StoppingForce, NonRelativisticStoppingForce, ForceDirectionCheck

 

class CosmicRay(Charticle):
    """
    Class to give update cosmic ray parameters and introduce decay probability
    

    Charge in multiples of e, the electron charge magnitude.
    """

    def __init__(self, Position=np.array([0,0,0], dtype=float), Velocity=np.array([0,0,0], dtype=float), Acceleration=np.array([0,0,0], dtype=float), Name='Particle Name', Mass=1.0, Charge = 1.0):
        
        super().__init__(Position=Position, Velocity=Velocity, Acceleration=Acceleration, Name=Name, Mass=Mass, Charge = Charge)

        
    def __repr__(self):
        return 'Cosmic Ray: %s, Mass: %s, Charge: %s, Position: %s, Velocity: %s, Acceleration: %s' %(self.Name, self.mass, self.charge, self.position, self.velocity, self.acceleration)

    def CosmicRayUpdate(self, deltaT, PositionList, VelocityList, AccelerationList, ListofDirections):
        beta = self.beta()
        for i in range(len(self.velocity)):
                PositionList[i].append(self.position[i])
                VelocityList[i].append(self.velocity[i])
                if np.abs(self.velocity[i]) <= 2.74E6: # minimum speed before bethe stopping power eqn breaks due to -ve ln.
                    AccelerationList[i].append(self.acceleration[i])

                else:
                    if np.abs(self.velocity[i]) >= 1E7:
                        Force = StoppingForce(5.3E25,self.charge,beta[i],1.36E-17) # using stratosphere eDensity for now.                 
                    else:
                        Force = NonRelativisticStoppingForce(5.3E25,self.charge,self.velocity[i],1.36E-17) # using stratosphere eDensity for now.                    

                    AccelerationCalc = (Force/self.mass)
                    self.acceleration[i] = ForceDirectionCheck(ListofDirections[i],AccelerationCalc)                
                    AccelerationList[i].append(self.acceleration[i])
                    self.Velocityupdate(i,deltaT)
                    
                    if ListofDirections[i] == 1 and self.velocity[i] < 0:
                        self.velocity[i] = 0
                        self.acceleration[i] = 0 
                        self.Positionupdate(i,deltaT)
                    elif ListofDirections[i] == -1 and self.velocity[i] > 0:
                        self.velocity[i] = 0
                        self.acceleration[i] = 0 
                        self.Positionupdate(i,deltaT)
                    else:
                        self.Positionupdate(i,deltaT)
