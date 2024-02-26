from cmath import phase
from math import pi
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random


physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

amplitudeBackLeg = np.pi/3
frequencyBackLeg = 8
phaseOffsetBackLeg = np.pi/8

amplitudeFrontLeg = np.pi/3
frequencyFrontLeg = 8
phaseOffsetFrontLeg = -np.pi/8

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

targetAngles =  np.sin(np.linspace(0, 2*np.pi,1000))

#targetAngles = (np.pi / 4) * targetAngles


motorCommandBackLeg = amplitudeBackLeg * np.sin(frequencyBackLeg * targetAngles + phaseOffsetBackLeg)
motorCommandFrontLeg = amplitudeFrontLeg * np.sin(frequencyFrontLeg * targetAngles + phaseOffsetFrontLeg)

np.save("data/targetAnglesData",targetAngles)


#exit()
for _ in range(1000):
    p.stepSimulation()
    backLegSensorValues[_] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
    frontLegSensorValues[_] = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")
    
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_Backleg', controlMode = p.POSITION_CONTROL, targetPosition = motorCommandBackLeg[_], maxForce = 100)
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_Frontleg', controlMode = p.POSITION_CONTROL, targetPosition = motorCommandFrontLeg[_], maxForce = 100)

    
    time.sleep(1/240)
    print(_)
np.save("data/frontLegData",frontLegSensorValues)
np.save("data/backLegData",backLegSensorValues)
p.disconnect()


