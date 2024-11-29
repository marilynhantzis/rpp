def calculate_discriminant(a, b, c):
    return b**2 - 4*a*c

class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def discriminant(self):
        return calculate_discriminant(self.a, self.b, self.c)
