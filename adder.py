#
# Very contrived class that adds stuff together.
#

class Adder:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b
