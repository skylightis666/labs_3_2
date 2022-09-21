from time import sleep
import pygame
import random
import numpy as np
from scipy.special import fresnel
 
# Initialize the game engine
pygame.init()
 
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GRAY = [115, 147, 179]
DOT_SIZE = 8
 
# Set the height and width of the screen
SIZE = [400, 400]
 
screen = pygame.display.set_mode(SIZE)

pygame.display.set_caption("Snow Animation")
 
# Create an empty array
 
# Loop 50 times and add a snow flake in a random x,y position
for i in range(50):
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    # snow_list.append([x, y])

lspc = np.linspace(0, 10, 1000) # (0, 1, 100)
S, C = fresnel(lspc)
def gen_dots_lines():
    snow_list = []

    for i in range(len(S)):
        group = []
        for j in range(2): #[0.5, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 1.2, 1.4]:
            shift_x = random.randrange(50, 80) / 100
            # shift_y = random.randrange(-10, 10)
            group.append([S[(i+int(shift_x*100))%1000]*400/0.8, C[(i+int(shift_x*100))%1000]*400/0.8])
            shift_x += 0.005
            group.append([S[(i+int(shift_x*100))%1000]*400/0.8, C[(i+int(shift_x*100))%1000]*400/0.8])
            shift_x += 0.005
            group.append([S[(i+int(shift_x*100))%1000]*400/0.8, C[(i+int(shift_x*100))%1000]*400/0.8])
            shift_x += 0.005
            group.append([S[(i+int(shift_x*100))%1000]*400/0.8, C[(i+int(shift_x*100))%1000]*400/0.8])
            shift_x += 0.005
            group.append([S[(i+int(shift_x*100))%1000]*400/0.8, C[(i+int(shift_x*100))%1000]*400/0.8])


            # group.append([S[i]*400/0.8, C[i]*400/0.8])
        snow_list.append(group)

    return snow_list
def gen_dots():
    snow_list = []

    for i in range(len(S)):
        group = []
        for j in range(4): #[0.5, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 1.2, 1.4]:
            shift_x = random.randrange(50, 80) / 100
            group.append([S[(i+int(shift_x*100))%1000]*400/0.8, C[(i+int(shift_x*100))%1000]*400/0.8])

        snow_list.append(group)

    return snow_list
 
clock = pygame.time.Clock()
 
# Loop until the user clicks the close button.
done = False
cnt = 0

dots_list1 = gen_dots_lines()
dots_list2 = gen_dots_lines()
dots_list3 = gen_dots_lines()
dots_list4 = gen_dots_lines()
dots_list5 = gen_dots_lines()
dots_list6 = gen_dots_lines()
# super_list1 = [gen_dots_lines(), gen_dots_lines(), gen_dots_lines(), gen_dots_lines(), gen_dots_lines(), gen_dots_lines(), gen_dots_lines()]
        
# dots_list3 = gen_dots()
cnt = 0
cnt1 = 50
cnt2 = 150
cnt_array = [a*50 for a in range(8) ]
cnt_array_max = [a*50 for a in range(1, 9) ]
was = True
was1 = True
was2 = True
was_array = [True] * 8

DEFAULT_IMAGE_SIZE = (10, 10)
default_img = pygame.image.load('bub.png')
img1 = pygame.transform.scale(default_img, DEFAULT_IMAGE_SIZE)
img2 = pygame.transform.scale(default_img, (20, 20))
img3 = pygame.transform.scale(default_img, (15, 15))
img4 = pygame.transform.scale(default_img, (7, 7))



def segment(cnt1, was1):
    if (random.randrange(0, 2)):
        for j in range(10):
            screen.blit(img1, dots_list1[cnt1][j])
    if (random.randrange(0, 2)):
        for j in range(10):
            if (was1):
                dots_list2[cnt1][j][0] += 15
            screen.blit(img2, dots_list2[cnt1][j])
    if (random.randrange(0, 2)):
        for j in range(10):
            if (was1):
                dots_list3[cnt1][j][0] -= 15
            screen.blit(img3, dots_list3[cnt1][j])
    if (random.randrange(0, 2)):
        for j in range(10):
            if (was1):
                dots_list4[cnt1][j][0] += 15
                dots_list4[cnt1][j][1] -= 15
            screen.blit(img4, dots_list4[cnt1][j])
    if (random.randrange(0, 2)):
        for j in range(10):
            if (was1):
                dots_list5[cnt1][j][0] -= 15
                dots_list5[cnt1][j][1] += 15
            screen.blit(img1, dots_list5[cnt1][j])
    if (random.randrange(0, 2)):
        for j in range(10):
            if (was1):
                dots_list6[cnt1][j][0] += 15
                dots_list6[cnt1][j][0] += 15
            screen.blit(img1, dots_list6[cnt1][j])

while not done:
 
    for event in pygame.event.get():   # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True   # Flag that we are done so we exit this loop
 
    screen.fill(WHITE)

    # if (cnt < 50):
    #     cnt += 1
    # else:
    #     cnt = 0
    #     was = False

    # if (random.randrange(0, 2)):
    #     for j in range(10):
    #         pygame.draw.circle(screen, GRAY, dots_list1[cnt][j], DOT_SIZE)
    # if (random.randrange(0, 2)):
    #     for j in range(10):
    #         if (was):
    #             dots_list2[cnt][j][0] += 15
    #         pygame.draw.circle(screen, GRAY, dots_list2[cnt][j], DOT_SIZE)
    # if (random.randrange(0, 2)):
    #     for j in range(10):
    #         if (was):
    #             dots_list3[cnt][j][0] -= 15
    #         pygame.draw.circle(screen, GRAY, dots_list3[cnt][j], DOT_SIZE)
    # if (random.randrange(0, 2)):
    #     for j in range(10):
    #         if (was):
    #             dots_list4[cnt][j][0] += 15
    #             dots_list4[cnt][j][1] -= 15
    #         pygame.draw.circle(screen, GRAY, dots_list4[cnt][j], DOT_SIZE)
    # if (random.randrange(0, 2)):
    #     for j in range(10):
    #         if (was):
    #             dots_list5[cnt][j][0] -= 15
    #             dots_list5[cnt][j][1] += 15
    #         pygame.draw.circle(screen, GRAY, dots_list5[cnt][j], DOT_SIZE)
    # if (random.randrange(0, 2)):
    #     for j in range(10):
    #         if (was):
    #             dots_list6[cnt][j][0] += 15
    #             dots_list6[cnt][j][0] += 15
    #         pygame.draw.circle(screen, GRAY, dots_list6[cnt][j], DOT_SIZE)

    # if (cnt1 < 150):
    #     cnt1 += 1
    # else:
    #     cnt1 = 50
    #     was1 = False

    # segment(cnt1, was1)

    # if (cnt2 < 250):
    #     cnt2 += 1
    # else:
    #     cnt2 = 150
    #     was2 = False

    # segment(cnt2, was2)

    for j in range(8):
        if (cnt_array[j] < cnt_array_max[j]):
            cnt_array[j] += 1
        else:
            cnt_array[j] = cnt_array_max[j] - 50
            was_array[j] = False
        segment(cnt_array[j], was_array[j])


    # cnt1 = ((cnt1 + 1) % len(S) + 400) % len(S)


    # if (random.randrange(0, 2)):
    #     for j in range(10):
    #         pygame.draw.circle(screen, GRAY, dots_list1[cnt1][j], DOT_SIZE)
    # if (random.randrange(0, 2)):
    #     for j in range(10):
    #         dots_list2[cnt1][j][0] += 15
    #         pygame.draw.circle(screen, GRAY, dots_list2[cnt1][j], DOT_SIZE)
    # if (random.randrange(0, 2)):
    #     for j in range(10):
    #         dots_list3[cnt1][j][0] -= 15
    #         pygame.draw.circle(screen, GRAY, dots_list3[cnt1][j], DOT_SIZE)
    # if (random.randrange(0, 2)):
    #     for j in range(10):
    #         dots_list4[cnt1][j][0] += 15
    #         dots_list4[cnt1][j][1] -= 15
    #         pygame.draw.circle(screen, GRAY, dots_list4[cnt1][j], DOT_SIZE)
    # if (random.randrange(0, 2)):
    #     for j in range(10):
    #         dots_list5[cnt1][j][0] -= 15
    #         dots_list5[cnt1][j][1] += 15
    #         pygame.draw.circle(screen, GRAY, dots_list5[cnt1][j], DOT_SIZE)
    # if (random.randrange(0, 2)):
    #     for j in range(10):
    #         dots_list6[cnt1][j][0] += 15
    #         dots_list6[cnt1][j][0] += 15
    #         pygame.draw.circle(screen, GRAY, dots_list6[cnt1][j], DOT_SIZE)

    # for j in range(4):
    #     if (random.randrange(0, 2) % 2 == 1):
    #         dots_list3[cnt][j][1] += random.randrange(-30, -15)
    #     else: 
    #         dots_list3[cnt][j][1] += random.randrange(15, 30)

    #     pygame.draw.circle(screen, GRAY, dots_list3[cnt][j], 5)

    screen.blit(pygame.transform.rotate(screen, 270), (0, 0))
    screen.blit(pygame.transform.flip(screen, False, True), (0, 0))

    pygame.display.flip()
    pygame.time.wait(60)
    # clock.tick(60)
 
        # Move the snow flake down one pixel
        # snow_list[i][1] += 1
 
        # # If the snow flake has moved off the bottom of the screen
        # if snow_list[i][1] > 400:
        #     # Reset it just above the top
        #     y = random.randrange(-50, -10)
        #     snow_list[i][1] = y
        #     # Give it a new x position
        #     x = random.randrange(0, 400)
        #     snow_list[i][0] = x
 
    # Go ahead and update the screen with what we've drawn.

 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()