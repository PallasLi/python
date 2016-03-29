#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoTest.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
#     .manage.py runserver  startweb
#     execute_from_command_line(sys.argv)
# python3 manage.py migrate --run-syncdb
# python3 manage.py createsuperuser --username=joe --email=joe@example.com
