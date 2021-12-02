# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 00:27:42 2021

@author: jacob
"""

WIN_WIDTH = 640
WIN_HEIGHT = 480

PLAYER_LAYER = 4
ENEMY_LAYER = 3
BLOCK_LAYER=2
GROUND_LAYER = 1

PLAYER_SPEED = 3
ENEMY_SPEED = 2

TILESIZE = 32
FPS=60

RED = (255,0,0)
BLACK = (0,0,0)
BLUE = (0,0,255)
WHITE = (255,255,255)


tilemap = [
    "BBBBBBBBBBBBBBBBBBBB",
    "B..................B",
    "B...BBB............B",
    "B..................B",
    "B......E...........B",
    "B..................B",
    "B........BBB.......B",
    "B........P.B.......B",
    "B..........B.......B",
    "B..................B",
    "B..................B",
    "B.............E....B",
    "B..................B",
    "B..................B",
    "BBBBBBBBBBBBBBBBBBBB",    
    ]