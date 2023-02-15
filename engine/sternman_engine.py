from objects.engine import Engine


class SternmanEngine(Engine):
    """A class that represents a Sternman engine"""
    def __init__(self, warning_light_on, last_service_date):
        super().__init__(last_service_date)
        self._last_service_date = last_service_date
        self._warning_light_on = warning_light_on
        
    def needs_service(self):
        """Determines if this engine needs service."""
        return self._warning_light_on
