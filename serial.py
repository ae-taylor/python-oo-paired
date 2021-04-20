class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    # instantiates new SerialGenerator with self as first param and a start number
    def __init__(self, start):
        self.start = start
        self.counter = start - 1

    # Generates next sequential number and returns that number
    def generate(self):
        self.counter = self.counter + 1
        return self.counter

    # Resets the counter back to initial start point
    def reset(self):
        self.counter = self.start -1


        