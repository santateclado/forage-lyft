from abc import ABC, abstractmethod


class Engine(ABC):
    """Abstract class for an engine"""
    def __init__ (self, last_service_date):
        self._last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        """Determines if the engine needs service."""
        pass