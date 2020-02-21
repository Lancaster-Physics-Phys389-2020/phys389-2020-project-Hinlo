import numpy as np
import math
import copy
from scipy import constants
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from Particle import Particle
from Particle import Charticle



proton = Charticle([0,0,0], [1E8,0,0], [0,0,0],'Proton', constants.proton_mass, constants.elementary_charge)
EField = np.array([0,1,0])
BField = np.array([0,1,0])

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


#zoomer(proton,100,0.001)


def Atmosphere(cray, eDensity, runtime, deltaT):
    t = 0
    Ecray = cray.KineticEnergy()
    xpos = []
    ypos = []
    zpos = []
    I = 1.29E-17
    for _ in np.arange (0,runtime,deltaT):
        
        
        cray.update(deltaT)
        #eqn for beta
        beta = (np.linalg.norm(cray.velocity)/constants.speed_of_light)
        #stopping power equation -  this is energy loss per metre, need to find how to approximate energy loss per time step by working out distance travelled in each time step. 
        dEbydx = -(((4*math.pi)/constants.electron_mass*constants.speed_of_light*constants.speed_of_light)*
        ((eDensity*cray.charge*constants.speed_of_light)/(beta*beta))*
        ((constants.elementary_charge*constants.elementary_charge)/(4*math.pi*constants.epsilon_0)*
        (constants.elementary_charge*constants.elementary_charge)/(4*math.pi*constants.epsilon_0))*
        (math.log((2*constants.elementary_charge*constants.speed_of_light*constants.speed_of_light*beta*beta)/(I*(1-beta*beta)))-beta*beta))

        t += deltaT
        Ecray += dEbydx
        print(Ecray)
        if Ecray >= 0:
            xpos.append(cray.position[0])
            ypos.append(cray.position[1])
            zpos.append(cray.position[2])
        else:
            break

    
    ax = plt.axes(projection='3d')
    ax.set_xlabel('X Position [m]')
    ax.set_ylabel('Z Position [m]')
    ax.set_zlabel('Y Position [m]')
    ax.plot3D(xpos ,zpos,ypos)
    plt.show()

    


Atmosphere(proton,2.5E25,1,0.0001)