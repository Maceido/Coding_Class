import pygame
#screen size
SIZE = WIDTH, HEIGHT = 600, 400
FPS = 10      
class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()
        #when player isnt moving
        self.idle = []
        self.idle.append(pygame.image.load('Sprites/animationplayer/adventurer-idle-2-00.png'))
        self.idle.append(pygame.image.load('Sprites/animationplayer/adventurer-idle-2-01.png'))
        self.idle.append(pygame.image.load('Sprites/animationplayer/adventurer-idle-2-02.png'))
        self.idle.append(pygame.image.load('Sprites/animationplayer/adventurer-idle-2-03.png'))

        #When the player runs right this is the animation
        self.run = []
        self.run.append(pygame.image.load('Sprites/animationplayer/adventurer-run-00.png'))
        self.run.append(pygame.image.load('Sprites/animationplayer/adventurer-run-01.png'))
        self.run.append(pygame.image.load('Sprites/animationplayer/adventurer-run-02.png'))
        self.run.append(pygame.image.load('Sprites/animationplayer/adventurer-run-03.png'))
        self.run.append(pygame.image.load('Sprites/animationplayer/adventurer-run-04.png'))
        self.run.append(pygame.image.load('Sprites/animationplayer/adventurer-run-05.png'))
        #When the player runs left this is the animantion 
        self.runback = []
        self.runback.append(pygame.image.load('Sprites/animationplayer/adventurer-run-backwards-00.png'))
        self.runback.append(pygame.image.load('Sprites/animationplayer/adventurer-run-backwards-01.png'))
        self.runback.append(pygame.image.load('Sprites/animationplayer/adventurer-run-backwards-02.png'))
        self.runback.append(pygame.image.load('Sprites/animationplayer/adventurer-run-backwards-03.png'))
        self.runback.append(pygame.image.load('Sprites/animationplayer/adventurer-run-backwards-04.png'))
        self.runback.append(pygame.image.load('Sprites/animationplayer/adventurer-run-backwards-05.png'))
        #Players jumping animation
        self.jump = []
        self.jump.append(pygame.image.load('Sprites/animationplayer/adventurer-jump-00.png'))
        self.jump.append(pygame.image.load('Sprites/animationplayer/adventurer-jump-01.png'))
        self.jump.append(pygame.image.load('Sprites/animationplayer/adventurer-jump-02.png'))
        self.jump.append(pygame.image.load('Sprites/animationplayer/adventurer-jump-03.png'))
        #Players attacking animation
        self.attack = []
        self.attack.append(pygame.image.load('Sprites/animationplayer/adventurer-attack2-00.png'))
        self.attack.append(pygame.image.load('Sprites/animationplayer/adventurer-attack2-01.png'))
        self.attack.append(pygame.image.load('Sprites/animationplayer/adventurer-attack2-02.png'))
        self.attack.append(pygame.image.load('Sprites/animationplayer/adventurer-attack2-03.png'))
        self.attack.append(pygame.image.load('Sprites/animationplayer/adventurer-attack2-04.png'))

        self.hurt = []
        self.hurt.append(pygame.image.load('Sprites/animationplayer/adventurer-hurt-00.png'))
        self.hurt.append(pygame.image.load('Sprites/animationplayer/adventurer-hurt-01.png'))
        self.hurt.append(pygame.image.load('Sprites/animationplayer/adventurer-hurt-02.png'))

        self.die = []
        self.die.append(pygame.image.load('Sprites/animationplayer/adventurer-die-00.png'))
        self.die.append(pygame.image.load('Sprites/animationplayer/adventurer-die-01.png'))
        self.die.append(pygame.image.load('Sprites/animationplayer/adventurer-die-02.png'))
        self.die.append(pygame.image.load('Sprites/animationplayer/adventurer-die-03.png'))
        self.die.append(pygame.image.load('Sprites/animationplayer/adventurer-die-04.png'))
        self.die.append(pygame.image.load('Sprites/animationplayer/adventurer-die-05.png'))
        self.die.append(pygame.image.load('Sprites/animationplayer/adventurer-die-06.png'))

        self.loserscreen = []
        self.loserscreen.append(pygame.image.load('Sprites/GameOver/gameover_0.png'))
        self.loserscreen.append(pygame.image.load('Sprites/GameOver/gameover_1.png'))
        self.loserscreen.append(pygame.image.load('Sprites/GameOver/gameover_2.png'))
        self.loserscreen.append(pygame.image.load('Sprites/GameOver/gameover_3.png'))
        self.loserscreen.append(pygame.image.load('Sprites/GameOver/gameover_4.png'))
        self.loserscreen.append(pygame.image.load('Sprites/GameOver/gameover_5.png'))
        self.loserscreen.append(pygame.image.load('Sprites/GameOver/gameover_6.png'))

        
        #these are the index for the player's animation images
        self.idleimg = 0
        self.hurtimg = 0
        self.runimg = 0
        self.jumpimg = 0
        self.runbackimg = 0
        self.attackimg = 0
        self.dieimg = 0
        self.overscreen = 0

        #the x cords
        self.x = 0
        #the y cords
        self.y = 250
         
        #this place the player in there default x to y cords and gives it a rect place holder of 10,10 which would be changed later in the code
        self.rect = pygame.Rect(self.x, self.y, 10, 10)
    
    #this function is activated when the user press the keys 
    def handle_keys(self):
        #if the user walks off the screen this will place them back to -20 on the x cords
        if self.x < -20:
            self.x = -20
        #if the user walks off the screen this will place them back to 520 on the x cords
        if self.x > 520:
            self.x = 520
        #if the index goes over how many images there are the index will set back to 0 which is the first image of the animation
        if self.idleimg >= len(self.idle):
            self.idleimg = 0
        if self.runimg >= len(self.run):
            self.runimg = 0
        if self.jumpimg >= len(self.jump):
            self.jumpimg = 0
        if self.runbackimg >= len(self.runback):
            self.runbackimg = 0
        if self.attackimg >= len(self.attack):
            self.attackimg = 0

        key = pygame.key.get_pressed()
        dist = 10 #how fast the player be moving
        if key[pygame.K_RIGHT]: # right key
            self.y = 300
            self.image = self.run[self.runimg]
            self.runimg += 1
            self.x += dist # move right

        elif key[pygame.K_LEFT]:#left key
            self.y = 300
            self.image = self.runback[self.runbackimg]
            self.runbackimg += 1
            self.x -= dist

        elif key[pygame.K_UP]:#jumping key
            self.y = 275
            self.image = self.jump[self.jumpimg]
            self.jumpimg += 1


        elif key[pygame.K_SPACE]:#Attack key
            self.y = 300
            self.image = self.attack[self.attackimg]
            self.attackimg += 1

                
        else:#defualt the player be in idle if no keys are pressed
            self.image = self.idle[self.idleimg]
            self.idleimg += 1
            self.y = 300
        
        #this gives the player a new rect which can actually be detected by other sprites 
        self.rect = pygame.Rect(self.x, self.y, 0,0 ).inflate(40,100)
    #changes the animation to a hurt img had to spell hurt with two t's wouldnt work with just 1
    def hurtt(self):
        self.hurtimg += 1
        if self.hurtimg >= len(self.hurt):
            self.hurtimg = 0
        self.image = self.hurt[self.hurtimg]

    def dies(self):
        self.dieimg += 1

        if self.dieimg >= len(self.die):
            self.dieimg = 6

        self.image = self.die[self.dieimg]
    
    #returns the self.x so it'll always knows what the x cords are
    def pos(self):
        x = (self.x, self.y)
        return x
    
    def collison_box(self):
        return self.rect

#enemy sprite currently only have skelly on the screen
class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(enemy, self).__init__()
        #skellys walking animation
        self.walk = []
        self.walk.append(pygame.image.load('Sprites/Enemies/skelly/skeleton_00.png'))
        self.walk.append(pygame.image.load('Sprites/Enemies/skelly/skeleton_01.png'))
        self.walk.append(pygame.image.load('Sprites/Enemies/skelly/skeleton_02.png'))
        self.walk.append(pygame.image.load('Sprites/Enemies/skelly/skeleton_03.png'))
        self.walk.append(pygame.image.load('Sprites/Enemies/skelly/skeleton_04.png'))
        self.walk.append(pygame.image.load('Sprites/Enemies/skelly/skeleton_05.png'))
        self.walk.append(pygame.image.load('Sprites/Enemies/skelly/skeleton_06.png'))
        self.walk.append(pygame.image.load('Sprites/Enemies/skelly/skeleton_07.png'))
        self.walk.append(pygame.image.load('Sprites/Enemies/skelly/skeleton_08.png'))
        self.walk.append(pygame.image.load('Sprites/Enemies/skelly/skeleton_09.png'))
        self.walk.append(pygame.image.load('Sprites/Enemies/skelly/skeleton_10.png'))
        self.walk.append(pygame.image.load('Sprites/Enemies/skelly/skeleton_11.png'))
        self.walk.append(pygame.image.load('Sprites/Enemies/skelly/skeleton_12.png'))

        #skellys attack animation
        self.attack = []
        self.attack.append(pygame.image.load('Sprites/Enemies/skelly/skelly_attack-00.png'))
        self.attack.append(pygame.image.load('Sprites/Enemies/skelly/skelly_attack-01.png'))
        self.attack.append(pygame.image.load('Sprites/Enemies/skelly/skelly_attack-02.png'))
        self.attack.append(pygame.image.load('Sprites/Enemies/skelly/skelly_attack-03.png'))
        self.attack.append(pygame.image.load('Sprites/Enemies/skelly/skelly_attack-04.png'))
        self.attack.append(pygame.image.load('Sprites/Enemies/skelly/skelly_attack-05.png'))
        self.attack.append(pygame.image.load('Sprites/Enemies/skelly/skelly_attack-06.png'))
        self.attack.append(pygame.image.load('Sprites/Enemies/skelly/skelly_attack-07.png'))
        self.attack.append(pygame.image.load('Sprites/Enemies/skelly/skelly_attack-08.png'))
        self.attack.append(pygame.image.load('Sprites/Enemies/skelly/skelly_attack-09.png'))
        self.attack.append(pygame.image.load('Sprites/Enemies/skelly/skelly_attack-10.png'))
        self.attack.append(pygame.image.load('Sprites/Enemies/skelly/skelly_attack-11.png'))
        self.attack.append(pygame.image.load('Sprites/Enemies/skelly/skelly_attack-12.png'))
        self.attack.append(pygame.image.load('Sprites/Enemies/skelly/skelly_attack-13.png'))
        self.attack.append(pygame.image.load('Sprites/Enemies/skelly/skelly_attack-14.png'))
        self.attack.append(pygame.image.load('Sprites/Enemies/skelly/skelly_attack-15.png'))
        self.attack.append(pygame.image.load('Sprites/Enemies/skelly/skelly_attack-16.png'))
        self.attack.append(pygame.image.load('Sprites/Enemies/skelly/skelly_attack-17.png'))
        #skellys default x and y cords
        self.x = 600
        self.y = 275
        #image index 
        self.index = 0
        #gives player a rect
        self.rect = pygame.Rect(self.x, self.y, 0, 0)
    #this changes the mode of the skelly for example when he attacks thats because the dist was changed to 0 but his walking animation will only activate when dist is set to 2
    def mode(self,speed):
        self.dist = speed

    #this updates all the info and animations going on with skelly
    def update(self):
        if self.dist == 2:
            if self.index >= len(self.walk):
                self.index = 0
            self.y = 275
            self.image = self.walk[self.index]
        else:
            if self.index >= len(self.attack):
                self.index = 0
            self.y = 265
            self.image = self.attack[self.index]
        self.index += 1
        self.x -= self.dist
        if self.x < -100:
            self.x = 600
        self.rect = pygame.Rect(self.x, self.y, 0, 0).inflate(50,105)

   #like the one in MySprite class this returns the x cords for the enemy
    def pos(self):
        x = (self.x, self.y)
        return x
    #returns the rect so i can pin point his hit box
    def collison_box(self):
        return self.rect
        
   #returns the index of the images
    def index(self):
        return self.index

Sprite = pygame.sprite.Sprite

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class Ground(Sprite):
    def __init__(self, image,x,y):
        Sprite.__init__(self)
        self.image = image
        self.rect = image.get_rect(x=x, y=y)

class Health(pygame.sprite.Sprite):
    def __init__(self):
        super(Health, self).__init__()
        self.health = []
        self.health.append(pygame.image.load('Sprites/Health/health_00.png'))
        self.health.append(pygame.image.load('Sprites/Health/health_01.png'))
        self.health.append(pygame.image.load('Sprites/Health/health_02.png'))
        self.health.append(pygame.image.load('Sprites/Health/health_03.png'))
        self.health.append(pygame.image.load('Sprites/Health/health_04.png'))
        self.health.append(pygame.image.load('Sprites/Health/health_05.png'))
        self.health.append(pygame.image.load('Sprites/Health/health_06.png'))
        self.health.append(pygame.image.load('Sprites/Health/health_07.png'))
        self.health.append(pygame.image.load('Sprites/Health/health_08.png'))
        self.health.append(pygame.image.load('Sprites/Health/health_09.png'))
        self.health.append(pygame.image.load('Sprites/Health/health_10.png'))
        self.health.append(pygame.image.load('Sprites/Health/health_11.png'))
        self.health.append(pygame.image.load('Sprites/Health/health_12.png'))
        self.health.append(pygame.image.load('Sprites/Health/health_13.png'))
        self.health.append(pygame.image.load('Sprites/Health/health_14.png'))
        self.health.append(pygame.image.load('Sprites/Health/health_15.png'))
        self.health.append(pygame.image.load('Sprites/Health/health_16.png'))
        self.health.append(pygame.image.load('Sprites/Health/health_17.png'))
        self.health.append(pygame.image.load('Sprites/Health/health_18.png'))
        self.index = 0
        self.image = self.health[self.index]
        self.rect = pygame.Rect(0, 0, 0, 0)

    #allows the heart images to be updated to indicate the players being hurt
    def damagetaken(self):
        self.index +=1
        if self.index >= len(self.health):
            self.index = 18
        self.image = self.health[self.index]
        self.rect = pygame.Rect(0, 0, 0, 0)
    def index():
        return self.index
class GameOver(pygame.sprite.Sprite):
    def __init__(self):
        super(GameOver, self).__init__()
        self.loserscreen = []
        self.loserscreen.append(pygame.image.load('Sprites/GameOver/gameover_0.png'))
        self.loserscreen.append(pygame.image.load('Sprites/GameOver/gameover_1.png'))
        self.loserscreen.append(pygame.image.load('Sprites/GameOver/gameover_2.png'))
        self.loserscreen.append(pygame.image.load('Sprites/GameOver/gameover_3.png'))
        self.loserscreen.append(pygame.image.load('Sprites/GameOver/gameover_4.png'))
        self.loserscreen.append(pygame.image.load('Sprites/GameOver/gameover_5.png'))
        self.loserscreen.append(pygame.image.load('Sprites/GameOver/gameover_6.png'))
        self.overscreen = 0
        self.image = self.loserscreen[self.overscreen]
        self.rect = pygame.Rect(200, 100, 0, 0)

    def gameover(self):
        self.overscreen += 1

        if self.overscreen >= len(self.loserscreen):
            self.overscreen = 6

        self.image = self.loserscreen[self.overscreen]
def main():
    #sets the speed of the enemy sprite
    enemy.mode(enemy,2)
    #sets the background to an image
    BackGround = Background('Sprites/BackGround/bg.jpg', [0,-100])
    #sets the size of the screen
    screen = pygame.display.set_mode(SIZE)
    #sets the class to variable it makes it easier to be called
    my_sprite = MySprite()

    Game_over = GameOver()
    #does the same just so it be easier
    enemy_sprite = enemy()
    #makes a group for the player sprite
    my_group = pygame.sprite.Group(my_sprite)
    Over_group = pygame.sprite.Group(Game_over)
    #makes it easier to be called on
    heart_sprites = Health()
    #makes a group for the heart sprites
    health_group = pygame.sprite.Group(heart_sprites)
    #makes a group for the enemy sprite
    enemy_group=pygame.sprite.Group(enemy_sprite)
    #sets collison box for player sprite
    rect1 = my_sprite.collison_box()
    #fps for the game
    clock = pygame.time.Clock()
    #creates a group for the tiles images to be put into
    tiles = pygame.sprite.Group()
    #starting point of where the tiles will be placed
    x_cords = 0
    images = {}
    images['Bricks'] = pygame.image.load('Sprites/Ground/grey_brick/grey_brick_center.png').convert_alpha()
    for i in range(0,12):
        tiles.add(Ground(images['Bricks'], x_cords, 322))
        tiles.add(Ground(images['Bricks'], x_cords, 372))
        x_cords += 50
 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        my_group.update()
        screen.fill('white')
        rect1 = my_sprite.collison_box()
        rect2 = enemy_sprite.collison_box()
        screen.blit(BackGround.image, BackGround.rect)
        tiles.draw(screen)
        enemy_group.update()
        Over_group.update()
        health_group.update()
        enemy_group.draw(screen)
        health_group.draw(screen)
        if heart_sprites.index == 18:
            my_sprite.dies()
            Game_over.gameover()
            Over_group.draw(screen)
        else:
            my_sprite.handle_keys()
            if enemy_sprite.index == 14:
                heart_sprites.damagetaken()
                my_sprite.hurtt()
            collide = rect1.colliderect(rect2)
            if collide and heart_sprites.index != 18:
                enemy.mode(enemy,0) 
            else:
                enemy.mode(enemy,2)
        my_group.draw(screen)
        pygame.display.update()
        pygame.display.flip()
        clock.tick(10)
 
if __name__ == '__main__':
    main()