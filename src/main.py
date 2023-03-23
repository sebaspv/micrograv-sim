import pygame
import random

# Iniciar Pygame
pygame.init()

# Configurar la ventana
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Microgravedad")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clase de objetos
class Objeto(pygame.sprite.Sprite):
    def __init__(self, x, y, size, color):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidad_x = random.randint(-2, 2)
        self.velocidad_y = random.randint(-2, 2)

    def update(self):
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y
        if self.rect.left > 800 or self.rect.right < 0:
            self.velocidad_x = -self.velocidad_x
        if self.rect.top > 600 or self.rect.bottom < 0:
            self.velocidad_y = -self.velocidad_y

# Lista de objetos
objetos = pygame.sprite.Group()
for i in range(1):
    objeto = Objeto(random.randint(0, 800), random.randint(0, 600), 20, WHITE)
    objetos.add(objeto)

# Loop del juego
running = True
while running:
    # Eventos del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar los objetos
    objetos.update()

    # Dibujar en la pantalla
    screen.fill(BLACK)
    objetos.draw(screen)
    pygame.display.flip()

# Salir del juego
pygame.quit()
