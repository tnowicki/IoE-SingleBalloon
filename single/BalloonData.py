#JSON fields used by devide
BALLOON_ID = "balloon_id"
LATITUDE = "lat" #szerokość gegraficzna
LONGITUDE = "lng" #długość geograficzna
TEMPERATURE = "temperature C"
HUMIDITY = "humidity [%]"
WIND_SPEED = "wind speed [m/s]"
WIND_DIRECTION = "wind direction"

#Data constraints
LATITUDE_MIN, LATITUDE_MAX = -90, 90
LONGITUDE_MIN, LONGITUDE_MAX = -180, 180
TEMERATURE_MIN, TEMPERATURE_MAX = -90, 60
HUMIDITY_MIN, HUMIDITY_MAX = 0, 100
WIND_SPEED_MIN, WIND_SPEED_MAX = 0, 150
WIND_DIRECTION_MIN, WIND_DIRECTION_MAX = 0, 360

#Helper functions
def newLatitude(current, jump):
    new = current + jump
    if new > LATITUDE_MAX:
        return new - LATITUDE_MAX
    elif new < LATITUDE_MIN:
        return LATITUDE_MIN - new
    else:
        return new

def newLongitude(current, jump):
    new = current + jump
    if new > LONGITUDE_MAX:
        return LONGITUDE_MIN + new - LONGITUDE_MAX
    elif new < LONGITUDE_MIN:
        return LONGITUDE_MIN - new
    else:
        return new