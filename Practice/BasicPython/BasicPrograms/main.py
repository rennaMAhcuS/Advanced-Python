# Presume that a ladder is put upright against a wall.
# Let variables length and angle store the length of
# the ladder and the angle that it forms with the ground
# as it leans against the wall.
# Write a Python program to compute the height reached by
# the ladder on the wall for the following values of length
# and angle:
import math

length = int(input("Enter the length of the ladder: "))
angle = int(input("Enter the angle (in degrees) made by the ladder with the ground: "))

print("The height reached by the ladder on the wall is", round((length * math.sin(math.radians(angle))), 3))
