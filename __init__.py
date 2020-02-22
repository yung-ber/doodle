# 5 ducks company's doodle engine for first person
# games. open scource for all who want to make 3D
# games in python 3.
import doodle, sys, math
import pygame as game
# set up engine
events=[]
game.init()
w,h=400,400; cx,cy=w//2,h//2
screen=game.display.set_mode((w,h), game.RESIZABLE)
game.display.set_caption('Powered by DOODLE')
clock=game.time.Clock()
# definitions
def gameloop(loop, cam):
	while True:
		#dt = clock.tick/1000
		events=[]
		for event in game.event.get():
			if event.type == game.QUIT:
				game.quit()
				sys.exit()
			else:
				events+=[event]
		screen.fill((255,255,255))
		loop()
		game.display.update()
		key=doodle.game.key.get_pressed()
		cam.update(1,key)
class shape:
	def __init__(self, verts, edges):
		self.verts=verts
		self.edges=edges
	def plot(self, cam):
		for edge in self.edges:
			points=[]
			for x,y,z in self.verts[edge[0]],self.verts[edge[1]]:
				x-=cam.pos[0]
				y-=cam.pos[1]
				z-=cam.pos[2]
				z+=5
				f=200/z
				x,y=x*f,y*f
				points+=[(cx+int(x),cy+int(y))]
			game.draw.line(screen,(0,0,0),points[0],points[1],1)
class cam:
	def __init__(self,pos=(0,0,0),rot=(0,0),fly=False):
		self.pos=list(pos)
		self.rot=list(rot)
		self.fly=fly
	def update(self, speed, key):
		s=speed*10
		if self.fly:
			if key[game.K_q]: self.pos[1]-=s
			if key[game.K_w]: self.pos[1]+=s
		if key[game.K_w]: self.pos[2]+=s
		if key[game.K_s]: self.pos[2]-=s
		if key[game.K_a]: self.pos[0]-=s
		if key[game.K_d]: self.pos[0]+=s
cube=shape([(-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)],[(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)])
