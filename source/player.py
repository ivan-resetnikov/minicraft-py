import pygame as pg
from resource_loader import multi_load_from_spritesheet, AlphaMode
from camera import Camera

vec2 = pg.math.Vector2



class Player:
	def __init__(self):
		self.sprites = multi_load_from_spritesheet("./resources/entities.png", (
				pg.Rect(0, 0, 8, 8),
				pg.Rect(0, 8, 8, 8),
				pg.Rect(0, 16, 8, 8),
				pg.Rect(0, 24, 8, 8),
			), AlphaMode.KEY)

		self.pos = vec2(0, 0)
		self.vel = vec2(0, 0)

		self.speed = 0.8

	def ready(self) -> None:
		pass

	def update(self) -> None:
		pressed_keys = pg.key.get_pressed()

		self.vel.x += (float(pressed_keys[pg.K_d]) - float(pressed_keys[pg.K_a])) * self.speed
		self.vel.y += (float(pressed_keys[pg.K_s]) - float(pressed_keys[pg.K_w])) * self.speed
		self.vel *= 0.6

		self.pos += self.vel

	def draw(self, render_target: pg.Surface, camera: Camera) -> None:
		sprite = self.sprites[0]

		match int(self.vel.y):
			case -1: sprite = self.sprites[1]
			case  1: sprite = self.sprites[0]

		match int(self.vel.x):
			case -1: sprite = self.sprites[2]
			case  1: sprite = self.sprites[3]

		render_target.blit(sprite, self.pos - camera.pos)