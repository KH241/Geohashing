# Geohashing
Yet another implementation of [Geohashing](https://geohashing.site/geohashing/Main_Page)

It calculates a position and then opens google maps on your browser (with the position).

# Configuration
In the file  `config.py`, you need to change the following:
 * latitude - to your latitude
 * longitude - to your longitude

You can also change these if you want
 * decimal_start - defines when the program will start filling the coordinates with hashnumbers (it starts at 0)
 * decimal_places - defines how precise your coordinates will be
 * api_request - the link your browser will open (important: `{0}` is the latitude and `{1}` is the longitude)
