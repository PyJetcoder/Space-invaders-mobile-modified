import random

import math

import pygame
from pygame import mixer

#initialize pygame.
pygame.init()

#screen
screen=pygame.display.set_mode((1000,1000))

#background and background sound
background = pygame.image.load('back.png')
mixer.music.load('background.mp3')
mixer.music.play(-1)

#Game title and icon
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#Player
playerImg=pygame.image.load('player.png')
playerX= 450
playerY= 850
playerX_change = 0
def player(x,y):
    screen.blit(playerImg, (x, y))


#Enemies
enemyImg = [ ]
enemyX = [ ]
enemyY = [ ]
enemyX_change = [ ]
enemyY_change = [ ]
num_of_enemies = 10
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 850))
    enemyY.append(random.randint(100, 400))
    enemyX_change.append(5)
    enemyY_change.append(20)

def enemy(x,y, i):
    screen.blit(enemyImg[i], (x, y))
    

#boss
bossImg = pygame.image.load('boss.png')
bossX = random.randint(100,700)
bossY = random.randint(100,300)
bossX_change = 10
bossY_change = 40
def boss(x,y):
    screen.blit(bossImg, (x, y))


#bullet    
bulletImg=pygame.image.load('bullet.png')
bulletX= 0
bulletY= 850
bulletX_change = 0
bulletY_change = 40
bullet_state = "ready"
def bullet_fire(x,y):
    global bullet_state
    bullet_state= "fire"
    screen.blit(bulletImg, (x+48, y+20))


#collision function
def Collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt( (math.pow(enemyX - bulletX,2) ) + (math.pow(enemyY - bulletY,2) ) )
    if distance <= 60:
        return True
    else:
        return False
    

#score and highlight score
score_value = 0    
font_score = pygame.font.Font('freesansbold.ttf',50)
textX = 10
textY = 10
increment =1
def show_score(x,y):
    score = font_score.render("Score :" + str(score_value), True, (255,255,255))
    screen.blit(score,(x, y))
    

font_score_highlight = pygame.font.Font('freesansbold.ttf',80)
highlightX = 300
highlightY = 500
def highlight_score(x,y):
    highlight_score = font_score_highlight.render("Score :" + str(score_value), True, (255,0,0))
    screen.blit(highlight_score,(x, y))
    
    
#lives and highlight lives
lives_value = 3  
font_lives = pygame.font.Font('freesansbold.ttf',50)
livestxtX = 10
livestxtY = 60
def lives(x,y):
    lives = font_lives.render("Lives :" + str(lives_value), True, (255,0,0))
    screen.blit(lives,(x, y))


font_lives_highlight = pygame.font.Font('freesansbold.ttf',80)
livehlX = 300
livehlY = 580
def lives_highlight(x,y):
    lives_highlight = font_lives_highlight.render("Lives :" + str(lives_value), True, (255,0,0))
    screen.blit( lives_highlight,(x, y))        
        
                                            
#Game over text
over_font = pygame.font.Font('freesansbold.ttf',100)       
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255,0,0))
    screen.blit(over_text,(200,400))
 
       
#levels
font_level = pygame.font.Font('freesansbold.ttf',70)
levelX = 400
levelY = 10
level = font_level.render("Level 1", True, (0,255,0))
level_sound = mixer.Sound('level.wav')    
def levels(x,y):
    screen.blit(level,(x, y))      
    
    
#Game loop
running=True
while running:
    #Display background color:
    #The 3 values are RGB(Red,Green Blue);Any color can be created using these 3 colors
    #The value for each are limited from 0 to 255
    screen.fill((0,0,0))
    screen.blit(background, (0, 0))

    #operating of levels
    if score_value <= 9:
        levels(levelX,levelY) 
        
    if score_value >= 10:
        if score_value <= 29:
            level = font_level.render("Level 2", True, (0,255,255))
            increment = 2
            levels(levelX,levelY)

    if score_value >= 30:
        if score_value <= 99:
            level = font_level.render("Level 3", True, (255,255,0))
            increment = 5            
            levels(levelX,levelY)
    
    if score_value >= 100:
        if score_value <= 299:
            level = font_level.render("Level 4", True, (255,97,3))
            increment = 10        
            levels(levelX,levelY)
                
    if score_value >= 3:
        bossX += bossX_change
        boss(bossX,bossY)
        level = font_level.render("Max level", True, (255,0,0))
        increment = 20          
        levels(levelX,levelY)             
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False 

        #if keystroke pressed check whether its right or left or up or down
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_q:
                running=False
            elif event.key == pygame.K_LEFT:
                playerX_change = -40
            elif event.key == pygame.K_a:
                playerX_change = -40
            elif event.key == pygame.K_s:
                playerX_change = 40
            elif event.key == pygame.K_RIGHT:
                playerX_change = 40
            elif event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                     bullet_sound = mixer.Sound('shoot.wav')
                     bullet_sound.play()
                     bulletX = playerX
                     bullet_fire(bulletX,bulletY)
                     
            playerX += playerX_change  
                                                       
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT or event.key == pygame.K_s or event.key == pygame.K_s:
                playerX_change = 0                       
    
    #boundaries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 936:
        playerX = 936

    for i in range(num_of_enemies):                    
        #Game over and lives
        if enemyY[i] >= 840 :
            if enemyY[i] <= 900:   
                live_sound = mixer.Sound('live.wav')        
                live_sound.play()        
                enemyY[i] = 2000                    
                lives_value -= 1         
                     
        if lives_value <= 0:            
            lives_value = 0
            game_over_text()
            highlight_score(highlightX,highlightY)
            lives_highlight(livehlX,livehlY)
            textY = 2000
            livestxtY = 2000
            break
            
        enemyX[i] += enemyX_change[i]        
        if enemyX[i] <= 0:
            enemyX[i] = 1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 850:
            enemyX[i] = -1
            enemyY[i] += enemyY_change[i]

        if bossX <= 100:
            bossX = 1
            bossY += bossY_change
        elif bossX >= 700:
            bossX = -1
            bossY += bossY_change              
            
       #collision
        collision = Collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if bullet_state == "fire":
            if collision:
               explosion_sound = mixer.Sound('explosion.wav')
               explosion_sound.play()
               bulletY= 850
               bullet_state= "ready"    
               score_value += increment
               enemyX[i] = random.randint(0, 850)
               enemyY[i] = random.randint(100, 400)   
                    
        enemy(enemyX[i],enemyY[i], i)                                         
                                                                                                             
    #bullet movement
    if bulletY <= 0:
        bulletY  = 850
        bullet_state = "ready"
        
    if bullet_state == "fire":
        bullet_fire(bulletX, bulletY)
        bulletY -= bulletY_change    
     
    player(playerX,playerY)   
    show_score(textX,textY) 
    lives(livestxtX,livestxtY)
    pygame.display.update()