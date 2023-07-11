import pygame
import sys

pygame.init()

# Dimensiones de la ventana
width = 800
height = 600

# Colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Posición inicial del objeto en caída libre
x = width // 2
y = 0

# Velocidad inicial y aceleración
velocidad = 0
aceleracion = 9.8

# Configuración de la ventana
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simulación de caída libre")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Actualización de la posición y velocidad
    velocidad += aceleracion
    y += velocidad

    # Si el objeto llega al suelo, detener la simulación
    if y >= height:
        velocidad = 0
        y = height

    # Dibujar en la ventana
    window.fill(WHITE)
    pygame.draw.circle(window, BLUE, (x, int(y)), 20)
    pygame.display.flip()

    clock.tick(60)