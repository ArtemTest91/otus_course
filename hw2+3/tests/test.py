from Square import Square
from Triangle import Triangle
from Circle import Circle
from Rectangle import Rectangle

rect = Rectangle(3, 5)
s = Square(10)
print(rect.add_area(other_figure=s))

squa = Square(5)
s = Triangle(5, 5, 7)
print(squa.add_area(other_figure=s))

circ = Circle(5)
s = Rectangle(3, 5)
print(circ.add_area(other_figure=s))

rect2 = Rectangle(5, 7)
s = Triangle(10, 14, 21)
print(rect2.add_area(other_figure=s))

print(7 + 0.5)