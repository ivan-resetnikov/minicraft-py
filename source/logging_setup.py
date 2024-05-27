# This file sets up a logging environment, thus should be imported and never used

import logging
import datetime
import configparser

config = configparser.ConfigParser()

logging.basicConfig(filename="game.log", level=logging.DEBUG)
logging.info("Session started".center(50, "="))
logging.info(f"Session date: {datetime.datetime.now()}")

config.read("info.cfg")

logging.info("Minicaraft version-{} build-{}".format(
	config.get("game", "version", fallback="UNDEF"),
	config.get("game", "build", fallback="UNDEF")))