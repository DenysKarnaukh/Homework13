class Counter:

    def __init__(self, current=1, min_value=0, max_value=10):
        self.min_value = min_value
        self.max_value = max_value
        self.current = current

    def set_current(self, start):
        if start < self.min_value or start > self.max_value:
            raise ValueError("Поточне значення поза межами")
        self.current = start

    def set_max(self, max_max):
        if max_max < self.min_value:
            raise ValueError("max < min")
        self.max_value = max_max

    def set_min(self, min_min):
        if min_min > self.max_value:
            raise ValueError("min > max")
        self.min_value = min_min

    def step_up(self):
        if self.current >= self.max_value:
            raise ValueError("Досягнуто максимуму")
        self.current += 1

    def step_down(self):
        if self.current <= self.min_value:
            raise ValueError("Досягнуто мінімуму")
        self.current -= 1

    def get_current(self):
        return self.current

