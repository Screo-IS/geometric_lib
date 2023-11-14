import square
import rectangle
import circle
import triangle


def test_square_area():
    input_ = int(input("Enter side length "))
    res = square.area(input_)
    print(res)


def test_square_perimeter():
    input_ = int(input("Enter side length "))
    res = square.perimeter(input_)
    print(res)


def test_circle_area():
    input_ = int(input("Enter radius length "))
    res = circle.area(input_)
    print(res)


def test_circle_perimeter():
    input_ = int(input("Enter radius length "))
    res = circle.perimeter(input_)
    print(res)


def test_rectangle_area():
    input_ = list(map(int, (input("Enter side length ").split(" "))))
    res = rectangle.area(input_[0], input_[1])
    print(res)


def test_rectangle_perimeter():
    input_ = list(map(int, (input("Enter side length ").split(" "))))
    res = rectangle.perimeter(input_[0], input_[1])
    print(res)


def test_triangle_area():
    input_ = list(map(int, (input("Enter the side length and altitude length of the triangle ").split(" "))))
    res = triangle.area(input_[0], input_[1])
    print(res)


def test_triangle_perimeter():
    input_ = list(map(int, (input("Enter the sides length ").split(" "))))
    res = triangle.perimeter(input_[0], input_[1], input_[2])
    print(res)

count = 0
while True:
    if count != 0:
        print('\n')
    print("Enter the name of the figure:\n"
          "1. Square\n"
          "2. Rectangle\n"
          "3. Circle\n"
          "4. Triangle\n"
          "5. Exit")
    figure = input()
    count += 1

    if figure == 'Square':
        print("Enter:\n"
              "1. Calculate area\n"
              "2. Calculate perimeter")
        action = int(input())
        if action == 1:
            test_square_area()
        else:
            test_square_perimeter()
    if figure == "Rectangle":
        print("Enter:\n"
              "1. Calculate area\n"
              "2. Calculate perimeter")
        action = int(input())
        if action == 1:
            test_rectangle_area()
        else:
            test_rectangle_perimeter()
    if figure == "Circle":
        print("Enter:\n"
              "1. Calculate area\n"
              "2. Calculate perimeter")
        action = int(input())
        if action == 1:
            test_circle_area()
        else:
            test_circle_perimeter()
    if figure == "Triangle":
        print("Enter:\n"
              "1. Calculate area\n"
              "2. Calculate perimeter")
        action = int(input())
        if action == 1:
            test_triangle_area()
        else:
            test_triangle_perimeter()
    if figure == "Exit":
        break