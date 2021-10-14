import pygame, sys

pygame.init()
clock=pygame.time.Clock()
screen = pygame.display.set_mode((400,600))

player=pygame.Rect(200,500,30,30)
playerSpeed=20
enemy=pygame.Rect(70,50,40,40)
enemyspeed= -2;

while True:    
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            #Code to move the player towards left.
            if event.key == pygame.K_LEFT:
                player.x -=playerSpeed
            #Add code here, to move the player towards right.
         
    enemy.x= enemy.x + enemyspeed
    
    if enemy.x == 0:
        enemyspeed=enemyspeed * -1
        enemy.y= enemy.y + 20
    
    if enemy.x == 380: 
        enemyspeed=enemyspeed * -1
        enemy.y= enemy.y + 20
    
           
    pygame.draw.rect(screen,(123,200,100),enemy)
    pygame.draw.rect(screen,(23,100,100),player)
    
    
    pygame.display.update()
    clock.tick(30)

