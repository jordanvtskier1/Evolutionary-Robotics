import numpy as np
import matplotlib.pyplot

backLegSensorValues = np.load("data/backLegData.npy")
frontLegSensorValues = np.load("data/frontLegData.npy")

matplotlib.pyplot.plot(backLegSensorValues, linewidth = 4, label = "Back Leg")
matplotlib.pyplot.plot(frontLegSensorValues, label = "Front Leg")

matplotlib.pyplot.legend()
matplotlib.pyplot.show()