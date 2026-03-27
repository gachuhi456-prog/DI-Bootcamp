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
            self._radius = float(radius)
        elif diameter is not None:
            self._radius = float(diameter) / 2
        else:
            raise ValueError("Must provide either radius or diameter")
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        self._radius = float(value)
    
    @property
    def diameter(self):
        return self._radius * 2
    
    @diameter.setter
    def diameter(self, value):
        self._radius = float(value) / 2
    
    def area(self):
        """Compute the circle's area."""
        return math.pi * (self._radius ** 2)
    
    def __str__(self):
        return f"Circle(radius={self._radius:.2f}, diameter={self.diameter:.2f}, area={self.area():.2f})"
    
    def __repr__(self):
        return f"Circle(radius={self._radius})"
    
    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self._radius + other._radius)
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Circle):
            return self._radius > other._radius
        return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self._radius == other._radius
        return False
    
    def __lt__(self, other):
        if isinstance(other, Circle):
            return self._radius < other._radius
        return NotImplemented
    
    def __hash__(self):
        return hash(self._radius)


# ============================================
# Test the Circle Class
# ============================================
def test_circle():
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
    print(f"\nUnsorted circles radii: {[c.radius for c in circles]}")
    circles.sort()
    print(f"Sorted circles radii: {[c.radius for c in circles]}")

    # Test repr
    print(f"\nrepr(c1): {repr(c1)}")
    
    return circles


# ============================================
# Bonus: Turtle Visualization (Fixed for VS Code)
# ============================================
def draw_circles_turtle(circles_list):
    """Draw circles using turtle graphics."""
    try:
        import turtle
        
        # Create screen
        screen = turtle.Screen()
        screen.title("Circle Visualization")
        screen.setup(width=800, height=600)
        
        t = turtle.Turtle()
        t.speed(0)
        t.hideturtle()
        
        # Sort circles
        sorted_circles = sorted(circles_list)
        
        # Calculate layout
        x_start = -300
        y_position = 0
        max_radius = max(c.radius for c in sorted_circles)
        spacing = max_radius * 2 + 20
        
        colors = ['red', 'blue', 'green', 'orange', 'purple', 'yellow']
        
        for i, circle in enumerate(sorted_circles):
            t.penup()
            x_pos = x_start + (i * spacing)
            t.goto(x_pos, y_position - circle.radius)
            t.pendown()
            
            # Set color
            t.pencolor(colors[i % len(colors)])
            t.fillcolor(colors[i % len(colors)])
            
            # Draw filled circle
            t.begin_fill()
            t.circle(circle.radius)
            t.end_fill()
            
            # Label
            t.penup()
            t.goto(x_pos, y_position + circle.radius + 15)
            t.pencolor('black')
            t.write(f"r={circle.radius:.0f}", align="center", font=("Arial", 10, "bold"))
        
        print("\nTurtle window opened. Click the window X button to close.")
        screen.exitonclick()
        
    except Exception as e:
        print(f"\nTurtle error: {e}")
        print("Running ASCII fallback instead.")
        draw_circles_ascii(circles_list)


def draw_circles_ascii(circles_list):
    """ASCII art fallback for circle visualization."""
    sorted_circles = sorted(circles_list)
    
    print("\n" + "=" * 60)
    print("ASCII Circle Visualization")
    print("=" * 60)
    
    for c in sorted_circles:
        r = int(c.radius)
        print(f"\nCircle: radius={r}, area={c.area():.1f}")
        
        # Simple ASCII representation
        diameter = r // 2
        if diameter < 2:
            diameter = 2
        
        for y in range(-diameter, diameter + 1):
            line = ""
            for x in range(-diameter * 2, diameter * 2 + 1):
                # Check if point is inside circle
                dist = ((x/2)**2 + y**2) ** 0.5
                if abs(dist - diameter) < 1.2:
                    line += "*"
                else:
                    line += " "
            print(line)
        
        print(f"{' ' * (diameter * 2)}r={r}")


# ============================================
# Main Execution
# ============================================
if __name__ == "__main__":
    # Run basic tests
    test_circles = test_circle()
    
    # Ask user about visualization
    print("\n" + "=" * 60)
    print("Bonus: Circle Visualization")
    print("=" * 60)
    
    choice = input("\nShow visualization? (1=Turtle, 2=ASCII, 3=Skip): ").strip()
    
    if choice == "1":
        # Create sample circles for visualization
        viz_circles = [
            Circle(radius=30),
            Circle(radius=50),
            Circle(radius=20),
            Circle(radius=40),
            Circle(radius=35)
        ]
        draw_circles_turtle(viz_circles)
    elif choice == "2":
        viz_circles = [
            Circle(radius=30),
            Circle(radius=50),
            Circle(radius=20),
            Circle(radius=40),
            Circle(radius=35)
        ]
        draw_circles_ascii(viz_circles)
    else:
        print("Skipping visualization.")
    
    print("\n" + "=" * 60)
    print("Circle class completed!")
    print("=" * 60)