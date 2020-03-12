import numpy as np
import math
import copy
import random
import time
from scipy import constants
from Particle import Particle, Charticle
from CosmicRaySupportFunctions import StoppingForce, NonRelativisticStoppingForce, ForceDirectionCheck

 

class CosmicRay(Charticle):
    """
    Class to give update cosmic ray parameters and introduce decay probability
    

    Charge in multiples of e, the electron charge magnitude.
    """

    def __init__(self, Position=np.array([0,0,0], dtype=float), Velocity=np.array([0,0,0], dtype=float), Acceleration=np.array([0,0,0], dtype=float), Name='Particle Name', Mass=1.0, Charge = 1.0, Interact = 0):
        
        super().__init__(Position=Position, Velocity=Velocity, Acceleration=Acceleration, Name=Name, Mass=Mass, Charge = Charge)
        self.interact= Interact
        
    def __repr__(self):
        return 'Cosmic Ray: %s, Mass: %s, Charge: %s, Position: %s, Velocity: %s, Acceleration: %s, Interact: %s' %(self.Name, self.mass, self.charge, self.position, self.velocity, self.acceleration, self.interact)

    def CosmicRayUpdate(self, deltaT, PositionList, VelocityList, AccelerationList, ListofDirections):
        beta = self.beta()
        for i in range(len(self.velocity)):
                PositionList[i].append(self.position[i])
                VelocityList[i].append(self.velocity[i])
                if np.abs(self.velocity[i]) <= 2.74E6: # minimum speed before bethe stopping power eqn breaks due to -ve ln.
                    AccelerationList[i].append(self.acceleration[i])
                    self.velocity[i] = 0
                    self.acceleration[i] = 0

                else:
                    if np.abs(self.velocity[i]) >= 1E7:
                        Force = StoppingForce(1.67E25,self.charge,beta[i],1.36E-17) # using mesosphere eDensity for now.                 
                    else:
                        Force = NonRelativisticStoppingForce(1.67E25,self.charge,self.velocity[i],1.36E-17) # using mesosphere eDensity for now.                    

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




    def CosmicRayInteractionUpdate(self, deltaT, PositionList, VelocityList, AccelerationList, ListofDirections):
        beta = self.beta()
        
        

        if self.interact >= 70:
            
            for i in range(len(self.velocity)):
                PositionList[i].append(self.position[i])
                VelocityList[i].append(self.velocity[i])
                AccelerationList[i].append(self.acceleration[i])
                
                
        else:    
            for i in range(len(self.velocity)):
                self.interact = round(random.randint(0,100)*np.abs(self.velocity[i]))/(0.708*constants.speed_of_light)
                # print('Interaction has value %s'%(self.interact))

                # if self.interact != 0:
                #     time.sleep(0.1)
                if self.interact >= 70:
                    # print('OMG Interaction!')
                    for j in range(3-i):
                        PositionList[2-j].append(self.position[2-j])
                        VelocityList[2-j].append(self.velocity[2-j])
                        AccelerationList[2-j].append(self.acceleration[2-j])
                    break
                else:
                    PositionList[i].append(self.position[i])
                    VelocityList[i].append(self.velocity[i])

                    if np.abs(self.velocity[i]) <= 2.74E6: # minimum speed before bethe stopping power eqn breaks due to -ve ln.
                        AccelerationList[i].append(self.acceleration[i])
                        self.velocity[i] = 0
                        self.acceleration[i] = 0
                
                    else:
                        if np.abs(self.velocity[i]) >= 1E7:
                            Force = StoppingForce(1.67E25,self.charge,beta[i],1.36E-17) # using mesosphere eDensity for now.                 
                        else:
                            Force = NonRelativisticStoppingForce(1.67E25,self.charge,self.velocity[i],1.36E-17) # using mesosphere eDensity for now.                    

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

    # def InteractionCheck(self,Interact):
    #     if Interact
       