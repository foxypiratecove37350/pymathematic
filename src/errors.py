class InDevError(NotImplementedError):
    def __init__(self, msg: str | None = None) -> None:
        if msg is None:
            super().__init__('Still in devloppement')
        else:
            super().__init__(msg)
        
class DivisionByZeroError(ZeroDivisionError):
    def __init__(self, msg: str | None = None) -> None:
        if msg is None:
            super().__init__('Division by 0, +∞ as x → 0+, -∞ as x → 0-')
        else:
            super().__init__(msg)

class PositiveIntegerError(ValueError):
    def __init__(self, msg: str | None = None) -> None:
        if msg is None:
            super().__init__('Positive integer expected')
        else:
            super().__init__(msg)

class NegativeIntegerError(ValueError):
    def __init__(self, msg: str | None = None) -> None:
        if msg is None:
            super().__init__('Negative integer expected')
        else:
            super().__init__(msg)