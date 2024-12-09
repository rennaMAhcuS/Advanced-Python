import tkinter as tk
import random


def generate_random_path(width, height):
    # Initialize the starting position
    x, y = 0, 0  # Bottom-left corner
    path = []

    while x < width - 1 or y < height - 1:
        if x == width - 1:
            path.append('U')
            y += 1
        elif y == height - 1:
            path.append('R')
            x += 1
        else:
            move = random.choice(['R', 'U'])
            if move == 'R':
                x += 1
            else:
                y += 1
            path.append(move)

    return ''.join(path)


def draw_path(canvas, path, block_size=50):
    # Starting position on the canvas
    x, y = 0, 0
    for move in path:
        if move == 'R':
            canvas.create_line(x, y, x + block_size, y, width=2, fill="red")
            x += block_size
        elif move == 'U':
            canvas.create_line(x, y, x, y - block_size, width=2, fill="red")
            y -= block_size


# Example usage
width = 50  # Width of the rectangle
height = 30  # Height of the rectangle
path = generate_random_path(width, height)
print(f"Generated path: {path}")

# Set up the tkinter window
root = tk.Tk()
root.title("Path Drawing")

# Calculate canvas size
canvas_width = width * 50
canvas_height = height * 50

# Create a canvas and draw the path
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()
draw_path(canvas, path)

# Start the tkinter loop
root.mainloop()
