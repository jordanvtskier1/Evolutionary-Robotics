import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p


class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        #self.Prepare_To_Act()


    def Set_Value(self,robot,desiredAngle):
        pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = self.jointName, controlMode = p.POSITION_CONTROL, targetPosition = desiredAngle, maxForce = 100)

    """
    def Prepare_To_Act(self): #, amplitude, frequency, offset
        if self.jointName == b'Torso_Backleg':
            self.amplitude = np.pi/3    #amplitude
            self.frequency = 8  #frequency
            self.offset = 0   #offset
        else:
            self.amplitude = np.pi/3    #amplitude
            self.frequency = 4  #frequency
            self.offset = 0   #offset
        
        targetAngles =  np.sin(np.linspace(0, 2*np.pi,1000))

        self.motorValues = self.amplitude * np.sin(self.frequency * targetAngles + self.offset)    
        """
  
    """
    def Save_Values(self):
        np.save(f"data/{self.jointName}targetAnglesData",self.motorValues)"""
