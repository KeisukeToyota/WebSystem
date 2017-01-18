#!/usr/bin/env python
import os
import sys
import pymysql


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WebSystem.settings")

    from django.core.management import execute_from_command_line

    from django.core.management import execute_from_command_line
    pymysql.install_as_MySQLdb()

    execute_from_command_line(sys.argv)
