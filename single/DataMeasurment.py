import random
from single.BalloonData import *


def getRandomData(balloonData):
  """ Changes values in the JSON to random integers """

  balloonData[TEMPERATURE] = \
   random.randint(TEMERATURE_MIN, TEMPERATURE_MAX)

  balloonData[HUMIDITY] = \
   random.randint(HUMIDITY_MIN, HUMIDITY_MAX)

  balloonData[WIND_SPEED] = \
   random.randint(WIND_SPEED_MIN, WIND_SPEED_MAX)

  balloonData[WIND_DIRECTION] = \
   random.randint(WIND_DIRECTION_MIN, WIND_DIRECTION_MAX)

def getMeteoData(balloonData):
  getRandomData(balloonData)
