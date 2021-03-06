import numpy as np
import math
import copy
from scipy import constants

class Particle:
    """
    Class to model a Massive particle in a vacuum. Particle moves downward at constant speed 
    It will make use of numpy arrays to store the Position Velocity etc. 
     

    Mass in kg 
    Position and Velocity in m/s 
    """

    def __init__(self, Position=np.array([0,0,0], dtype=float), Velocity=np.array([0,0,0], dtype=float), Acceleration=np.array([0,0,0], dtype=float), Name='Roger', Mass=1.0):
        self.Name = Name
        self.position = np.array(Position,dtype=float)
        self.velocity = np.array(Velocity,dtype=float)
        self.acceleration = np.array(Acceleration,dtype=float)
        self.mass = Mass

    def __repr__(self):
        return 'Particle: %s, Mass: %s, Position: %s, Velocity: %s, Acceleration: %s'%(self.Name,self.mass,self.position, self.velocity,self.acceleration)

    def KineticEnergy(self):
        return 0.5*self.mass*np.vdot(self.velocity,self.velocity)

    def beta(self):
        return ((self.velocity)/constants.speed_of_light)

    def gamma(self):
        return (1/(math.sqrt(1 - np.linalg.norm(Particle.beta(self))*np.linalg.norm(Particle.beta(self)))))

    def RelativisticKineticEnergy(self):
        return ((Particle.gamma(self)-1.0)*self.mass*constants.speed_of_light*constants.speed_of_light)
  
    def momentum(self):
        return self.mass*np.array(self.velocity,dtype=float)

    def update(self,index,deltaT):
        self.velocity[index] +=  self.acceleration[index]*deltaT
        self.position[index] +=  self.velocity[index]*deltaT

    def Velocityupdate(self,index,deltaT):
        self.velocity[index] +=  self.acceleration[index]*deltaT

    def Positionupdate(self,index,deltaT):
        self.position[index] +=  self.velocity[index]*deltaT
        
        

class Charticle(Particle):
    """
    Class to give charge parameter to particles. Currently set to give a proton e.g charge = 1.0
    

    Charge in multiples of e, the electron charge magnitude.
    """

    def __init__(self, Position=np.array([0,0,0], dtype=float), Velocity=np.array([0,0,0], dtype=float), Acceleration=np.array([0,0,0], dtype=float), Name='Particle Name', Mass=1.0, Charge = 1.0):
        
        super().__init__(Position=Position, Velocity=Velocity, Acceleration=Acceleration, Name=Name, Mass=Mass)

        self.charge = Charge
    def __repr__(self):
        return 'Charged Particle: %s, Mass: %s, Charge: %s, Position: %s, Velocity: %s, Acceleration: %s' %(self.Name, self.mass, self.charge, self.position, self.velocity, self.acceleration)




