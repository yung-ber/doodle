# doodle
doodle game engine
## doodle_engine_core
  ### doodle_engine_core.matrix44
    - Matrix44 (4x4 matrix class)
    - Matrix44Error (error class for matrix44)
  ### doodle_engine_core.doodle3D
    (contains copy of pygame, OpenGL.GL, and OpenGL.GLU; also contains a copy of doodle_engine_core.matrix44)
    - Game ( EX. game=Game((800,600), title='Ree!') )
    - Vector3 (class for 3D vectors)
  ### doodle_engine_core.doodle2D
    #### game_obj ( class for gameObjects (or sprites) )
      - example=__init__(script, position, image)
      - example.act()
      - example.display()
    (contains copy of pygame (as doodle2D.game))
    - screen (pygame.surface)
    - black (colour tuple)
    - white (colour tuple)
    - frame_end(fps) (next frame)
    - events() (copy of pygame.event.get)
    - quit_game() (quit the game)
    - gameloop(gameobjects) (main game loop)
