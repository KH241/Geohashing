from datetime import datetime

import config
import hashlib


class Generator(object):
    def __init__(self):
        self.latitude = config.latitude
        self.longitude = config.longitude

    def getHash(self):
        # instead of Dow Jones I use the time

        time = datetime.now()
        date_string = time.strftime("%Y-%m-%d-%H%M.%S")

        return str(hashlib.md5(date_string.encode()).hexdigest())

    def getCoordinates(self):
        hash_str = self.getHash()

        latitude_hash_str = hash_str[:16]
        longitude_hash_str = hash_str[16:]

        latitude_decimal = str(int(longitude_hash_str, base=16))
        longitude_decimal = str(int(latitude_hash_str, base=16))

        latitude_split = str(self.latitude).split(".")
        longitude_split = str(self.longitude).split(".")

        latitude  = latitude_split[0] + "." + latitude_split[1][:config.decimal_start]
        longitude = longitude_split[0] + "." + longitude_split[1][:config.decimal_start]

        latitude += latitude_decimal[config.decimal_start:config.decimal_places]
        longitude += longitude_decimal[config.decimal_start:config.decimal_places]

        return latitude, longitude
