from cmath import phase
from math import pi
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import constants as c
from simulation import SIMULATION


simulation = SIMULATION()
simulation.Run()
del simulation
