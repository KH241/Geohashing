from datetime import datetime

import config
import hashlib


class Generator(object):
    def __init__(self):
        self.latitude = str(config.latitude).split(".")
        self.longitude = str(config.longitude).split(".")

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

        latitude = self.latitude[0] + "." + self.latitude[1][:config.decimal_start]
        longitude = self.longitude[0] + "." + self.longitude[1][:config.decimal_start]

        latitude += latitude_decimal[config.decimal_start:config.decimal_places]
        longitude += longitude_decimal[config.decimal_start:config.decimal_places]

        return latitude, longitude
