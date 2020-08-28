# documentation
index:
  - [matrix44](https://github.com/yung-ber/doodle/blob/master/README.md#doodle_engine_corematrix44)
  - [doodle3D](https://github.com/yung-ber/doodle/blob/master/README.md#doodle_engine_coredoodle3D)
  - [doodle2D](https://github.com/yung-ber/doodle/blob/master/README.md#doodle_engine_coredoodle2D)
## doodle_engine_core
  ### doodle_engine_core.matrix44
    - Matrix44 (4x4 matrix class)
    - Matrix44Error (error class for matrix44)
    - a bunch of other stuff that you probably dont need to know about unless you are really techy, in which case you could just read the code
  ### doodle_engine_core.doodle3D
    (contains copy of pygame, OpenGL.GL, and OpenGL.GLU; also contains a copy of doodle_engine_core.matrix44)
    - Game ( EX. game=Game((800,600), title='Ree!') )
    - Mosaic (class for mosaics)
      - example=Mosaic(image)
      - example.render()
    - Cube (class for cube objects)
      - example=Cube(position, colour)
      - example.num_faces
      - example.vertices
      - example.normals
      - example.vertex_indices
      - example.render()
    - Vector3 (class for 3D vectors)
    - more Vector3 definitions
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
