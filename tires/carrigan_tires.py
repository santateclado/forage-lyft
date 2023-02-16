from objects.tires import Tires


class CarriganTires(Tires):
    """A class for Carrigan Tires"""
    def __init__(self, tire_status):
        super().__init__(tire_status)
        self._tire_status = tire_status

    def needs_service(self):
        """Determines if this tire set needs service."""
        result = False
        for x in self._tire_status:
            if x >= 0.9:
                result = True
                break
        return result
