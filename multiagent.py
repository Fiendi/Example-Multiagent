import pygame
import random
import math

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Define screen dimensions
WIDTH, HEIGHT = 800, 600

# Define agent properties
AGENT_RADIUS = 10

# Define obstacle properties
NUM_OBSTACLES = 10
OBSTACLE_MIN_RADIUS = 20
OBSTACLE_MAX_RADIUS = 50

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multi-Agent Cooperation Example")
clock = pygame.time.Clock()

class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), AGENT_RADIUS)

    def move_towards(self, target):
        angle = math.atan2(target[1] - self.y, target[0] - self.x)
        self.x += math.cos(angle)
        self.y += math.sin(angle)

class Obstacle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        pygame.draw.circle(screen, BLACK, (int(self.x), int(self.y)), self.radius)

agents = [Agent(50, HEIGHT//2), Agent(WIDTH-50, HEIGHT//2)]
obstacles = [Obstacle(random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(OBSTACLE_MIN_RADIUS, OBSTACLE_MAX_RADIUS)) for _ in range(NUM_OBSTACLES)]

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for agent in agents:
        for obstacle in obstacles:
            distance = math.sqrt((obstacle.x - agent.x)**2 + (obstacle.y - agent.y)**2)
            if distance < AGENT_RADIUS + obstacle.radius:
                agent.move_towards((random.randint(0, WIDTH), random.randint(0, HEIGHT)))
                break

        for other_agent in agents:
            if other_agent != agent:
                distance = math.sqrt((other_agent.x - agent.x)**2 + (other_agent.y - agent.y)**2)
                if distance < 2 * AGENT_RADIUS:
                    agent.move_towards((random.randint(0, WIDTH), random.randint(0, HEIGHT)))
                    break

        agent.draw()

    for obstacle in obstacles:
        obstacle.draw()

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
