import math
from functools import total_ordering

# ============================================
# Circle Class with Dunder Methods
# ============================================

@total_ordering
class Circle:
    def __init__(self, radius=None, diameter=None):
        """Create a circle with either radius or diameter."""
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Must provide either radius or diameter")
    
    # Property to get diameter from radius
    @property
    def diameter(self):
        return self.radius * 2
    
    # Property setter to allow setting diameter
    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2
    
    # Compute area
    def area(self):
        return math.pi * (self.radius ** 2)
    
    # String representation
    def __str__(self):
        return f"Circle(radius={self.radius:.2f}, diameter={self.diameter:.2f}, area={self.area():.2f})"
    
    # Official representation
    def __repr__(self):
        return f"Circle(radius={self.radius})"
    
    # Add two circles (radius adds up)
    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        return NotImplemented
    
    # Greater than comparison
    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        return NotImplemented
    
    # Equal comparison
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return False
    
    # Less than comparison (required for sorting, but @total_ordering handles others)
    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented


# ============================================
# Test the Circle Class
# ============================================
print("=" * 60)
print("Circle Class with Dunder Methods")
print("=" * 60)

# Create circles using radius and diameter
c1 = Circle(radius=5)
c2 = Circle(diameter=10)  # radius = 5
c3 = Circle(radius=3)
c4 = Circle(radius=8)

print(f"\nCircle 1 (radius=5): {c1}")
print(f"Circle 2 (diameter=10): {c2}")
print(f"Circle 3 (radius=3): {c3}")
print(f"Circle 4 (radius=8): {c4}")

# Test area
print(f"\nArea of c1: {c1.area():.2f}")

# Test diameter property
print(f"\nc1 diameter: {c1.diameter}")
c1.diameter = 20
print(f"After setting diameter to 20, radius is: {c1.radius}")

# Reset c1 for further tests
c1 = Circle(radius=5)

# Test addition
c_sum = c1 + c3
print(f"\nc1 + c3 = {c_sum}")

# Test comparisons
print(f"\nComparisons:")
print(f"c1 > c3: {c1 > c3}")   # True (5 > 3)
print(f"c1 == c2: {c1 == c2}") # True (both radius 5)
print(f"c1 < c4: {c1 < c4}")   # True (5 < 8)

# Test sorting
circles = [c4, c1, c3, c2]  # Unordered: 8, 5, 3, 5
print(f"\nUnsorted circles: {[c.radius for c in circles]}")
circles.sort()
print(f"Sorted circles: {[c.radius for c in circles]}")

# Test repr
print(f"\nrepr(c1): {repr(c1)}")


# ============================================
# Bonus: Turtle Visualization
# ============================================
print("\n" + "=" * 60)
print("Bonus: Drawing Circles with Turtle")
print("=" * 60)

try:
    import turtle
    
    def draw_circles(circles_list):
        """Draw circles using turtle graphics, sized and positioned by radius."""
        screen = turtle.Screen()
        screen.title("Circle Visualization")
        screen.setup(width=800, height=600)
        
        t = turtle.Turtle()
        t.speed(0)  # Fastest speed
        t.hideturtle()
        
        # Sort circles for organized display
        circles_list.sort()
        
        # Starting position
        x_start = -300
        y_position = 0
        spacing = 80
        
        for i, circle in enumerate(circles_list):
            t.penup()
            # Position turtle at bottom of circle
            x_pos = x_start + (i * spacing)
            t.goto(x_pos, y_position - circle.radius)
            t.pendown()
            
            # Draw circle
            t.circle(circle.radius)
            
            # Label with radius
            t.penup()
            t.goto(x_pos, y_position + circle.radius + 10)
            t.write(f"r={circle.radius}", align="center", font=("Arial", 10, "normal"))
        
        # Keep window open
        print("Close the turtle window to exit...")
        screen.mainloop()
    
    # Create sample circles and draw them
    sample_circles = [
        Circle(radius=30),
        Circle(radius=50),
        Circle(radius=20),
        Circle(radius=40),
        Circle(radius=35)
    ]
    
    print("Drawing circles with turtle...")
    print(f"Circles to draw: {[c.radius for c in sample_circles]}")
    draw_circles(sample_circles)

except ImportError:
    print("Turtle module not available or PythonTurtle not installed.")
    print("To install: pip install PythonTurtle")
    print("Or use built-in turtle (usually included with Python)")
    print("\nSimulating circle drawing with ASCII art:")
    
    def ascii_circle(radius):
        """Simple ASCII representation of a circle."""
        chars = int(radius / 2)
        print(f"  {' ' * chars}***")
        print(f" {' ' * (chars-1)}*     *")
        print(f"{' ' * (chars-2)}