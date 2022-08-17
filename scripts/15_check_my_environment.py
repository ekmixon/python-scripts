"""
Pass in a config file based on your environment.

Example:

import check_my_environment


class Main:
    def __init__(self, configFile):
        pass

    def process(self):
        print("ok")

if __name__ == "__main__":
    m = Main(some_script.CONFIGFILE)
    m.process()

"""


import os
import sys
ENVIRONMENT = "development"
CONFIGFILE = None


def get_config_file():
    directory = os.path.dirname(__file__)
    return {
        "development": f"{directory}/../config/development.cfg",
        "staging": f"{directory}/../config/staging.cfg",
        "production": f"{directory}/../config/production.cfg",
    }.get(ENVIRONMENT, None)

CONFIGFILE = get_config_file()

if CONFIGFILE is None:
    sys.exit("Configuration error! Unknown environment set. \
              Edit config.py and set appropriate environment")
print(f"Config file: {CONFIGFILE}")
if not os.path.exists(CONFIGFILE):
    sys.exit("Configuration error! Config file does not exist")
print("Config ok ....")
