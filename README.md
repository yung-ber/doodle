# documentation
index:
  [matrix44](https://github.com/yung-ber/doodle/blob/master/README.md#doodle_engine_corematrix44)
  [doodle3D](https://github.com/yung-ber/doodle/blob/master/README.md#doodle_engine_coredoodle3D)
  [doodle2D](https://github.com/yung-ber/doodle/blob/master/README.md#doodle_engine_coredoodle2D)
## doodle_engine_core
  ### doodle_engine_core.matrix44
    - Matrix44 (4x4 matrix class)
    - Matrix44Error (error class for matrix44)
  ### doodle_engine_core.doodle3D
    (contains copy of pygame, OpenGL.GL, and OpenGL.GLU; also contains a copy of doodle_engine_core.matrix44)
    - Game ( EX. game=Game((800,600), title='Ree!') )
    - Vector3 (class for 3D vectors)
  ### doodle_engine_core.doodle2D
    - game_obj ( class for gameObjects (or sprites) )
      - example=game_obj(script, position, image) (init)
      - example.act() (exec script)
      - example.display() (render gameObject)
    (contains copy of pygame (as doodle2D.game))
    - screen (pygame.surface)
    - black (colour tuple)
    - white (colour tuple)
    - frame_end(fps) (next frame)
    - events() (copy of pygame.event.get)
    - quit_game() (quit the game)
    - gameloop(gameobjects) (main game loop)
## example 2d project
  ### project
    from doodle_engine_core.doodle2D import*
    img=game.image.load('image.png').convert_alpha() # replace with your own image
    obj=game_obj('x,y=self.xy\nx+=1\ny+=1\nself.xy=(x,y)', (0,0), img)
    gameloop([obj])
