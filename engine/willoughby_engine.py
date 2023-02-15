from objects.engine import Engine


class WilloughbyEngine(Engine):
    """A class representing a Willoughby engine"""

    def __init__(self, last_service_mileage, current_mileage):
        super().__init__(last_service_mileage)
        self._last_service_mileage = last_service_mileage
        self._service_interval = 60000
        self._current_mileage = current_mileage

    def needs_service(self):
        """Determines if this engine needs service."""
        result = False
        if (self._current_mileage % self._service_interval) == 0:
            self._last_service_mileage = self._current_mileage
            result = True
        return result
