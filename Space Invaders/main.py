import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH = 900
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

white = 255,255,255
black = 0,0,0
red = 255,0,0
yellow = 255,255,0
border = pygame.Rect((WIDTH//2,0), 10, HEIGHT)

health_font = pygame.font.SysFont("comicsans", 45)
winner_font = pygame.font.SysFont("futura", 75)

fps = 60
vel = 5
bullet_vel = 7
max_bullets = 5
player_width = 55
player_height = 40

enemy_red_img = pygame.image.load("./images/spaceship_red.png")
enemy_red_scale = pygame.transform.scale(enemy_red_img, (player_width, player_height))
enemy_red = pygame.transform.rotate(enemy_red_scale, 270)

enemy_yellow_img = pygame.image.load("./images/spaceship_yellow.png")
enemy_yellow_scale = pygame.transform.scale(enemy_yellow_img, (player_width, player_height))
enemy_yellow = pygame.transform.rotate(enemy_yellow_scale, 90)

bg = pygame.image.load("./images/spacebg.png")
bg_scaled = pygame.transform.scale(bg, (WIDTH, HEIGHT))

def draw_screen(red,yellow,red_bullet,yellow_bullet,red_health,yellow_health,bg):
    screen.blit(bg_scaled, (0,0))
    pygame.draw.rect(screen, white, border)
    red_health_text = health_font.render("Health: " + str(red_health), 1, white)
    yellow_health_text = health_font.render("Health: " + str(yellow_health), 1, white)
    screen.blit(red_health_text, (WIDTH-red_health_text.get_width()-10, 20))
    screen.blit(red_health_text, (10, 20))
