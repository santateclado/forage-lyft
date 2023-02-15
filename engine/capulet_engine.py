from objects.engine import Engine


class CapuletEngine(Engine):
    """A class representing a Capulet engine"""

    def __init__(self, last_service_mileage, current_mileage):
        self._last_service_mileage = last_service_mileage
        self._service_interval = 30000
        self._current_mileage = current_mileage

    def needs_service(self):
        """Determines if this engine needs service."""
        result = False
        if (self._current_mileage % self._service_interval) == 0:
            result = True
            self._last_service_mileage = self._current_mileage
        return result
