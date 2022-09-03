from time import sleep
import pygame
import random
import numpy as np
from scipy.special import fresnel
 
# Initialize the game engine
pygame.init()
 
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
 
# Set the height and width of the screen
SIZE = [400, 400]
 
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Snow Animation")
 
# Create an empty array
snow_list = []
 
# Loop 50 times and add a snow flake in a random x,y position
for i in range(50):
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    # snow_list.append([x, y])

lspc = np.linspace(0, 10, 1000) # (0, 1, 100)
S, C = fresnel(lspc)
for i in range(len(S)):
    group = []
    for j in range(10):
        shift_x = random.randrange(-10, 10)
        shift_y = random.randrange(-10, 10)
        group.append([S[(i+j*100)%1000]*400/0.8, C[(i+j*100)%1000]*400/0.8])
        # group.append([S[i]*400/0.8, C[i]*400/0.8])
    snow_list.append(group)
 
clock = pygame.time.Clock()
 
# Loop until the user clicks the close button.
done = False
cnt = 0
while not done:
 
    for event in pygame.event.get():   # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True   # Flag that we are done so we exit this loop
 
    # Set the screen background
    screen.fill(BLACK)
 
    # Process each snow flake in the list
    # for i in range(len(snow_list)):
 
        # Draw the snow flake
        # 
    cnt = ((cnt + 1) % len(S) + 400) % len(S) 
    print(cnt)
    for j in range(10):
        pygame.draw.circle(screen, WHITE, snow_list[cnt][j], 2)
    pygame.display.flip()
    pygame.time.wait(10)
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