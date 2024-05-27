import pygame as pg
from dataclasses import dataclass



KEY_COLOR = (255, 0, 255)

@dataclass
class AlphaMode:
	NONE: int = 0
	KEY: int = 1
	FULL: int = 2


def load_from_spritesheet(spritesheet_path: str, rect: pg.Rect, alpha_mode: int=AlphaMode.NONE) -> pg.Surface:
	""" Loads a defined area from an image (spritesheet) """

	image = pg.image.load(spritesheet_path).subsurface(rect)
	
	match alpha_mode:
		case AlphaMode.NONE: image = image.convert()
		case AlphaMode.KEY: image = image.convert(); image.set_colorkey(KEY_COLOR)
		case AlphaMode.FULL: image = image.convert_alpha()

	return image.convert()


def multi_load_from_spritesheet(spritesheet_path: str, rects: list[pg.Rect]|tuple[pg.Rect], alpha_mode: int=AlphaMode.NONE) -> pg.Surface:
	""" Loads a list of defined areas from an image (spritesheet) """

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