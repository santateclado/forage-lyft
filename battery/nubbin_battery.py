from datetime import timedelta
from objects.battery import Battery


class NubbinBattery(Battery):
    """A class representing a Nubbin battery"""

    def __init__(self, last_service_date):
        super().__init__(last_service_date, timedelta(years=4))
        self._last_service_date = last_service_date
        self._service_interval = timedelta(years=4)

    def needs_service(self):
        """Determines if this battery needs service. 
        Returns True if the battery needs service, False otherwise"""
        return Battery.needs_service(self)
