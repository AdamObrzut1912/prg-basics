class C:
    def __init__(self, coordinates):
        self.coordinates = coordinates
    def m(self, n):
        self.true_false = False
        counter = 0
        for array in self.coordinates:
            if array[0] > 0 and array[1] > 0:
                counter += 1
        if counter >= n:
            self.true_false = True
        else:
            self.true_false = False

    def __str__(self):
        return str(self.true_false)