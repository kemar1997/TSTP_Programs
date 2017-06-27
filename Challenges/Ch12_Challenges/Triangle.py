# Create a Triangle class with a method called area that calculates and returns
# its area. Then create a Triangle object, call area on it, and print the result.

# a,b,c are the sides of the triangle
class Triangle():
    def __init__(self, a, b, c):
        self.s1 = a
        self.s2 = b
        self.s3 = c

    def area(self):
        # calculcate the semi-perimeter
        s = (self.s1 + self.s2 + self.s3) / 2

        # calculate the area
        return (s*(s-self.s1)*(s-self.s2)*(s-self.s3)) ** 0.5


triangle = Triangle(5, 6, 7)
print(triangle.area())
