import pygame
pygame.init()

pygame.display.set_mode((500,500));
window=pygame.display.set_mode((500,500));

x_coor=250
y_coor=250

height=50
width=50
running=True


while running: #game loop begins
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if x_coor>0:
            x_coor-=0.1


    elif keys[pygame.K_RIGHT]:
        if x_coor+width<500:
            x_coor+=0.1


    elif keys[pygame.K_UP]:
        if y_coor>0:
            y_coor -= 0.1

    elif keys[pygame.K_DOWN]:
        if y_coor+height<500:
            y_coor += 0.1

    window.fill((0,0,0))
    pygame.draw.rect(window, (255, 0, 0), (x_coor, y_coor, width, height))
    pygame.display.update()