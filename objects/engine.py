from abc import ABC, abstractmethod
from objects.serviceable import Serviceable


class Engine(Serviceable, ABC):
    """Abstract class for an engine"""

    @abstractmethod
    def needs_service(self):
        """Determines if the engine needs service."""
        pass
