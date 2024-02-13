import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np


physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = np.zeros(100)
frontLegSensorValues = np.zeros(100)

for _ in range(100):
    p.stepSimulation()
    backLegSensorValues[_] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
    frontLegSensorValues[_] = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")
    time.sleep(1/60)
    print(_)
np.save("data/frontLegData",frontLegSensorValues)
np.save("data/backLegData",backLegSensorValues)
p.disconnect()


