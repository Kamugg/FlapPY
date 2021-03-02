import pygame
import Bird
import Pipe

pygame.init()
SCREEN_XSIZE = 300
SCREEN_YSIZE = 400
screen = pygame.display.set_mode((SCREEN_XSIZE, SCREEN_YSIZE))
pygame.display.set_caption('FlapPY')
bird_x = 50  # Bird fixed x
gravity = 0.0008  # Gravity for the bird
score = 0
spawnpoints = [300, 450, 600]  # Initial spawn points of the pipes
pipes = []
for spawn in spawnpoints:  # Adding pipes
    pipes.append(Pipe.Pipe(spawn, SCREEN_YSIZE))
bird = Bird.Bird(200)  # The bird spawns at y = 200
speed = 0.05  # Pipe speed
# Loading all the required images
birdpng = pygame.image.load('bird.png').convert_alpha()
birdpng = pygame.transform.scale(birdpng, (20, 20))
pygame.display.set_icon(birdpng)
background = pygame.rect.Rect(0, 0, SCREEN_XSIZE, SCREEN_YSIZE)
backpng = pygame.image.load('background.png').convert()
backpng = pygame.transform.scale(backpng, (SCREEN_XSIZE, SCREEN_YSIZE))
top_pipe = pygame.image.load('top_pipe.png').convert()
top_pipe = pygame.transform.scale(top_pipe, (50, 30))
# Initializing font to render the score on screen
pygame.font.init()
myfont = pygame.font.SysFont('Arial Bold', 40)
done = False
# Main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:  # Pushing the up key triggers the bird's jump
                bird.jump()
    screen.fill((0, 0, 0))
    screen.blit(backpng, background)  # Background
    bird.move(gravity)  # Moves the bird
    screen.blit(pygame.transform.rotate(birdpng, bird.getangle()),
                birdpng.get_rect(center=bird.getrect().center))  # Showing the bird and rotating it accordingly around it's center
    for pipe in pipes:
        pipe.move(speed)  # Moving pipes
        for p in pipe.getrects():
            # Blitting the pipes on the screen
            # Each pipe class contains two pipes (the higher and the lower one)
            # Each pipe has two images: the top part (standard) and the bottom part (scaled accordingly to the pipe's height)
            # So we have 4 blits calls in total
            screen.blit(top_pipe, (pipe.getpos(), SCREEN_YSIZE - pipe.getheight()))
            screen.blit(pipe.bottomimage, (pipe.getpos(), SCREEN_YSIZE - pipe.getheight() + 30))
            screen.blit(pygame.transform.rotate(top_pipe, 180),
                        (pipe.getpos(), SCREEN_YSIZE - pipe.getheight() - pipe.gap - 30))
            screen.blit(pipe.upperimage, (pipe.getpos(), 0))
    # If the first pipe is no longer on screen is "teleported" back and it's resetted (new height)
    if pipes[0].getpos() <= -50:
        pipes.append(pipes.pop(0))
        pipes[-1].reset()
    # If the bird jumps over the first pipe the score increases
    # If the score is a multiple of 10, the pipes' speed increases a little
    if pipes[0].getpos() < 50 and not pipes[0].scored:
        score += 1
        pipes[0].scored = True
        if score % 10 == 0:
            speed += 0.002
    # Now the death conditions
    # If the bird hits the ground or the ceiling is game over
    if not (0 < bird.getpos() < SCREEN_YSIZE):
        done = True
    # If the bird hits the pipe (the check is only performed when the first pipe on the list is near enough)
    # It's game over
    if 0 <= pipes[0].getpos() <= 80:
        for rect in pipes[0].getrects():
            if bird.getrect().colliderect(rect):
                done = True
    # Rendering the score
    textsurface = myfont.render(str(score), False, (255, 255, 255))
    screen.blit(textsurface, (SCREEN_XSIZE / 2 - textsurface.get_size()[0] / 2, 10))
    pygame.display.update()
