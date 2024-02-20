class SimplePolicy:
    def __init__(self) -> None:
        pass

    def choose_action(self, state: int) -> int:
        if state < 37:
            return 2  # Increase temperature
        elif state > 39:
            return 0  # Decrease temperature
        else:
            return 1  # Maintain temperature
