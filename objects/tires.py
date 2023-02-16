from abc import ABC, abstractmethod
from objects.serviceable import Serviceable


class Tires(Serviceable, ABC):
    """An abstract class for tires"""
    def __init__(self, tire_status):
        self._tire_status = tire_status
