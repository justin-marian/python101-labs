import random as rd
import math

def random_points(radius, center_x, center_y):
    """
    Generates a random point (x, y) inside a circle.
    
    Parameters:
        radius (float): Radius of the circle.
        center_x (float): X-coordinate of the circle center.
        center_y (float): Y-coordinate of the circle center.
    
    Returns:
        tuple: (x, y) coordinates inside the circle.
    """
    # Generate a random angle (0 to 2π) and radius (scaled within circle)
    theta = rd.uniform(0, 2 * math.pi)
    r = radius * math.sqrt(rd.uniform(0, 1))  # Uniform distribution in the circle
    
    # Convert polar to Cartesian coordinates
    x = center_x + r * math.cos(theta)
    y = center_y + r * math.sin(theta)
    
    return x, y
