import unittest
from datetime import datetime, timedelta

from engine import capulet_engine, sternman_engine, willoughby_engine


class TestCapuletEngine(unittest.TestCase):
    def should_be_serviced(self):
        engine1 = capulet_engine.CapuletEngine(0, 15000)
        engine2 = capulet_engine.CapuletEngine(0, 30000)
        engine3 = capulet_engine.CapuletEngine(30000, 45000)
        engine4 = capulet_engine.CapuletEngine(15000, 30000)
        engine5 = capulet_engine.CapuletEngine(15000, 45000)
        engine6 = capulet_engine.CapuletEngine(30000, 60000)

        self.assertFalse(engine1.needs_service())
        self.assertTrue(engine2.needs_service())
        self.assertFalse(engine3.needs_service())
        self.assertFalse(engine4.needs_service())
        self.assertTrue(engine5.needs_service())
        self.assertTrue(engine6.needs_service())


class TestSternmanEngine(unittest.TestCase):
    def should_be_serviced(self):
        engine1 = sternman_engine.SternmanEngine(False)
        engine2 = sternman_engine.SternmanEngine(True)

        self.assertFalse(engine1.needs_service())
        self.assertTrue(engine2.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    def should_be_serviced(self):
        engine1 = willoughby_engine.WilloughbyEngine(0, 15000)
        engine2 = willoughby_engine.WilloughbyEngine(0, 30000)
        engine3 = willoughby_engine.WilloughbyEngine(0, 60000)
        engine4 = willoughby_engine.WilloughbyEngine(30000, 60000)
        engine5 = willoughby_engine.WilloughbyEngine(30000, 90000)
        engine6 = willoughby_engine.WilloughbyEngine(90000, 12000)
        engine7 = willoughby_engine.WilloughbyEngine(90000, 15000)

        self.assertFalse(engine1.needs_service())
        self.assertFalse(engine2.needs_service())
        self.assertTrue(engine3.needs_service())
        self.assertFalse(engine4.needs_service())
        self.assertTrue(engine5.needs_service())
        self.assertFalse(engine6.needs_service())
        self.assertTrue(engine7.needs_service())
