import numpy as np
import matplotlib.pyplot

#backLegSensorValues = np.load("data/backLegData.npy")
#frontLegSensorValues = np.load("data/frontLegData.npy")

targetAngles = np.load("data/targetAnglesData.npy")

matplotlib.pyplot.plot(targetAngles)

#matplotlib.pyplot.plot(backLegSensorValues, linewidth = 4, label = "Back Leg")
#matplotlib.pyplot.plot(frontLegSensorValues, label = "Front Leg")

#matplotlib.pyplot.legend()
matplotlib.pyplot.show()