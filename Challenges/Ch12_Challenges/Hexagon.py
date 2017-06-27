# Make a Hexgon class with a method called calculate_perimeter that calculates
# and returns its perimeter. Then create a Hexagon object, call calculate_peri
# meter on it, and print the result.

# P = 6a (a = length of on side)

class Hexagon():
    def __init__(self, a):
        self.s = a

    def calculate_perimeter(self):
        return 6 * self.s


hexagon = Hexagon(4.3)
print(hexagon.calculate_perimeter())
