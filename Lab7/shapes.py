class Rectangle:
    def __init__(self, a=1, b=1):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            if a >= 0 and b >= 0:
                self.b = b
                self.a = a
            else:
                raise ValueError("a and b cannot be negative numbers")
        else:
            raise TypeError("a and b must be of numeric type")

    def get_area(self):
        return self.a * self.b

    def get_perimeter(self):
        return self.a * 2 + self.b * 2
