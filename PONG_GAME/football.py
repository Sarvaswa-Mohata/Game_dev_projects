import pygame
import sys

def ball_animation() :
    global ball_speed_x, ball_speed_y
    ball[0]+=ball_speed_x
    ball[1]+=ball_speed_y

    if (ball[1]<=ball_image.get_height()/2-40 or ball[1]>=screen_height-ball_image.get_height()-30) :
        ball_speed_y *= -1
    if (ball[0]<=ball_image.get_width()/2-60 or ball[0]>=screen_width-ball_image.get_width()-30):
        ball_speed_x *= -1
    
    if (ball[0]==player.left and (ball[1]>=player.top and ball[1]<=player.bottom)):
        ball_speed_x *= -1

    if (ball[0]==opponent.right and (ball[1]>=opponent.top and ball[1]<=opponent.bottom)):
        ball_speed_x *= -1

def player_animation() :
    
    player.y+=player_speed
    if player.top <=0:
        player.top =0
    if player.bottom >=screen_height :
        player.bottom = screen_height

def opponent_ai():
    if opponent.top < ball[1]:
        opponent.top += opponent_speed
    if opponent.bottom > ball[1]:
        opponent.bottom -=opponent_speed
    if opponent.top <=0:
        opponent.top =0
    if opponent.bottom >=screen_height :
        opponent.bottom = screen_height

#General setup
pygame.init()
clock = pygame.time.Clock()
FPS=60

#Setting up the main window
screen_width = 1280
screen_height = 960
DISPLAY = (screen_width,screen_height)
BALL_DIM = (150,150)
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')

#Game Rectangles
ball_image = pygame.image.load('Assets/Football.png')
ball_image = pygame.transform.scale(ball_image,BALL_DIM)
bg_img = pygame.image.load('Assets/Football_field_bg.png')
bg_img = pygame.transform.scale(bg_img,DISPLAY)
ball = [screen_width/2 - ball_image.get_width()/2, screen_height/2 - ball_image.get_height()/2]
ball_loc = ball_image.get_rect()
ball_loc.center = ball[0],ball[1]
player=pygame.Rect(screen_width -125,screen_height/2 -70, 10, 180)
opponent = pygame.Rect(120, screen_height/2 - 70, 10, 180)
light_grey =(250,250,250)

ball_speed_x =10
ball_speed_y =10
player_speed = 0
opponent_speed =10
while True:
    #Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 15
            if event.key == pygame.K_UP:
                player_speed -= 15
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 15
            if event.key == pygame.K_UP:
                player_speed += 15
        
    ball_animation()
    player_animation()
    opponent_ai()

    #Visuals
    screen.blit(bg_img, (0,0))
    pygame.draw.rect(screen,light_grey, player)
    pygame.draw.rect(screen,light_grey,opponent)
    screen.blit(ball_image, ball)


    
    #updating the window
    pygame.display.flip()
    clock.tick(FPS)
    