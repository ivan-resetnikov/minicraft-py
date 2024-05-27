import pygame as pg
from resource_loader import multi_load_from_spritesheet, AlphaMode
from camera import Camera

vec2 = pg.math.Vector2



class Player:
	def __init__(self):
		self.sprites = multi_load_from_spritesheet("./resources/sprites/entities.png", (
				pg.Rect(0, 0, 16, 16),
				pg.Rect(16, 0, 16, 16),
				pg.Rect(32, 0, 16, 16),
				pg.Rect(48, 0, 16, 16),
			), AlphaMode.KEY)

		self.pos = vec2(0, 0)
		self.vel = vec2(0, 0)

		self.speed = 0.5
		self.input_vector: vec2 = vec2()

	def ready(self) -> None:
		pass

	def update(self) -> None:
		pressed_keys = pg.key.get_pressed()

		self.input_vector = vec2(
			(float(pressed_keys[pg.K_d]) - float(pressed_keys[pg.K_a])),
			(float(pressed_keys[pg.K_s]) - float(pressed_keys[pg.K_w])))
		
		if self.input_vector:
			input_vector_norm: vec2 = self.input_vector.normalize()
		else:
			input_vector_norm: vec2 = self.input_vector

		self.vel += input_vector_norm * self.speed
		self.vel *= 0.6

		self.pos += self.vel

	def draw(self, render_target: pg.Surface, camera: Camera) -> None:
		sprite = self.sprites[0]

		match self.input_vector.y:
			case -1: sprite = self.sprites[1]
			case  1: sprite = self.sprites[0]

		match self.input_vector.x:
			case -1: sprite = self.sprites[2]
			case  1: sprite = self.sprites[3]

		render_target.blit(sprite, self.pos - camera.pos)