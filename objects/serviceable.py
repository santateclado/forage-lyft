from abc import ABC, abstractmethod


class Serviceable(ABC):
    """Abstract class for a serviceable object."""

    @abstractmethod
    def needs_service(self):
        """Determines if the object needs service."""
        pass
