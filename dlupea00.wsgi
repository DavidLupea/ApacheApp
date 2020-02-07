#!/usr/bin/python3
import sys
sys.path.insert(0, "/var/www/dlupea00/")
sys.path.insert(0, "/var/www/dlupea00/dlupea00/")

import logging
logging.basicConfig(stream = sys.stderr)

from dlupea00 import app as application
