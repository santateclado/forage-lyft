from datetime import timedelta, datetime
from objects.battery import Battery


class SpindlerBattery(Battery):
    """A class representing a Spindler battery"""

    def __init__(self, last_service_date):
        super().__init__(last_service_date, timedelta(years=3))
        self._last_service_date = last_service_date
        self._service_interval = timedelta(years=3)

    def needs_service(self):
        """Determines if this battery needs service."""
        return Battery.needs_service(self)