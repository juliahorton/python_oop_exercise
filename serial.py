"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    Attributes
    ------------------

    start (int): number to begin counting up from

    Doctests
    ------------------
    
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

    def __init__(self, start):
        """Create class instance with the given start number"""
        self.start = start
        self.increment = -1
        
    def generate(self):
        """Return the next sequential number"""
        self.increment += 1
        return self.start + self.increment

    def reset(self):
        """Reset the number back to the original start number"""
        self.increment = -1
