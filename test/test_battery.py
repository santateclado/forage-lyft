import unittest
from datetime import datetime, timedelta

from battery import nubbin_battery, spindler_battery


class TestNubbinBattery(unittest.testCase):
    def should_be_serviced(self):
        today = datetime.today().date()
        battery1 = nubbin_battery.NubbinBattery(today)
        battery2 = nubbin_battery.NubbinBattery(today - timedelta(years=2))
        battery3 = nubbin_battery.NubbinBattery(today - timedelta(years=3))
        battery4 = nubbin_battery.NubbinBattery(today - timedelta(years=4))
        battery5 = nubbin_battery.NubbinBattery(today - timedelta(days=50))
        battery6 = nubbin_battery.NubbinBattery(today - timedelta(years=5))
        battery7 = nubbin_battery.NubbinBattery(today - timedelta(years=6))

        self.assertFalse(battery1.needs_service())
        self.assertFalse(battery2.needs_service())
        self.assertFalse(battery3.needs_service())
        self.assertTrue(battery4.needs_service())
        self.assertFalse(battery5.needs_service())
        self.assertTrue(battery6.needs_service())
        self.assertTrue(battery7.needs_service())


class TestSpindlerBattery(unittest.testCase):
    def should_be_serviced(self):
        today = datetime.today().date()
        battery1 = spindler_battery.SpindlerBattery(today)
        battery2 = spindler_battery.SpindlerBattery(
            today - timedelta(days=150))
        battery3 = spindler_battery.SpindlerBattery(
            today - timedelta(days=365))
        battery4 = spindler_battery.SpindlerBattery(
            today - timedelta(days=(365 + 150)))
        battery5 = spindler_battery.SpindlerBattery(
            today - timedelta(days=(365 * 2)))
        battery6 = spindler_battery.SpindlerBattery(
            today - timedelta(days=((365 * 2) + 150)))

        self.assertFalse(battery1.needs_service())
        self.assertFalse(battery2.needs_service())
        self.assertFalse(battery3.needs_service())
        self.assertFalse(battery4.needs_service())
        self.assertTrue(battery5.needs_service())
        self.assertTrue(battery6.needs_service())
