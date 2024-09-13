import sys
from  game import Game
import pygame
from colors import Colors
pygame.init()
clock = pygame.time.Clock()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
dark_blue = (44, 44, 127)

game = Game()

MOVEDOWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(MOVEDOWN_EVENT, 300)

font = pygame.font.Font(None, 30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.moveLeft()
            if event.key == pygame.K_RIGHT:
                game.moveRight()
            if event.key == pygame.K_DOWN:
                game.score += 1
                game.moveDown()
            if event.key == pygame.K_UP:
                game.rotate_block()
        if event.type == MOVEDOWN_EVENT:
            game.moveDown()
            game.get_score()


    screen.fill(dark_blue)
    game.draw(screen)

    score_surface = font.render(f'Score: {game.score}', True, (255, 255, 255))
    score_rect = score_surface.get_rect(center=(350, 50))
    screen.blit(score_surface, score_rect)

    pygame.display.update()
    clock.tick(60)
