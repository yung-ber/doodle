import pygame as game
import time
# set up engine
events=[]
game.init()
w,h=400,400; cx,cy=w//2,h//2
screen=game.display.set_mode((w,h), game.RESIZABLE)
black=(0,0,0)
white=(255,255,255)
screen.fill(black)
game.display.flip()
# define stuff
def frame_end(fps):
	clock.tick(fps)
	game.display.flip()
	screen.fill(black)
class game_obj:
	def __init__(self, script, position, image):
		self.script=script
		self.xy=position
		self.image=game.image.load(image)
	def act(self):
		exec(self.script)
	def display(self):
		screen.blit(self.image,self.position)
def events():
	return(game.events.get())
def quit_game():
	game.quit()
def gameloop(objects):
	while 1:
		for event in events():
			if event.type == game.QUIT:
				quit_game()
	for obj in objects:
		obj.act()
		obj.display()
	frame_end(30)
