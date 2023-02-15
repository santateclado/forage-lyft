from datetime import timedelta, datetime
from objects.battery import Battery


class NubbinBattery(Battery):
    """A class represeting a Nubbin battery"""

    def __init__(self, last_service_date):
        super().__init__(last_service_date)
        self._last_service_date = last_service_date

    def needs_service(self):
        """Determines if this battery needs service. 
        Returns True if the battery needs service, False otherwise"""
        result = False
        next_service_date = self._last_service_date + timedelta(years=4)
        if datetime.today().date() >= next_service_date:
            result = True
        return result
