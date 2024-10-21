import random

import pygame
import sys

score=0

screen=pygame.display.set_mode((500,500))

fruitx=random.randint(0,24)*20
fruity=random.randint(0,24)*20

pygame.display.set_caption('Snake')
clock=pygame.time.Clock()
s=[(100,120),(120,120),(140,120)]

def draw_snake(l):
    pygame.draw.rect(screen,(255,0,0),(l[0],l[1],20,20))


right=1
left=2
up=3
down=4
def move_snake(direction):
    head_x= s[0][0]
    head_y= s[0][1]
    if direction == right:
        new_head = (head_x + 20, head_y)
    elif direction == left:
        new_head = (head_x - 20, head_y)
    elif direction == up:
        new_head = (head_x, head_y - 20)
    elif direction == down:
        new_head = (head_x, head_y + 20)

    s.insert(0, new_head)

    if fruit_collision()==True:
        pass
    else:
        s.pop()


def check_collision():
    head_x=s[0][0]
    head_y=s[0][1]

    if head_x<0 or head_x>=500 or head_y<0 or head_y>=500:
        return True
    else:
        return False

def fruit_collision():
    head_x = s[0][0]
    head_y = s[0][1]
    if head_x==fruitx and head_y==fruity:
        return True
        
    else:
        return False
    


start=60
direction=right
while True:

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                direction=left
            elif event.key==pygame.K_RIGHT:
                direction=right
            elif event.key==pygame.K_UP:
                direction=up
            elif event.key==pygame.K_DOWN:
                direction=down
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen,(0,255,0),(fruitx,fruity,20,20))
    move_snake(direction)
    start+=20

    if check_collision()==True:
        pygame.quit()
        sys.exit()

    if fruit_collision()==True:
        fruitx = random.randint(0, 24) * 20
        fruity = random.randint(0, 24) * 20


    for co_ordinates in s:
        draw_snake(co_ordinates)
    pygame.display.update()
    clock.tick(5)