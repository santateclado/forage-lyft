from abc import ABC, abstractmethod

class Car(ABC):
    """Abstract class for a car."""""

    def __init__(self, engine, battery):
        self._engine = engine
        self._battery = battery

    @abstractmethod
    def needs_service(self):
        """Determines if the car needs service."""
        
