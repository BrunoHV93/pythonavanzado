# Example of how to use pytz
# This is to avoid doing datetime.datetime
from datetime import datetime
# This is necessary to use different timezones
import pytz

#Example for Colombia. It´s necessary to check in the time zone data base
bogota_timezone = pytz.timezone("America/Bogota")
bogota_date =datetime.now(bogota_timezone)
print("Bogotá: ", bogota_date.strftime("%d/%m/%Y, %H:%M"))