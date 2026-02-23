import pygame
import serial
import sys

# 🔹 CHANGE COM PORT
ser = serial.Serial('COM7', 115200, timeout=1)

pygame.init()

WIDTH, HEIGHT = 900, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arduino Joystick Drawing")

clock = pygame.time.Clock()

# Canvas area (leave space for buttons)
canvas = pygame.Surface((900, 600))
canvas.fill((0, 0, 0))

cursor_x = 450
cursor_y = 300

font = pygame.font.SysFont(None, 30)

# Button rectangles
clear_button = pygame.Rect(200, 610, 150, 30)
reset_button = pygame.Rect(550, 610, 150, 30)

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if clear_button.collidepoint(event.pos):
                canvas.fill((0, 0, 0))

            if reset_button.collidepoint(event.pos):
                canvas.fill((0, 0, 0))
                cursor_x = 450
                cursor_y = 300

    if ser.in_waiting:
        try:
            data = ser.readline().decode().strip()
            x_val, y_val, button = data.split(",")

            x_val = int(x_val)
            y_val = int(y_val)
            button = int(button)

            # Movement
            if x_val < 400:
                cursor_x -= 5
            if x_val > 600:
                cursor_x += 5
            if y_val > 400:
                cursor_y -= 5
            if y_val < 600:
                cursor_y += 5

            cursor_x = max(0, min(899, cursor_x))
            cursor_y = max(0, min(599, cursor_y))

            # Draw only if D2 HIGH
            if button == 1:
                pygame.draw.circle(canvas, (255, 255, 255), (cursor_x, cursor_y), 3)

        except:
            pass

    # Draw canvas
    screen.fill((30, 30, 30))
    screen.blit(canvas, (0, 0))

    # Draw cursor
    pygame.draw.circle(screen, (0, 255, 0), (cursor_x, cursor_y), 5, 1)

    # Draw buttons
    pygame.draw.rect(screen, (200, 0, 0), clear_button)
    pygame.draw.rect(screen, (0, 0, 200), reset_button)

    screen.blit(font.render("CLEAR", True, (255, 255, 255)), (245, 615))
    screen.blit(font.render("RESET", True, (255, 255, 255)), (595, 615))

    pygame.display.flip()

ser.close()
pygame.quit()
sys.exit()
