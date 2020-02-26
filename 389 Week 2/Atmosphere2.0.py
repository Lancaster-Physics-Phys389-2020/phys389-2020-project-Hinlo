import numpy as np
import math
import copy
from scipy import constants
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from Particle import Particle
from Particle import Charticle



proton = Charticle([0,0,0], [0,1E8,0], [0,0,0],'Proton', 1.67E-27, 1)



def Atmosphere(cray, eDensity, runtime):
    #set initial values
    t = 0.0
    deltaT = 0.01*runtime
    beta = cray.beta()
    print(cray.gamma())
    cray.gamma()
    Ecray = cray.RelativisticKineticEnergy()
    
    

    pos = [[],[],[]]  
    timelist = []
    yvelocitylist = []

    direction = []
    for i in range(len(cray.velocity)): # create a list which defines direction in xyz planes - +1 is +ve direction, -1 is -ve direction
        if cray.velocity[i] >= 0:
            direction.append(1)
        else:
            direction.append(-1)
    #print(direction)

    I = 1.29E-17 #define mean excitation potential of air





    for _ in np.arange (0,runtime,deltaT): #run simulation over runtime
        
        
        yvelocitylist.append(cray.velocity[1])
        timelist.append(t) 
        print('Position =', cray.position, 'Velocity = ', cray.velocity, 'Acceleration =', cray.acceleration, 'Kinetic Energy =', Ecray)
        
        
        #stopping power equation -  this is energy loss per metre, need to find how to approximate energy loss per time step by working out distance travelled in each time step.
        for i in range(len(cray.velocity)):

            
            
            
            if cray.velocity[i] == 0: #check if velocity component is zero, if so particle stationary in that axis
                cray.acceleration[i] = 0 #so set acceleration in that axis to zero
                pos[i].append(cray.position[i]) # and append the position
            
            else:
                Forcei = -(((4*math.pi)/(constants.electron_mass*constants.speed_of_light*constants.speed_of_light))*
                ((eDensity*cray.charge*cray.charge)/(beta[i]*beta[i]))*
                ((constants.elementary_charge*constants.elementary_charge)/(4*math.pi*constants.epsilon_0)*
                (constants.elementary_charge*constants.elementary_charge)/(4*math.pi*constants.epsilon_0))*
                (math.log((2*constants.electron_mass*constants.speed_of_light*constants.speed_of_light*beta[i]*beta[i])/(I*(1-beta[i]*beta[i])))-beta[i]*beta[i]))

            
                if direction[i] == 1: #defining stopping power and deceleration for +ve motion in i direction
                    
                    cray.acceleration[i] = (Forcei/(cray.mass)) #otherwise update acceleration accordingly
                    cray.update(deltaT) # update velocity and position
                    if cray.velocity[i] < 0:    #check if velocity has changed direction, if so it has been stopped so set velocity and acceleration to zero, stop updating position in that axis
                        cray.velocity[i] = 0
                        cray.acceleration[i] = 0
                        pos[i].append(pos[i][int(t/deltaT)-1]) #this works as long as the particle doesn't stop after one time step - if it does, this will try to index [0-1]
                    else:
                        pos[i].append(cray.position[i]) #if direction hasn't changed, particle hasn't been stopped yet, keep updating values.

                if direction[i] == -1: #defining stopping power and deceleration for -ve motion in i direction 
                    NegativeForcei = -Forcei

                    if cray.velocity[i] == 0: 
                        cray.acceleration[i] = 0
                    else:
                        cray.acceleration[i] = (NegativeForcei/(cray.mass))

                    cray.update(deltaT)
                    if cray.velocity[i] > 0:    
                        cray.velocity[i] = 0
                        cray.acceleration[i] = 0
                        pos[i].append(pos[i][int(t/deltaT)-1])
                    else:
                        pos[i].append(cray.position[i])
                print(Forcei)
        beta = cray.beta()
        print(beta)
        cray.gamma()
        Ecray = cray.RelativisticKineticEnergy()
        
        t += deltaT 
        

            
            
        

    #print(pos)
    ax = plt.axes(projection='3d')
    ax.plot3D(pos[0],pos[1],pos[2])
    ax.set_xlabel('X Position [m]')
    ax.set_ylabel('Y Position [m]')
    ax.set_zlabel('Z Position [m]')
    plt.show()
    
    
    #print(yvelocitylist)
    #print(timelist)
    plt.plot(timelist, yvelocitylist)
    plt.xlabel('Time [s]')
    plt.ylabel('Y-Velocity [m/s]')
    plt.show()

    


Atmosphere(proton,2.5E25,0.00001)

