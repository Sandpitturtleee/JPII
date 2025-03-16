import json
import os


class Matrix1:
    model_count = 0

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __add__(self, m):
        return Matrix1(self.a + m.a, self.b + m.b, self.c + m.c, self.d + m.d)

    def __mul__(self, m):
        a = self.a * m.a + self.b * m.c
        b = self.a * m.b + self.b * m.d
        c = self.c * m.a + self.d * m.c
        d = self.c * m.b + self.d * m.d
        return Matrix1(a, b, c, d)

    def __str__(self):
        return f"[{self.a} {self.b}]\n[{self.c} {self.d}]"

    def __repr__(self):
        return f"Matrix({self.a}, {self.b}, {self.c}, {self.d})"


