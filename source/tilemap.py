import pygame as pg
import logging
import math

from camera import Camera

vec2 = pg.math.Vector2
x = 0
y = 1

TILE_SIZE: int = 16
CHUNK_SIZE: int = 16


class Tile:
	""" Tile data container, part of the tilemap system """

	def __init__(self, sprite: pg.Surface, pos: tuple[int, int]) -> None:
		self.sprite = sprite
		self.pos = pos


class Chunk:
	""" Chunk interface, part of the tilemap system """

	def __init__(self, pos: tuple[int, int]) -> None:
		self.pos: tuple[int, int] = pos
		
		self.tiles: dict[Tile] = {}
		self.surface: pg.Surface = pg.Surface((
			TILE_SIZE * CHUNK_SIZE, TILE_SIZE * CHUNK_SIZE))


	def add_tile(self, tile: Tile, rel_pos: tuple[int, int]) -> None:
		""" Sets a tile  """
		self.surface.blit(tile.sprite, (rel_pos[x] * TILE_SIZE, rel_pos[y] * TILE_SIZE))

		# TODO: Store tile in the self.tiles property


	def draw(self, render_target: pg.Surface, camera: Camera) -> None:
		render_target.blit(self.surface, vec2(self.pos) - camera.pos)


class TileMap:
	""" Tilemap system interaface """

	def __init__(self) -> None:
		self.chunks: dict[Chunk] = {}


	def set_tile(self, tile: Tile) -> None:
		""" TODO """

		chunk_coords: tuple[int] = (
			math.floor(tile.pos[x] / CHUNK_SIZE),
			math.floor(tile.pos[y] / CHUNK_SIZE))
		chunk_index: str = f"x{chunk_coords[x]}y{chunk_coords[y]}"
		
		# Add chunk if it doesn't exist
		if not chunk_index in tuple(self.chunks.keys()):
			self.chunks[chunk_index] = Chunk((
				chunk_coords[x] * CHUNK_SIZE * TILE_SIZE,
				chunk_coords[y] * CHUNK_SIZE * TILE_SIZE))

		# Relative-to-chunk position of the tile
		rel_pos: tuple[int] = (
			tile.pos[x] - chunk_coords[x] * CHUNK_SIZE,
			tile.pos[y] - chunk_coords[y] * CHUNK_SIZE)

		self.chunks[chunk_index].add_tile(tile, rel_pos)


	def draw(self, render_target: pg.Surface, camera: Camera) -> None:
		for chunk in tuple(self.chunks.values()):
			chunk.draw(render_target, camera)
