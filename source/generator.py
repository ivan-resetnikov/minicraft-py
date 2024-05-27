import pygame as pg
import random
from resource_loader import load_from_spritesheet, AlphaMode
from tilemap import TileMap, Tile

sprite_sheet = pg.image.load("./resources/sprites/tileset.png")

TILE_SPRITES: dict[str, Tile] = {
	"dirt": sprite_sheet.subsurface(pg.Rect(0, 0, 16, 16)),
	"sand": sprite_sheet.subsurface(pg.Rect(16, 0, 16, 16)),
	"water": sprite_sheet.subsurface(pg.Rect(32, 0, 16, 16)),
	"stone": sprite_sheet.subsurface(pg.Rect(48, 0, 16, 16)),
}



def generate_world(tilemap: TileMap) -> None:
	""" Generated a new world """

	# TODO: Make an actual world generator
	for y in range(32):
		for x in range(32):
			tilemap.set_tile(Tile(
				tuple(TILE_SPRITES.values())[random.randint(0, 3)],
				(x, y)))