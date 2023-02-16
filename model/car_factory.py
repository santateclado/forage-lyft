from battery import nubbin_battery, spindler_battery
from engine import capulet_engine, willoughby_engine, sternman_engine
from tires import carrigan_tires, octoprime_tires
from objects import Car


class CarFactory:
    """A factory for cars"""

    @classmethod
    def create_calliope(cls, last_service_date, current_mileage, last_service_mileage, tire_status):
        """Creates a Calliope car"""
        engine = capulet_engine.__init__(last_service_mileage, current_mileage)
        battery = spindler_battery.__init__(last_service_date)
        tires = carrigan_tires.__init__(tire_status)
        car = Car.__init__(engine, battery, tires)
        return car

    @classmethod
    def create_glissade(cls, last_service_date, current_mileage, last_service_mileage, tire_status):
        """Creates a Glissade car"""
        engine = willoughby_engine.__init__(
            last_service_mileage, current_mileage)
        battery = spindler_battery.__init__(last_service_date)
        tires = carrigan_tires.__init__(tire_status)
        car = Car.__init__(engine, battery, tires)
        return car

    @classmethod
    def create_palindrome(cls, last_service_date, warning_light_on, tire_status):
        """Creates a Palindrome car"""
        engine = sternman_engine.__init__(warning_light_on)
        battery = spindler_battery.__init__(last_service_date)
        tires = octoprime_tires.__init__(tire_status)
        car = Car.__init__(engine, battery, tires)
        return car

    @classmethod
    def create_rorschach(cls, last_service_date, current_mileage, last_service_mileage, tire_status):
        """Creates a Rorschach car"""
        engine = willoughby_engine.__init__(
            last_service_mileage, current_mileage)
        battery = nubbin_battery.__init__(last_service_date)
        tires = octoprime_tires.__init__(tire_status)
        car = Car.__init__(engine, battery, tires)
        return car

    @classmethod
    def create_thovex(cls, last_service_date, current_mileage, last_service_mileage, tire_status):
        """Creates a Thovex car"""
        engine = capulet_engine.__init__(last_service_mileage, current_mileage)
        battery = nubbin_battery.__init__(last_service_date)
        tires = carrigan_tires.__init__(tire_status)
        car = Car.__init__(engine, battery, tires)
        return car
