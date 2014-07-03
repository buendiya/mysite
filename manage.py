#!/usr/bin/env python
import os
import sys
import logging

logger = logging.getLogger("manage.py")
formatter = logging.Formatter('%(name)-12s %(asctime)s %(levelname)-8s %(message)s', '%a, %d %b %Y %H:%M:%S',)
file_handler = logging.FileHandler("test.log")
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler(sys.stderr)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    logger.info("DJANGO_SETTINGS_MODULE: %s" % os.environ['DJANGO_SETTINGS_MODULE'])

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
