import random
from single.BalloonData import *
from single.DataMeasurment import getMeteoData

def pickRandomPlaceOnEarth(balloon_id):
    """ Prepares an intial ballon positin and data """
    balloonData = {
     BALLOON_ID : balloon_id,
     LATITUDE : random.randint(LATITUDE_MIN, LATITUDE_MAX),
     LONGITUDE : random.randint(LONGITUDE_MIN, LONGITUDE_MAX),
     TEMPERATURE : 0,
     HUMIDITY : 0,
     WIND_SPEED : 0,
     WIND_DIRECTION : 0
    }
    getMeteoData(balloonData)
    return balloonData

    
def makeRandomDrift(balloonData):
    """ Change position to a random neighborhood """
    drift = 15 #max drift
    balloonData[LATITUDE] = newLatitude(
     current=balloonData[LATITUDE],
     jump=random.randint(-drift,drift))
    balloonData[LONGITUDE] = newLongitude(
     current=balloonData[LONGITUDE],
     jump=random.randint(-drift,drift))
    

def makeMeteoDrift(balloonData):
    makeRandomDrift(balloonData)