import pygame  # Import the Pygame library for game development
import sys  # Import sys to allow program exit when needed

# ------------------------------------------------------------------

# Initialize Pygame library to set up the game environment
pygame.init()

# Set up the display dimensions (mesured in pixels)
screen_width = 800  # Width of the game window
screen_height = 600  # Height of the game window
screen = pygame.display.set_mode((screen_width, screen_height))  # Create the game window
pygame.display.set_caption('Pong')  # Set the title of the game window

# Define colors using RGB values
black = (0, 0, 0)  # Black color for background
white = (255, 255, 255)  # White color for paddles, ball, and text

# Paddle and ball settings
paddle_width = 10  # Width of the paddles
paddle_height = 100  # Height of the paddles
ball_size = 20  # Size of the ball

player_speed = 6  # Speed of the paddles
ball_speed_x = 5  # Horizontal speed of the ball
ball_speed_y = 5  # Vertical speed of the ball

# Score variables for each player
player1_score = 0  # Score of Player 1 (left paddle)
player2_score = 0  # Score of Player 2 (right paddle)

# Font for displaying the score
font = pygame.font.Font(None, 74)  # Create a font object with size 74

# ------------------------------------------------------------------

# Set the initial positions of the paddles and ball

# Rect is a built in object in pygame that stands for Rectangle
#       pygame.Rect(x, y, width, height)
# "//" is called a floor operator in python it divides number and rounds to the nearest integer
#       ex: 4 // 1.5 = 3
# We need to use this because '/' in python does not always return integers
#       ex: 4 / 1.5 = 2.66666...

player1 = pygame.Rect(30, (screen_height // 2) - (paddle_height // 2), paddle_width, paddle_height)  # Left paddle
player2 = pygame.Rect(screen_width - 40, (screen_height // 2) - (paddle_height // 2), paddle_width, paddle_height)  # Right paddle
ball = pygame.Rect(screen_width // 2, screen_height // 2, ball_size, ball_size)  # Ball at the center of the screen

# Main game loop
clock = pygame.time.Clock()  # Create a clock object to control the frame rate
running = True  # Boolean to keep the game loop running
while running:
    # Handle game events like quitting the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Check if the close button was clicked
            pygame.quit()  # Quit the Pygame application
            sys.exit()  # Exit the program

    # Move the paddles based on key presses
    keys = pygame.key.get_pressed()  # Get a dictionary of pressed keys
    if keys[pygame.K_w] and player1.top > 0:  # Move Player 1 paddle up (W key)
        player1.y -= player_speed
    if keys[pygame.K_s] and player1.bottom < screen_height:  # Move Player 1 paddle down (S key)
        player1.y += player_speed
    if keys[pygame.K_UP] and player2.top > 0:  # Move Player 2 paddle up (Up Arrow key)
        player2.y -= player_speed
    if keys[pygame.K_DOWN] and player2.bottom < screen_height:  # Move Player 2 paddle down (Down Arrow key)
        player2.y += player_speed

    # Move the ball
    ball.x += ball_speed_x  # Update the ball's horizontal position
    ball.y += ball_speed_y  # Update the ball's vertical position

    # Check for ball collision with top and bottom walls
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y = -ball_speed_y  # Reverse vertical direction

    # Check for ball collision with paddles
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x = -ball_speed_x  # Reverse horizontal direction

    # Scoring logic
    if ball.left <= 0:  # If the ball goes off the left side
        player2_score += 1  # Increment Player 2's score
        ball.center = (screen_width // 2, screen_height // 2)  # Reset the ball to the center
        ball_speed_x = -ball_speed_x  # Send ball to the opposite direction
    if ball.right >= screen_width:  # If the ball goes off the right side
        player1_score += 1  # Increment Player 1's score
        ball.center = (screen_width // 2, screen_height // 2)  # Reset the ball to the center
        ball_speed_x = -ball_speed_x  # Send ball to the opposite direction

#-------------------------------------------------------------------------
# Add Code to end game after 5 points have been scored by either player
#-------------------------------------------------------------------------

    # Update the screen with new positions and clear previous frame
    screen.fill(black)  # Fill the background with black
    pygame.draw.rect(screen, white, player1)  # Draw Player 1 paddle
    pygame.draw.rect(screen, white, player2)  # Draw Player 2 paddle
    pygame.draw.ellipse(screen, white, ball)  # Draw the ball

    # Display the scores on the screen
    score_text = font.render(f'{player1_score}  {player2_score}', True, white)  # Render the score text
    screen.blit(score_text, (screen_width // 2 - 50, 20))  # Draw the score text at the top center

    pygame.display.flip()  # Update the display with new visuals every tick
    clock.tick(60)  # Limit the game to 60 frames per second
