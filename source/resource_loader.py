import pygame as pg
import dataclasses
import logging
import math
import json
import os


SPRITES: dict[str, tuple[pg.Surface]] = {}

KEY_COLOR = (255, 0, 255)

@dataclasses.dataclass
class AlphaMode:
	NONE: int = 0
	KEY: int = 1
	FULL: int = 2


def load_from_spritesheet(spritesheet_path: str, rect: pg.Rect, alpha_mode: int=AlphaMode.NONE) -> pg.Surface:
	""" Loads a defined area from an image (spritesheet) """

	logging.debug("Loading from spritesheet")

	image = pg.image.load(spritesheet_path).subsurface(rect)
	
	match alpha_mode:
		case AlphaMode.NONE: image = image.convert()
		case AlphaMode.KEY: image = image.convert(); image.set_colorkey(KEY_COLOR)
		case AlphaMode.FULL: image = image.convert_alpha()

	return image.convert()


def multi_load_from_spritesheet(spritesheet_path: str, rects: list[pg.Rect]|tuple[pg.Rect], alpha_mode: int=AlphaMode.NONE) -> pg.Surface:
	""" Loads a list of defined areas from an image (spritesheet) """

	logging.debug("Multi-loading from spritesheet")
	logging.debug(f" * spritesheet_path: {spritesheet_path}")
	logging.debug(f" * rects: {rects}")
	logging.debug(f" * alpha_mode: {alpha_mode}")

	spritesheet = pg.image.load(spritesheet_path)
	images: list[pg.Rect] = []

	for rect in rects:
		image = spritesheet.subsurface(rect)

		match alpha_mode:
			case AlphaMode.NONE: image = image.convert()
			case AlphaMode.KEY: image = image.convert(); image.set_colorkey(KEY_COLOR)
			case AlphaMode.FULL: image = image.convert_alpha()

		images.append(image)

	return images


def load_sprites() -> None:
	""" Called ONCE after the display is initialized, it loads all the sprites in the game. """

	global SPRITES

	logging.debug("Loading all sprites")

	for dirpath, dirnames, filenames in os.walk("./resources/sprites"):
		logging.debug(f"Loading from {dirpath}")

		for filename in filenames:
			if not filename[-4:] == ".png": continue

			logging.debug(f" * {filename}")
			
			image_path: str = os.path.join(dirpath, filename)
			metadata_path: str = os.path.join(dirpath, filename[:-4]+".json")
			
			if not os.path.exists(metadata_path): continue

			image = pg.image.load(image_path)

			with open(metadata_path, "r") as f:
				metadata: dict = json.load(f)

			sprites: list = []
			sprite_count_x: int = math.floor(image.get_width() / metadata["grid_w"])
			sprite_count_y: int = math.floor(image.get_height() / metadata["grid_h"])
			for y in range(sprite_count_y):
				for x in range(sprite_count_x):
					sprite = image.subsurface((
						x * metadata["grid_w"], y * metadata["grid_h"], metadata["grid_w"], metadata["grid_h"]))

					match metadata["alpha_mode"]:
						case "NONE": sprite = sprite.convert()
						case "KEY": sprite = sprite.convert(); sprite.set_colorkey(KEY_COLOR)
						case "FULL": sprite = sprite.convert_alpha()

					sprites.append(sprite)

			SPRITES[filename[:-4]] = tuple(sprites)