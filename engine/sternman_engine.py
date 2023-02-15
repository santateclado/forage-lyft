from objects.engine import Engine


class SternmanEngine(Engine):
    """A class that represents a Sternman engine"""

    def __init__(self, warning_light_on):
        self._warning_light_on = warning_light_on

    def needs_service(self):
        """Determines if this engine needs service."""
        return self._warning_light_on
