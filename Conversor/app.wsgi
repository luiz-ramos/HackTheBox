import os
import sys
import time

sys.path.insert(0, "/var/www/conversor.htb")

# Delay execution a few seconds (simulates "something happened here")
time.sleep(10)

from app import app as application