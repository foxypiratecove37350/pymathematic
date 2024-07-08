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

class IntegerError(ValueError):
    def __init__(self, msg: str | None = None) -> None:
        if msg is None:
            super().__init__('Positive or negative integer expected')
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
            
class InvalidLiteralError(ValueError):
    def __init__(self, infos: tuple[type, str], msg: str | None = None) -> None:
        if msg is None:
            self.cls = infos[0]
            self.literal = infos[1]
            super().__init__(f"Invalid literal for {self.cls.__class__.__name__}(): '{self.literal}'")
        else:
            super().__init__(msg)