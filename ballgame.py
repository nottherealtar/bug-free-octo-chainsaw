import tkinter as tk
import time

# Constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 20
UPDATE_INTERVAL = 30  # milliseconds
BALL_SPEED = 5

# Variables
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = BALL_SPEED
ball_dy = BALL_SPEED
ball_radius = BALL_RADIUS

# Create the main window
root = tk.Tk()
root.title("Tuples are the death of me")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# Create the ball
ball = canvas.create_oval(ball_x - ball_radius, ball_y - ball_radius,
                          ball_x + ball_radius, ball_y + ball_radius,
                          fill="green")

# Main game loop
while True:
    # Move the ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Check if the ball hits the edges
    if ball_x + ball_radius >= WIDTH or ball_x - ball_radius <= 0:
        ball_dx *= -1
        ball_radius *= 1.04  # Enlarge the ball by 2%
        ball_dx *= 1.04      # Increase speed by 2%
    if ball_y + ball_radius >= HEIGHT or ball_y - ball_radius <= 0:
        ball_dy *= -1
        ball_radius *= 1.04  # Enlarge the ball by 2%
        ball_dy *= 1.04      # Increase speed by 2%
        

    # Update the ball position on the canvas
    canvas.coords(ball, ball_x - ball_radius, ball_y - ball_radius,
                  ball_x + ball_radius, ball_y + ball_radius)

    # Refresh the window
    root.update()

    # Pause for a short time to control the update speed
    time.sleep(UPDATE_INTERVAL / 1000)
