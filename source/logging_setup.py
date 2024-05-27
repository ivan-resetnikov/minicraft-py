# This file sets up a logging environment, thus should be imported and NEVER used

import logging
import datetime
import configparser

SPACING = 50



config = configparser.ConfigParser()

logging.basicConfig(filename="game.log", level=logging.DEBUG)
logging.info("Session started".center(SPACING, "="))
logging.info(f"Session date: {datetime.datetime.now()}")

config.read("info.cfg")

logging.info("Minicaraft version-{} build-{}".format(
	config.get("game", "version", fallback="UNDEF"),
	config.get("game", "build", fallback="UNDEF")))

logging.info("-" * SPACING)