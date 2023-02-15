from abc import ABC, abstractmethod


class Engine(ABC):
    """Abstract class for an engine"""

    @abstractmethod
    def needs_service(self):
        """Determines if the engine needs service."""
        pass