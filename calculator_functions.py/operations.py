from calculator import Calculator


class Operations(Calculator):
    """Extended calculator operations with error handling and validation."""

    def add(self, a, b):
        self._validate_numbers(a, b)
        return a + b
    
    def subtract(self, a, b):
        self._validate_numbers(a, b)
        return a - b
    

    