#Device specyfic settings, See: Device->Callback->Overview

THINGERIO_METHOD = "https://backend.thinger.io/v3/users/tjnowicki/devices/\
SingleBalloon/callback/data"

AUTHORIZATION_HEADER = "Bearer \
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJEZXZpY2VDYWxsYmFja1\
9TaW5nbGVCYWxsb29uIiwic3ZyIjoiZXUtY2VudHJhbC5hd3MudGhpbmdlci5pbyIs\
InVzciI6InRqbm93aWNraSJ9.4Ndm9u75MCbYiXzU-_wwEVvUHndtj-eJ0vy01tvhLv0"

THINGERIO_HEADERS = {
  "Content-Type": "application/json;charset=UTF-8",
  "Authorization": AUTHORIZATION_HEADER,
  "Accept": "application/json, text/plain, */*"
}

#
SLEEP_TIME = 10
