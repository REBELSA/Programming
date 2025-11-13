class clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
    def display(self):
        print(f"The time is {self.hour}:{self.minute:02}")

c = clock(3,30)
c.display()