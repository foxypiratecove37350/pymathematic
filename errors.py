class InDevError(NotImplementedError):
    def __init__(self) -> None:
        super().__init__('Still in devloppement')
        
class DivisionByZeroError(ZeroDivisionError):
    def __init__(self) -> None:
        super().__init__('Division by 0, +∞ as x → 0+, -∞ as x → 0-')