import math
import random
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Pong")

clock = pygame.time.Clock()

def mainGame():
    class Player():
        def __init__(self, img, x, y, y_change):
            self.img = img
            self.x = x
            self.y = y
            self.y_change = y_change

        def draw(self):
            screen.blit(self.img, (self.x, self.y))

    def ball(x, y):
            screen.blit(ballImg, (x, y))

    def isCollision1(x, y, ballX, ballY):
        distance = math.sqrt(math.pow(ballX - x, 2) + math.pow(ballY - y, 2))
        if distance <= 45:
            return True
        else:
            return False

    def isCollision2(x, y, ballX, ballY):
        distance = math.sqrt(math.pow(ballX - x, 2) + math.pow(ballY - y, 2))
        if distance <= 45:
            return True
        else:
            return False

    def wallCollide1(ballX):
        distance = math.sqrt(math.pow(ballX - 0, 2))
        if distance <= 15:
            return True
        else:
            return False
        
    def wallCollide2(ballX):
        distance = math.sqrt(math.pow(ballX - 800, 2))
        if distance <= 15:
            return True
        else:
            return False
                             


    player1_score_font = pygame.font.Font("freesansbold.ttf", 15)

    def player1ScoreFont(x, y):
        score1 = player1_score_font.render("Player 1 score: " + str(player1Score), True, (255, 255, 255))
        screen.blit(score1, (x, y))

    player2_score_font = pygame.font.Font("freesansbold.ttf", 15)

    def player2ScoreFont(x, y):
        score2 = player2_score_font.render("Player 2 score: " + str(player2Score), True, (255, 255, 255))
        screen.blit(score2, (x, y))
    

    player1Score = 0
    player2Score = 0
             

    player1 = Player(pygame.image.load("rectangle.png"), 50, 300, 0)
    player2 = Player(pygame.image.load("rectangle.png"), 718, 300, 0)

    ballImg = pygame.image.load("ball.png")
    ballX = 400
    ballY = 300
    ballX_speed = random.randint(-5, -4)
    ballY_speed = random.randint(4, 5)

    directionsY = [-1, 1]


    running = True
    while running:
        screen.fill((128, 128, 128))
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player1.y_change = -5
                if event.key == pygame.K_s:
                    player1.y_change = 5

                if event.key == pygame.K_UP:
                    player2.y_change = -5
                if event.key == pygame.K_DOWN:
                    player2.y_change = 5

            if event.type == pygame.KEYUP:
                player1.y_change = 0
                player2.y_change = 0

        collision1 = isCollision1(player1.x, player1.y, ballX, ballY)

        if collision1:
            ballX_speed *= -1
            ballY_speed *= random.choice(directionsY)

        collision2 = isCollision2(player2.x, player2.y, ballX, ballY)

        if collision2:
            ballX_speed *= -1
            ballY_speed *= random.choice(directionsY)

        wallCollideOne = wallCollide1(ballX)

        if wallCollideOne:
            ballX = 400
            ballY = 300
            player2Score += 1

        wallCollideTwo = wallCollide2(ballX)

        if wallCollideTwo:
            ballX = 400
            ballY = 300
            player1Score += 1


        if player1.y <= 0:
             player1.y = 0
             
        if player1.y >= 533:
             player1.y = 533

        if player2.y <= 0:
             player2.y = 0
             
        if player2.y >= 533:
             player2.y = 533

        if ballX <= 0:
            ballX_speed *= -1
        

            
        if ballX >= 800:
            ballX_speed *= -1
            

        if ballY <= 0:
            ballY_speed *= -1
        if ballY >= 600:
            ballY_speed *= -1

        player1ScoreFont(340, 20)
        player2ScoreFont(340, 45)
        
        player1.y += player1.y_change
        player2.y += player2.y_change
        ballX += ballX_speed
        ballY += ballY_speed
        
        player1.draw()
        player2.draw()
        ball(ballX, ballY)

        pygame.display.update()

startGame = True
start_font = pygame.font.Font("freesansbold.ttf", 50)

def startFont(x, y):
    text = start_font.render("Press Space To Start", True, (255, 255, 255))
    screen.blit(text, (x, y))
    

while startGame:
    screen.fill((128, 128, 128))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                mainGame()
                startGame = False
    startFont(160, 250)
    pygame.display.update()

