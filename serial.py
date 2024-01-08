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
        self.next = start
        self.counter = 0

    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.next + 1}>"
        
    def generate(self):
        """Return the next sequential number"""
        if self.counter == 0:
            self.counter += 1
            return self.start
        if self.counter == 1:
            self.counter += 1
            self.next += 1
            return self.next
        self.next += 1
        return self.next

    def reset(self):
        """Reset the number back to the original start number"""
        self.next = self.start
        self.counter = 0
