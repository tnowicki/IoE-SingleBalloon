import random
from single.BalloonData import *
from single.DataMeasurment import getMeteoData

from math import sin, cos, radians
from single.SingleBalloonDeviceSettings import SLEEP_TIME

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
    

D = 111*1000 #[m]
A = 100

def makeMeteoDrift(balloonData):
    """ Change position acc. to local wind """
    #Wind angle in radians
    theta = radians(balloonData[WIND_DIRECTION])
    #Wind speed components
    vLat = - balloonData[WIND_SPEED] * cos(theta) #[m/s]
    vLon = - balloonData[WIND_SPEED] * sin(theta) #[m/s]
    #Wind drift components
    dLatDist = A * vLat * SLEEP_TIME #[m]
    dLonDist = A * vLon * SLEEP_TIME #[m]
    #Geographic coordinates change
    d = D * cos(balloonData[LATITUDE])
    dLatJump = dLatDist/d if d!=0 else random(-1,1)    
    dLonJump =  dLonDist / D
    #
    balloonData[LATITUDE] = newLatitude(
     current=balloonData[LATITUDE],
     jump=dLatJump)
    balloonData[LONGITUDE] = newLongitude(
     current=balloonData[LONGITUDE],
     jump=dLonJump)