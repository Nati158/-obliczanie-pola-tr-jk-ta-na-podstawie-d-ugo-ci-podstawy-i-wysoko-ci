def calculate_triangle_area(base, height):
    return 0.5 * base * height

if __name__ == "__main__":
    base = float(input("Enter the length of the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = calculate_triangle_area(base, height)
    print("The area of the triangle is:", area)
