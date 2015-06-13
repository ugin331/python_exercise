##
Space Pong
import pygame, sys
from pygame.locals import *
from random import randint

#Height of the game window
WINDOW_HEIGHT = 600
#Width of the game window
WINDOW_WIDTH = 600

#Height and width of game ball
BALL_SIZE = 10
#Color of the game ball
GREEN = pygame.Color("Green")
#color of the paddle
BLUE = pygame.Color("Cyan")
#color of the other paddle
RED = pygame.Color("FireBrick")

#Start Main Function
def main():
    #initializes all imported pygame modules
    pygame.init()
    #create the playing screen
    mainSurface=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    #set the caption for the window
    pygame.display.set_caption('Space Pong')
    #load image for the background
    background_image=pygame.image.load("img/space.gif").convert()
    #resize it to match the window size
    background_image=pygame.transform.scale(background_image,(WINDOW_WIDTH,WINDOW_HEIGHT))
    #Set positions of graphics
    background_position=[0,0]
    #create the rectange that is the ball
    ball=pygame.Rect(WINDOW_WIDTH/2,WINDOW_HEIGHT/2,BALL_SIZE,BALL_SIZE)
    #create the rectangle that is the paddle
    paddle=pygame.Rect(WINDOW_WIDTH/2,WINDOW_HEIGHT-40,100,2)
    faddle=pygame.Rect(WINDOW_WIDTH/2,WINDOW_HEIGHT-40,100,2)
    #initialize clock
    clock = pygame.time.Clock()    
    #set the variable that controls
    #the main game loop
    playing=True
    #set paddle not to move
    paddleMove=0
    faddleMove=0
    #variables to control movment of ball
    ballDx=randint(randint(-4,3),randint(4,6))
    ballDy=randint(randint(-7,-2),randint(1,4))
    #start the game loop
    while playing:
        clock.tick(90)
        #get all the events since last
        #time the events were checked
        for event in pygame.event.get():
            if event.type == QUIT:
                playing = False
            #if the Event is a pressed key
            if event.type == KEYDOWN:
                #if the Q is pressed end the game
                if event.key == K_f:
                    playing = False
                #set the paddle to move to the left
                if event.key == K_d:
                    paddleMove=7
                    faddleMove=-7
                #set the paddle to move to the right
                if event.key == K_a:
                    paddleMove=-7
                    faddleMove=7
            #if this is a keyup (theplayer released the key so it is no longer down)
            if event.type == KEYUP:
                #since the player released the key
                #the paddle should be stationary
                if event.key == K_d or event.key == K_a:
                    paddleMove=0
                    faddleMove=0
        # this is to control the ball so it doesn't go off the screen
        if ball.y<=0 and ballDy<0:
            ballDy=ballDy*-1
        if ball.x<=0 and ballDx<0:
            ballDx=ballDx*-1
        #ifthe ball is moving right and 
        #off the board (x coordinate>screen width)
        if ball.x>=WINDOW_WIDTH - BALL_SIZE and ballDx>0:
            ballDx= - ballDx
            #bounce off paddle
        if ball.colliderect(paddle) and ballDy>0:
            ballDy= - ballDy
        if ball.colliderect(faddle) and ballDy>0:
            ballDy= - ballDy        
        #if ball gets to the bottom of the screen
        if ball.y>=WINDOW_HEIGHT and ballDy>0:
            ball.y=randint(1,599)
            ball.x=randint(1,599)
        #update the position of the ball
        ball.x=ball.x+ballDx
        ball.y=ball.y+ballDy
        #update the position of the paddle
        #paddlemoveis for the x coordinate
        #0 is for the y coordinate (not changing)
        paddle=paddle.move(paddleMove,0)
        faddle=faddle.move(faddleMove,0)
        #Copy background image to screen
        mainSurface.blit(background_image,background_position)
        #draw the ball rectangle
        pygame.draw.rect(mainSurface,GREEN,ball)
        #draw the paddle rectangle
        pygame.draw.rect(mainSurface,BLUE,paddle)
        pygame.draw.rect(mainSurface,RED,faddle)
        #update the display on the main screen
        pygame.display.update()
    
#run the main method when this file is loaded
if __name__=='__main__':
    main()
