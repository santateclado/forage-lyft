from abc import ABC
from datetime import datetime, timedelta
from objects.serviceable import Serviceable


class Battery(Serviceable, ABC):
    """Abstract class for a battery"""

    def __init__(self, last_service_date, service_interval):
        self._last_service_date = last_service_date
        self._service_interval = service_interval

    def needs_service(self):
        """Determines if this battery needs service. 
        Returns True if the battery needs service, False otherwise"""
        result = False
        next_service_date = self._last_service_date + timedelta(years=self._service_interval)
        if datetime.today().date() >= next_service_date:
            result = True
        return result
