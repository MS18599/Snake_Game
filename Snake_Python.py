import pygame
import random
import os
pygame.mixer.init()

pygame.init()
white=(255, 255, 255)
red=(255, 0, 0)
black=(0, 0, 0)

width = 700
height = 500

gamewindow = pygame.display.set_mode((width,height))
gover= pygame.image.load("image1.jpg")
gover = pygame.transform.scale(gover,(width,height)).convert_alpha()
bgimg = pygame.image.load("image.jpg")
bgimg = pygame.transform.scale(bgimg,(width,height)).convert_alpha()

pygame.display.set_caption("Snake_With_Mohit")
pygame.display.update()
#game specific var
clock=pygame.time.Clock()
font = pygame.font.SysFont(None,50)

def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])
def  plot_snake(gamewindow, color, snk_list, snake_size):
    for x,y in snk_list:
            pygame.draw.rect(gamewindow, color ,[x, y, snake_size, snake_size])


def welcome():
    exit_game = False
    while not exit_game:
        gamewindow.fill((222,200,200))
        gamewindow.blit(bgimg, (0, 0))
        text_screen("Welcome To Snake",black,180,200)
        text_screen("Press Space To Play", (244,209,66), 10, 460)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('back.mp3')
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(30)

def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 10
    fps = 30
    velocity_x = 0
    velocity_y = 0
    init_velocity = 5
    food_x = random.randint(20, width)
    food_y = random.randint(0, height)
    score = 0
    snk_list = []
    snk_len = 1
    if not os.path.exists("highscore.txt"):
        with open("highscore.txt","w") as f:
            f.write("0")
    with open("highscore.txt", "r") as f:
        highscore = f.read()
    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            gamewindow.fill(white)
            gamewindow.blit(gover, (0, 0))
            #text_screen("Game Over! press enter to continue.", red,50,200)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN: #press enter
                        welcome()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        #snake_x += 10
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        #snake_x -= 10
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        #snake_y -= 10
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        #snake_y += 10
                        velocity_y = init_velocity
                        velocity_x = 0
            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                score += 10
                food_x = random.randint(20, width / 2)
                food_y = random.randint(20, height / 2)
                snk_len += 5
            if score > int(highscore):
                 highscore = score


            gamewindow.fill(white)
            gamewindow.blit(bgimg, (0,0))
            text_screen("SCORE: "+str(score)+"              HIGHSCORE: "+str(highscore),(20, 55, 104),5,5)
            pygame.draw.rect(gamewindow, red , [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_len:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('over.mp3')
                pygame.mixer.music.play()
            if snake_x<0 or snake_x > width or snake_y < 0 or snake_y > height:
                game_over = True
                pygame.mixer.music.load('over.mp3')
                pygame.mixer.music.play()


            plot_snake(gamewindow, black, snk_list, snake_size)

        pygame.display.update()
        clock.tick(fps)




    pygame.quit()
    quit()
#gameloop()
welcome()