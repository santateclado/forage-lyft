from abc import ABC, abstractmethod
from datetime import date


class Battery(ABC):
    """Abstract class for a battery"""

    def __init__(self, last_service_date):
        self._last_service_date = last_service_date
        self._current_date = date.today()

    @abstractmethod
    def needs_service(self):
        """Determines if the battery needs service. 
        Returns True if the battery needs service, False otherwise"""
        pass
