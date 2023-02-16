from abc import ABC 
from objects.serviceable import Serviceable


class Engine(Serviceable, ABC):
    """Abstract class for an engine"""
