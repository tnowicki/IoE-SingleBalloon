import requests, time
from single.SingleBalloonDeviceSettings \
 import THINGERIO_METHOD, THINGERIO_HEADERS, SLEEP_TIME
from single.BalloonDrift \
 import pickRandomPlaceOnEarth, makeMeteoDrift
from single.DataMeasurment import getMeteoData

#Single balloon settings
BALLOON_ID = 0

def run():
    """ Single balloon action """
    print("Single Balloon job running...\n Press Ctrl+C to STOP")
    balloonData = pickRandomPlaceOnEarth(BALLOON_ID)
    
    try:
        while True:
            print(balloonData)
            requests.post(
             THINGERIO_METHOD,
             json=balloonData,
             headers= THINGERIO_HEADERS)
            makeMeteoDrift(balloonData)
            time.sleep(SLEEP_TIME)
            getMeteoData(balloonData)
    except KeyboardInterrupt:
        print("\nSingle Balloon job STOPPED")