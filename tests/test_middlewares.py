from django.test import TestCase
from django.conf import settings
from freezegun import freeze_time
from datetime import datetime
from unittest.mock import MagicMock
import pytz

from django_shift_work import middlewares


class TestDjango_shift_work(TestCase):

    def setUp(self):
        self.request = MagicMock()
        tz = settings.TIME_ZONE
        now = datetime(2019, 4, 17, tzinfo=pytz.timezone(tz))

        self.test_datetimes = (
            now,
            now.replace(hour=12),
            now.replace(hour=7),
            now.replace(hour=19)
        )

    def test_get_shift_shift_work(self):
        mw = middlewares.ShiftWorkMiddleWare(lambda x: x)
        dt = self.test_datetimes

        for dt, name in zip(self.test_datetimes, ('night', 'morning', 'morning', 'night')):
            with freeze_time(lambda: dt):
                resp = mw(self.request)
                print(resp.shift['name'], resp.shift['end'], name)
                assert resp.shift['name'] == name

    def tearDown(self):
        pass
