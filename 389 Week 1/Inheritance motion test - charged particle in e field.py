import numpy as np
import math
import copy
from scipy import constants
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from Particle import Particle
from Particle import Charticle



proton = Charticle([0,0,0], [1E6,1E6,0], [0,0,0],'Proton', 1.67E-27, 1E-19)
EField = np.array([0,0.0001,0])
BField = np.array([0,0.0001,0])

def zoomer(ChargedObject,runtime,deltaT):
    t = 0
    xpos = []
    ypos = []
    zpos = []
    for _ in np.arange (0,runtime,deltaT):
        
        ChargedObject.acceleration = (ChargedObject.charge*EField + ChargedObject.charge*(np.cross(ChargedObject.velocity,BField)))/ChargedObject.mass
        ChargedObject.update(deltaT)
        #print('chime = ',t, 'chosition = ',ChargedObject.position, 'chelocity= ',ChargedObject.velocity, 'chacceleration = ',ChargedObject.acceleration)
        t += deltaT
        xpos.append(ChargedObject.position[0])
        ypos.append(ChargedObject.position[1])
        zpos.append(ChargedObject.position[2])
        
    
    ax = plt.axes(projection='3d')
    ax.set_xlabel('X Position [m]')
    ax.set_ylabel('Z Position [m]')
    ax.set_zlabel('Y Position [m]')
    ax.plot3D(xpos ,zpos,ypos)
    plt.show()


#zoomer(proton,0.01,0.000001)


def Atmosphere(cray, eDensity, runtime, deltaT):
    t = 0.0
    cray.gamma()
    Ecray = cray.RelativisticKineticEnergy()
    pos = [[],[],[]]
    
    timelist = []
    print(Ecray)
    I = 1.29E-17
    for _ in np.arange (0,runtime,deltaT):
        
        timelist.append(t)
        cray.update(deltaT)
        #eqn for beta
        beta = (np.linalg.norm(cray.velocity)/constants.speed_of_light)
        #stopping power equation -  this is energy loss per metre, need to find how to approximate energy loss per time step by working out distance travelled in each time step.
        for i in np.arange(len(cray.velocity)): 
            Poweri = -(((4*math.pi)/(constants.electron_mass*constants.speed_of_light*constants.speed_of_light))*
            ((eDensity*cray.charge*constants.speed_of_light)/(beta*beta))*
            ((constants.elementary_charge*constants.elementary_charge)/(4*math.pi*constants.epsilon_0)*
            (constants.elementary_charge*constants.elementary_charge)/(4*math.pi*constants.epsilon_0))*
            (math.log((2*constants.elementary_charge*constants.speed_of_light*constants.speed_of_light*beta*beta)/(I*(1-beta*beta)))-beta*beta)*
            cray.velocity[i])

            if cray.velocity[i] == 0:
                cray.acceleration[i] = 0
            else:
                cray.acceleration[i] = (Poweri/(cray.mass*cray.velocity[i])) 

            cray.update(deltaT)
            Ecray = cray.RelativisticKineticEnergy()
            t += deltaT

        
            if cray.velocity[i] >= 0: 
                pos[i].append(cray.position[i])
                
            else:
                pos[i].append(cray.position[i-1])

    
    ax = plt.axes(projection='3d')
    ax.set_xlabel('X Position [m]')
    ax.set_ylabel('Z Position [m]')
    ax.set_zlabel('Y Position [m]')
    #ax.set_zlabel('time [s]')
    #ax.plot3D(xpos,zpos,timelist)
    ax.scatter3D(pos[0] ,pos[2],pos[1])
    plt.show()

    


Atmosphere(proton,2.5E25,0.1,0.01)

