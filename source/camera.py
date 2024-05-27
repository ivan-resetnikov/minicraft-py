import pygame as pg
import math

vec2 = pg.math.Vector2



class Camera:
	def __init__(self, window_size: vec2):
		self.pos = vec2(0, 0)
		self.half_target_size = vec2(0, 0)
		self.half_window_size = vec2(window_size) / 2


	def set_target(self, target, target_size: vec2) -> None:
		"""
		Sets the follow target for the camera
		
		Parameters:
		target = Any object with a `pos: pg.math.Vector2` property
		"""

		if not hasattr(self.target, "pos"): return

		self.target = target
		self.half_target_size = vec2(target_size) / 2


	def update(self) -> None:
		self.pos += (self.target.pos - self.half_window_size + self.half_target_size - self.pos) * 1.0