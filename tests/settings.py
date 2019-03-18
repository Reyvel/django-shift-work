# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import
from datetime import time

import django

DEBUG = True
USE_TZ = True
TIME_ZONE = 'Asia/Jakarta'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "eh#v7o0%)0%n(=-q&y=q$bo9ix)s2$)a_93id&t6$e=d&!wv89"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

ROOT_URLCONF = "tests.urls"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "django_shift_work",
]

SITE_ID = 1

if django.VERSION >= (1, 10):
    MIDDLEWARE = (
        'django_shift_work.middlewares.ShiftWorkMiddleWare'
    )
else:
    MIDDLEWARE_CLASSES = ()

SHIFT_PLAN = {
    'morning': (time(hour=7), time(hour=19)),
    'night': (time(hour=19), time(hour=7))
}
