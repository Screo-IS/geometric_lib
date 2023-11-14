import unittest
import circle
import rectangle
import triangle
import square

class UnitTest(unittest.TestCase):

    def test_rectangle_area(self):
        self.assertEqual(rectangle.area(5,5),25)
        self.assertEqual(rectangle.area('\n', 1), "length of side/sides not specified")
        self.assertEqual(rectangle.area(-1,1),'incorrect input, the input must contain numbers greater than 0')
        self.assertEqual(rectangle.area(2,'b'),'incorrect input, input cannot contain letters')
        self.assertEqual(rectangle.area(3,False),'incorrect input, input cannot be a boolean value')


    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle.perimeter(2,2), 8)
        self.assertEqual(rectangle.perimeter('\n', 2), "length of side/sides not specified")
        self.assertEqual(rectangle.perimeter('a',0), 'incorrect input, input cannot contain letters')
        self.assertEqual(rectangle.perimeter(-10,0), 'incorrect input, the input must contain numbers greater than 0')
        self.assertEqual(rectangle.perimeter(True,0), 'incorrect input, input cannot be a boolean value')

    def test_circle_perimeter(self):
        self.assertEqual(circle.perimeter(1), 6.283185307179586)
        self.assertEqual(circle.perimeter('\n'), "length of side/sides not specified")
        self.assertEqual(circle.perimeter(-1), 'incorrect input, the input must contain numbers greater than 0')
        self.assertEqual(circle.perimeter('y'), 'incorrect input, input cannot contain letters')
        self.assertEqual(circle.perimeter(False), 'incorrect input, input cannot be a boolean value')


    def test_circle_area(self):
        self.assertEqual(circle.area(1),3.141592653589793)
        self.assertEqual(square.area('\n'), "length of side/sides not specified")
        self.assertEqual(circle.area(0),'incorrect input, the input must contain numbers greater than 0')
        self.assertEqual(circle.area('e'),'incorrect input, input cannot contain letters')
        self.assertEqual(circle.area(True),'incorrect input, input cannot be a boolean value')


    def test_square_area(self):
        self.assertEqual(square.area(10), 100)
        self.assertEqual(square.area('\n'), "length of side/sides not specified")
        self.assertEqual(square.area(-5), 'incorrect input, the input must contain numbers greater than 0')
        self.assertEqual(square.area('d'),'incorrect input, input cannot contain letters')
        self.assertEqual(square.area(False),'incorrect input, input cannot be a boolean value')


    def test_square_perimetr(self):
        self.assertEqual(square.perimeter(5),20)
        self.assertEqual(square.perimeter('\n'), "length of side/sides not specified")
        self.assertEqual(square.perimeter(-2), 'incorrect input, the input must contain numbers greater than 0')
        self.assertEqual(square.perimeter('l'), 'incorrect input, input cannot contain letters')
        self.assertEqual(square.perimeter(True), 'incorrect input, input cannot be a boolean value')

    def test_triangle_perimeter(self):
        self.assertEqual(triangle.perimeter(2, 3, 4), 9)
        self.assertEqual(triangle.perimeter(5, 2, '\n'), "length of side/sides not specified")
        self.assertEqual(triangle.perimeter(3, 3, 0), 'incorrect input, the input must contain numbers greater than 0')
        self.assertEqual(triangle.perimeter(2, 'u', 3), 'incorrect input, input cannot contain letters')
        self.assertEqual(triangle.perimeter(True, 2, False), 'incorrect input, input cannot be a boolean value')
        self.assertEqual(triangle.perimeter(1, 2, 3), 'incorrect input, the basic property of a triangle must be satisfied')


    def test_triangle_area(self):
        self.assertEqual(triangle.area(3, 2), 3.0)
        self.assertEqual(triangle.area(1,'\n'), "length of side/sides not specified")
        self.assertEqual(triangle.area(3, 0), 'incorrect input, the input must contain numbers greater than 0')
        self.assertEqual(triangle.area('t', 'u'), 'incorrect input, input cannot contain letters')
        self.assertEqual(triangle.area(False, 7), 'incorrect input, input cannot be a boolean value')


if __name__ == '__main__':
    unittest.main()
