from cmath import phase
from math import pi
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
from constants import numberOfTimeSteps

from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self, directOrGUI):
        
        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
            self.GUI = False
        else:
            self.physicsClient = p.connect(p.GUI)
            self.GUI = True
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
        p.setGravity(0,0,-9.8)
        
        self.world = WORLD()
        self.robot = ROBOT()
        

    def Run(self):
                
        for _ in range(numberOfTimeSteps):
            p.stepSimulation()
            self.robot.Sense(_)
            self.robot.Think(_)
            self.robot.Act()

            if self.GUI == True:
                time.sleep(1/540)
            #print(_)
            
    def Get_Fitness(self):
        self.robot.Get_Fitness()
           
    def __del__(self):
        #self.robot.Save_Values()    
        p.disconnect()
   