WINDOW_WIDTH = 575
WINDOW_HIGHT = 575

PLAYER_LAYER = 1
BLOCK_LAYER = 2

TILESIZE = 32

PLAYER_SPEED = 3

PURPLE = 238, 59, 239
BLUE = 0, 0, 255
GREEN = 0, 255, 0
Black = 0, 0, 0

FPS = 60

def TILEMAP_Create():
    TILEMAP = []

    Width = 7
    Hight = 10

    TILEMAP.append('B' * Width)
    for i in range(Hight - 2):
        TILEMAP.append('B' + ' ' * (Width-2) + 'B')
    TILEMAP.append('B' * Width)
    return TILEMAP



TILEMAP = TILEMAP_Create()

  
'''TILEMAP = [
'BBBBBBBBBBBBBBBBBB',
'B                B',
'B                B',
'B                B',
'B               GB',
'B              G B',
'B             G  B',
'B            G   B',
'B           G    B',
'B          G     B',
'B         G      B',
'B        G       B',
'B       G        B',
'B      G         B',
'B     G          B',
'B    G           B',
'B P G            B',
'BBBBBBBBBBBBBBBBBB',
]'''
