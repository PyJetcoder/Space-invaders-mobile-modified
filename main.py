#programmed by Jeet Kashyap
#made with pygame
import random

import button

import math

import pygame
from pygame import mixer

#initialize pygame.
pygame.init()

#buttons
exit_img = pygame.image.load('exit_btn.png')
exit_button = button.Button(800, 10, exit_img, 0.8)
left_img = pygame.image.load('left-arrow.png')
left_button = button.Button(10, 1000, left_img, 0.8)
right_img = pygame.image.load('right-arrow.png')
right_button = button.Button(900, 1000, right_img, 0.8)
next_img = pygame.image.load('next-arrow.png')
next_button = button.Button(800, 650, next_img, 0.8)
shootbtn_img = pygame.image.load('shootbtn.png')
shoot_button = button.Button(1000, 500, shootbtn_img, 0.8)
#screen and surface
screen=pygame.display.set_mode((0,0))
pygame.display.set_caption('Space Invaders')
width, height= screen.get_size()
#scrolling background and sound
bg1_sound = mixer.Sound('background2.wav')        
bg1_sound.play(-1)	   	   	   
background = pygame.image.load('back.png').convert()
bg_width = background.get_width()
scroll = 0
tiles = math.ceil(10000 / bg_width)
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
    enemyX.append(random.randint(64, 936))
    enemyY.append(random.randint(100, 400))
    enemyX_change.append(5)
    enemyY_change.append(20)
    
def enemy(x,y, i):
    screen.blit(enemyImg[i], (x, y))
        
    
#boss
bossImg = pygame.image.load('boss.png')
bossX = random.randint(100,700)
bossY = random.randint(100,300)
bossX_change = 13
bossY_change = 20
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
    screen.blit(bulletImg, (x+48, y-20))
    
    
#Boss bullet    
BossbulletImg=pygame.image.load('bossbullet.png')
boss_bulletX= bossX
boss_bulletY= bossY
boss_bulletX_change = 0
boss_bulletY_change = 30
def boss_bullet_fire(x,y):
     screen.blit(BossbulletImg, (x+150, y+40))
        
    
#collision function
def Collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt( (math.pow(enemyX - bulletX,2) ) + (math.pow(enemyY - bulletY,2) ) )
    if distance <= 60:
        return True
    else:
        return False
        
    
def BossCollision(bossX, bossY, bulletX, bulletY):
    distance = math.sqrt( (math.pow(bossX - bulletX,2) ) + (math.pow(bossY - bulletY,2) ) )
    if distance <= 100:
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
    highlight_score = font_score_highlight.render("Score :" + str(score_value), True, (0,255,0))
    screen.blit(highlight_score,(x, y))
    
    
#lives
lives_value = 5
font_lives = pygame.font.Font('freesansbold.ttf',50)
livestxtX = 10
livestxtY = 60
def lives(x,y):
    lives = font_lives.render("Lives :" + str(lives_value), True, (255,0,0))
    screen.blit(lives,(x, y))
        
                                            
#Game over
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
   

#highest score
font_highscore = pygame.font.Font('freesansbold.ttf',50)       
def getHighestscore():
    with open('highest_score.txt','r') as f:
        return f.read()
        
        
name_input= " "
HiName = "Hello " + name_input
name = font_highscore.render(HiName, True, (0,255,0))
run=True   
running=False
while run:
    screen.fill((0,255,255))
    font_ctrl = pygame.font.Font('freesansbold.ttf',100)
    controls_text1 = font_ctrl.render("Controls-", True, (255,0,0))
    controls_text2 = font_ctrl.render("Use buttons to move and fire", True, (255,0,0)) 
    controls_text3 = font_ctrl.render("Or arrow keys to move and space to fire", True, (255,0,0))
    controls_text4 = font_ctrl.render("Game is better in landscape(android)", True, (255,0,0))
    controls_text5 = font_ctrl.render("Press Enter or next button to start.", True, (255,0,0))
    screen.blit(controls_text1,(10, 100))
    screen.blit(controls_text2,(10, 200))
    screen.blit(controls_text3,(10, 300))
    screen.blit(controls_text4,(10, 400))
    screen.blit(controls_text5,(10, 500))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_KP_ENTER:
                running = True
                run = False
            elif event.key == pygame.K_BACKSPACE:
                name_input = name_input[0:-1] 
            else:
                name_input += event.unicode      
                     
    screen.blit(name,(10,600))         
    if next_button.draw(screen):  
        running = True
        run = False
            
    pygame.display.update()    
    
clock=pygame.time.Clock()
start = 600

while running:     
    #Display background color:
    #The 3 values are RGB(Red,Green Blue);Any color can be created using these 3 colors
    #The value for each are limited from 0 to 255
    screen.fill((0,255,255))    
    for i in range(0, tiles):
        screen.blit(background, ( i * bg_width + scroll - 10, 0))       
        
    scroll = 5 
               
    if exit_button.draw(screen):
        running=False
            
    if left_button.draw(screen):
        playerX_change = -40
        playerX += playerX_change
            
    if right_button.draw(screen):
        playerX_change = 40
        playerX += playerX_change
                    	
    if shoot_button.draw(screen):
        if bullet_state == "ready":
            bullet_sound = mixer.Sound('shoot.wav')
            bullet_sound.play()
            bulletX = playerX
            bullet_fire(bulletX,bulletY)
            bulletY += bulletY_change        
                            	
   #operating of levels
    if score_value <= 9:
        levels(levelX,levelY) 
                    
    if score_value >= 10:   
        if score_value <= 29:  
            for l in range(num_of_enemies):
                if enemyY[l] <= 1000:
                    enemyX_change[l] = 7
                          
            level = font_level.render("Level 2", True, (0,255,255))
            increment = 2
            levels(levelX,levelY)
            if score_value == 10:
                level_sound.play()
                score_value += 2
        
    if score_value >= 30:        
        if score_value <= 99:
            for k in range(num_of_enemies):
                if enemyY[k] <= 1000:
                    enemyX_change[k] = 9
                        
            level = font_level.render("Level 3", True, (255,255,0))
            increment = 5            
            levels(levelX,levelY)
            if score_value == 30:
                level_sound.play()
                score_value += 5
            
    if score_value >= 100:
        if score_value <= 299:
            for n in range(num_of_enemies):
                if enemyY[n] <= 1000:
                    enemyX_change[n] = 11
                        
            level = font_level.render("Level 4", True, (255,97,3))
            increment = 10        
            levels(levelX,levelY)
            if score_value == 100:
                level_sound.play()
                score_value += 10
                        
    if score_value >= 300:
        for m in range(num_of_enemies):
            if enemyY[m] <= 1000:
                enemyX_change[m] = 13
                        
        if score_value == 300:
            level_sound.play()
            score_value += 20
                        
        boss(bossX,bossY)
        bossX += bossX_change
        level = font_level.render("Max level", True, (255,0,0))
        increment = 20          
        levels(levelX,levelY)        
        player_right = playerX + 20
        player_left = playerX - 20
        boss_bullet_fire(boss_bulletX, boss_bulletY)
                
        if boss_bulletY >= 900:
            boss_bulletX = bossX
            boss_bulletY = bossY
            boss_bullet_fire(boss_bulletX, boss_bulletY)
                    
        distance = math.sqrt( (math.pow((playerX - 64) - boss_bulletX,2) ) + (math.pow(playerY - boss_bulletY,2) ) )
        if distance <= 50:
            live_sound = mixer.Sound('live.wav')        
            live_sound.play()
            lives_value -= 1
            boss_bulletX = bossX
            boss_bulletY = bossY        
       
        #Boss collision
        Bosscollision = BossCollision(bossX, bossY, bulletX, bulletY)
        if bullet_state == "fire":
            if Bosscollision:              
               explosion_sound = mixer.Sound('explosion.wav')
               explosion_sound.play()
               level_sound.play()
               bulletY= 850
               bullet_state= "ready"    
               score_value += 40 
               bossX = random.randint(100,700)
               bossY = 100      
                                                                        
        boss_bulletY += boss_bulletY_change
        
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False 
    
        if event.type == pygame.VIDEORESIZE:
            width, height = event.w, event.h
                
        if event.type == pygame.KEYDOWN:             
            if event.key == pygame.K_LEFT:
                playerX_change = -40
            elif event.key == pygame.K_a:
                playerX_change = -40
            elif event.key == pygame.K_RIGHT:
                playerX_change = 40
            elif event.key == pygame.K_s:
                playerX_change = 40
            elif event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('shoot.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    bullet_fire(bulletX,bulletY)
                    bulletY += bulletY_change        
                    
            playerX += playerX_change        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_s or event.key == pygame.K_a or event.key == pygame.K_SPACE:
                playerX_change = 0
                
    #boundaries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 872:
        playerX = 872
    
    for i in range(num_of_enemies):                    
        #lives
        if enemyY[i] >= 840 :
            if enemyY[i] <= 900:   
                live_sound = mixer.Sound('live.wav')        
                live_sound.play()        
                enemyY[i] = 2000                    
                lives_value -= 1                              
               
        enemyX[i] += enemyX_change[i]        
        if enemyX[i] <= 0:
            enemyX[i] = 1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 850:
            enemyX[i] = -20
            enemyY[i] += enemyY_change[i]
    
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
                                     
    if bossY >= 650 :
        if bossY <= 900:   
            live_sound = mixer.Sound('live.wav')        
            live_sound.play()        
            bossY = 2000                    
            lives_value -= 1                              
        
    #game over            
    if lives_value <= 0:   
        bulletX= 20000
        bulletY= 20000
        start -= 1
        start_sec= start*2// 60
        lives_value = 0
        game_over_text()
        highlight_score(highlightX,highlightY)
        textY = 3000
        livestxtY = 3000
        bossY= 3000
        font_highscore = pygame.font.Font('freesansbold.ttf',80)
        screen.blit(highscoretxt,(300, 580))
        countdown_text = font_lives.render(f"Auto exit in {start_sec}." , True, (255,0,0))
        screen.blit(countdown_text,(300, 1010))                        
        for f in range (num_of_enemies):
            if enemyY[f] <= 1000:
                enemyY[f] = 3000       
    
        if start <= 0 :
            running = False        
                                 
    #bullet movement
    if bulletY <= 0:
        bulletY  = 850
        bullet_state = "ready"
            
    if bullet_state == "fire":
        bullet_fire(bulletX, bulletY)
        bulletY -= bulletY_change    
                   
    if bossX <= 100:
            bossX = 101
            bossY += bossY_change
    elif bossX >= 700:
            bossX = -1
            bossY += bossY_change         
    
    try:
        highestscore = int(getHighestscore())       
    except:
        highestscore = 0                 
            
    if highestscore <= score_value:
        if lives_value <=0:
            font_newhiscore = pygame.font.Font('freesansbold.ttf',80)
            newHiscore = font_newhiscore.render("New highscore!",True, (255,0,0))
            screen.blit(newHiscore,(300,660))          
                 
        highestscore = score_value
        with open('highest_score.txt','w') as f:
            f.write(str(highestscore))
        
    highscoretxt = font_highscore.render(f"HiScore: {highestscore}", True, (0,255,0))
    if lives_value >= 1:
        screen.blit(highscoretxt,(10, 110))          
        
    clock.tick(60)             
    player(playerX,playerY)                 
    show_score(textX,textY) 
    lives(livestxtX,livestxtY)          
    pygame.display.update()      
