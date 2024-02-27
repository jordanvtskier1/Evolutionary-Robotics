from cmath import phase
from math import pi
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random

from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self):
        
        
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
        p.setGravity(0,0,-9.8)
        
        self.world = WORLD()
        self.robot = ROBOT()
        

        

        
    def Run(self):
                
        for _ in range(1000):
            p.stepSimulation()
            self.robot.Sense(_)
            self.robot.Act(_)
            
    
            time.sleep(1/10)
            print(_)
           
    def __del__(self):
        self.robot.Save_Values()    
        p.disconnect()    
   