#!/usr/bin/env python
import os
import sys

if _name_ == "_main_":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jobportal.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Make sure it's installed and available on your PYTHONPATH environment variable. Did you forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
