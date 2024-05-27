import pygame as pg
from tilemap import TileMap, Tile
from player import Player
from camera import Camera
from generator import generate_world

vec2 = pg.math.Vector2

FPS: int = 60
PIXEL_SIZE: int = 4
RENDER_WIDTH: int = 256
RENDER_HEIGHT: int = 144
WINDOW_WIDTH: int = RENDER_WIDTH * PIXEL_SIZE
WINDOW_HEIGHT: int = RENDER_HEIGHT * PIXEL_SIZE



class Game:
	def __init__(self) -> None:
		self.window = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		self.render_texture = pg.Surface((RENDER_WIDTH, RENDER_HEIGHT))
		self.clock = pg.time.Clock()

		pg.display.set_caption("Minicraft")

	def run(self) -> None:
		self.init()

		self.running = True
		while self.running:
			for event in pg.event.get():
				match event.type:
					case pg.QUIT: self.running = False

			self.render_texture.fill((0, 0, 0))

			self.update()
			self.draw()

			self.window.blit(pg.transform.scale_by(self.render_texture, PIXEL_SIZE), (0, 0))
			pg.display.flip()
			self.clock.tick(FPS)

		self.quit()

	def init(self) -> None:
		self.font = pg.font.Font("./resources/fonts/pico-8.ttf", 4)

		self.tilemap = TileMap()
		self.player = Player()
		self.camera = Camera((RENDER_WIDTH, RENDER_HEIGHT))
		self.camera.set_target(self.player, (8, 8))

		generate_world(self.tilemap)

	def update(self) -> None:
		self.player.update()
		self.camera.update()

	def draw(self) -> None:
		self.tilemap.draw(self.render_texture, self.camera)
		self.player.draw(self.render_texture, self.camera)

		self.render_texture.blit(self.font.render(
				text=str(int(self.clock.get_fps())) + " FPS",
				antialias=False,
				color=(255, 255, 0),
				bgcolor=(0, 0, 0)),
			dest=(1, 1))

	def quit(self) -> None:
		pass



if __name__ == "__main__":
	pg.init()
	pg.font.init()

	Game().run()

	pg.font.quit()
	pg.quit()