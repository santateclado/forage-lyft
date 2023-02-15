from serviceable import Serviceable

class Car(Serviceable):
    """Abstract class for a car."""""

    def __init__(self, engine, battery):
        self._engine = engine
        self._battery = battery
    
    def needs_service(self):
        """Determines if the car needs service."""
        return self._engine.needs_service() or self._battery.needs_service()
