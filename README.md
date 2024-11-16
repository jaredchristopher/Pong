# Pong Game in Python - A Beginner's Guide to Game Development

This project is a simple implementation of the Pong game, created using the Pygame library. The game demonstrates the basic principles of game development and introduces key concepts such as movement, collision detection, scoring, and handling user input. It's designed to help high school girls learn fundamental programming skills and explore the world of computer science and game development.

## Getting Started

To get started, make sure you have Python and Pygame installed on your system. If you don't have Pygame installed, you can install it using the following command:

```
pip install pygame
```
## How the Game Works

The game is a two-player Pong game where players control paddles to hit a ball back and forth. The first player uses the W and S keys to move their paddle up and down, while the second player uses the Up and Down arrow keys.

Objective:
The goal is to prevent the ball from passing your paddle. If the ball crosses your paddle's side of the screen, the opponent scores a point.
The first player to reach a set number of points wins the game (for this implementation, the score increases each time the ball crosses the screen).
Key Concepts Covered

1. Setting Up the Game Window
The game window is initialized with a specified width and height using Pygame’s pygame.display.set_mode() function. The caption of the window is set to Pong.

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')
2. Handling User Input
The game listens for key presses (using pygame.key.get_pressed()) so that the players can control their paddles. The player moves up and down by pressing the W, S (for Player 1) and Up, Down arrows (for Player 2).
```
if keys[pygame.K_w] and player1.top > 0:
    player1.y -= player_speed
if keys[pygame.K_s] and player1.bottom < screen_height:
    player1.y += player_speed
```
3. Movement and Physics
The ball moves across the screen at a fixed speed, and when it hits the top or bottom edges, it bounces back. The ball changes direction when it collides with the paddles.

```
ball.x += ball_speed_x
ball.y += ball_speed_y
```

4. Collision Detection
When the ball collides with the paddles or the edges of the screen, it changes direction. This is done using pygame.Rect.colliderect() to check for intersections between the ball and paddles.

if ball.colliderect(player1) or ball.colliderect(player2):
    ball_speed_x = -ball_speed_x
5. Scoring System
Each time the ball crosses the left or right edge of the screen, a point is awarded to the opposite player. The ball is reset to the center of the screen after each point.

```
if ball.left <= 0:
    player2_score += 1
    ball.center = (screen_width // 2, screen_height // 2)
if ball.right >= screen_width:
    player1_score += 1
    ball.center = (screen_width // 2, screen_height // 2)
```

6. Rendering
Pygame’s pygame.draw.rect() and pygame.draw.ellipse() functions are used to draw the paddles and the ball on the screen. The score is rendered with the pygame.font.Font() method and displayed at the top of the screen using screen.blit().

```
pygame.draw.rect(screen, white, player1)
pygame.draw.rect(screen, white, player2)
pygame.draw.ellipse(screen, white, ball)

score_text = font.render(f'{player1_score}  {player2_score}', True, white)
screen.blit(score_text, (screen_width // 2 - 50, 20))
```

7. Frame Rate Control
The game loop runs continuously, and pygame.time.Clock() is used to control the frame rate, ensuring that the game runs at a smooth and consistent 60 frames per second.

```
clock.tick(60)
```
# How to Play

Player 1 uses the W and S keys to move their paddle up and down.
Player 2 uses the Up and Down arrow keys to move their paddle.
Try to prevent the ball from passing your paddle while aiming to get the ball past your opponent’s paddle.