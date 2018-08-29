import pygame, pytmx, sys, random
from pytmx.util_pygame import load_pygame

pygame.init()

###############CONSTANT###############

white = (255, 255, 255)
screen_res = (1600, 1600)

map = pygame.image.load('Assets/map1.png')
clock = pygame.time.Clock()


######Pygame Initialization

pygame.display.set_caption('MASON IS A FUCKING GOD')
display = pygame.display.set_mode(screen_res)                       # CREATES DISPLAY
screen = pygame.display.get_surface()                               # CREATES SURFACE FROM DISPLAY
tmxdata = load_pygame('Assets/map1.tmx')                            # LOADS TILED MAP DATA.



player_group = pygame.sprite.Group()




class Main(pygame.sprite.Sprite):
    state = 'world'


    def __init__(self):
        super().__init__








    def loop(self):

        while True:
            clock.tick(50)


            self.input()

            pygame.sprite.Group.update(player_group)

            self.render()
            self.tiler()


    def tiler(self):
        map = pytmx.load_pygame('map1.tmx')






    def input(self):
        #RECIEVES PLAYER INPUT. NEEDS TO BE FIXXED AS TO CONTINOUE MOVING TILL KEY IS DEPRESSED.
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit();  # sys.exit() if sys is imported

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player_character.rect.y -= 40
                        player_character.direction = 'N'
                    if event.key == pygame.K_DOWN:
                        player_character.rect.y += 40
                        player_character.direction = 'S'
                    if event.key == pygame.K_LEFT:
                        player_character.rect.x -= 40
                        player_character.direction = 'W'
                    if event.key == pygame.K_RIGHT:
                        player_character.rect.x += 40
                        player_character.direction = 'E'
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit();
                    if event.key == pygame.K_m:
                        self.state = 'map'



    def render(self):

        if self.state == 'world':
            pygame.Surface.fill(display,white)             #CLEAR SCREAM
            display.blit(map, (0,0))               #BLIT THE BACKGROUND MAP
            player_group.draw(screen)     #BLIT PLAYER CHARACTER MODEL AT CURRENT LOCATION
            pygame.display.flip()

        if self.state == 'map':
            pygame.Surface.fill(display, white)




class PC(pygame.sprite.Sprite):
    direction = 'N'
###ASSORTED MODELS FOR DIFFERENT FACING DIRECTIONS###
    sprites = {'N': 'Assets/Player Sprites/tile022.png',

               'E': 'Assets/Player Sprites/tile011.png',

               'S': 'Assets/Player Sprites/tile000.png',

               'W': 'Assets/Player Sprites/tile033.png'}



    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.direction = 'N'

        self.image = pygame.image.load('Assets/Player Sprites/tile000.png')
        self.rect = self.image.get_rect()

    def update(self, *args):

        self.image = pygame.image.load(self.sprites[self.direction])




























player_character = PC()

player_group.add(player_character)


init = Main()







init.loop()


x = input('g')