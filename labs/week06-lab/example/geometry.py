# Example 3: Mathematical function
def calculate_triangle_area(height, base):
    """Calculates and displays rectangle area"""
    area = 0.5 * height * base
    print(f"Triangle with height {height} and base {base}")
    print(f"Area = 0.5 * {height} x {base} = {area}")
    print()

    print("Calculating triangle areas: ")
    calculate_traiangle_area(5,3)
    calculate_triangle_area(10,7)

def calculate_circle_area(radius):
    pi = 3.14159
    area = pi * (radius ** 2)
    print(f"Circle with radius{radius}")
    print(f"Area ={pi} *{radius}**2 = {area}")
    print()

    print("Calculating circle areas: ")
    calculate_circle_area(5)
    calculate_circle_area(10)

    
    