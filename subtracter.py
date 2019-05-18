#
# Very contrived class that subtracts stuff.
#

class Subtracter:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def difference(self):
        return self.a - self.b
