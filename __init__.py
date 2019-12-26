# did u go 2 church this sunday?
# 5 ducks company's doodle engine for first person
# games. open scource for all who want to make first
# person games in python 3. covers the basics.
import doodle
import pygame as game
import time, sys, threading
from PIL import Image
game.init()
sprites=[]
class sprite:
    def __init__(self, image, xy=(250,250)):
        self.img=game.image.load(image) # notice I did not use .convert()
        self.im=Image.open(image)
        self.size=self.im.size # Get size if image
        self.clones=[]
        sprites.append(self)
        game.display.update()
        self.xy=xy
    def send(self, xy):
        (x,y)=xy # unpack coordinates
        self.xy=xy # for refresh() purposes
        (width,height)=self.size # unpack size
        x=x-(width/2)
        y=y-(height/2)
        xy=(x,y) # repack coordinates
        disp.blit(self.img, xy)
        game.display.update() # update display
    def refresh(self):
        self.send(self.xy) # send sprite to the front
        game.display.update() # update display
    def imgset(self, image):
        # mimic most of __init__'s code
        self.img=game.image.load(image)
        self.im=Image.open(image)
        self.size=self.im.size
        self.refresh() # call sprite refresh
    def clone(self):
        self.clones.append(self) # make clone
    def reset(self):
        self.clones=[] # delete clones
        self.xy=(250,250) # go to middle
		self.refresh() # update sprite
class background(sprite):
    def start():
        global BG
        BG=sprite('bg.png')
        BG.refresh()
def pulltheplug():
    game.quit()
def window(name=' '):
    global disp
    disp=game.display.set_mode((800, 600), game.RESIZABLE)
    game.display.set_caption(name)
class clock:
    frames=0
    def record():
        clock.frames+=1
    def reset():
        clock.frames=0
    def fps():
        while 1:
            time.sleep(1)
            print(clock.frames)
            clock.reset()
if __name__ == '__main__':
    try:
        exec(open(sys.argv[1]).read())
    except:
        print('ERROR: not running file or running in file.')
