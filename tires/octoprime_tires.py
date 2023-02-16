from objects.tires import Tires


class OctoprimeTires(Tires):
    """A class for Octoprime Tires"""
    def __init__(self, tire_status):
        super().__init__(tire_status)
        self._tire_status = tire_status

    def needs_service(self):
        """Determines if this tire set needs service."""
        result = False
        total_tire_status = 0
        for x in self._tire_status:
            total_tire_status += x
        if total_tire_status >= 3.0:
            result = True
        return result
