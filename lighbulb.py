class lightbulb:
    def __init__(self,status):
        self.status = status
        
    def toggle(self):
        self.status = "OFF" if self.status == "ON" else "ON"
        print("Light is",self.status)
        
bulb = lightbulb("OFF")
bulb.toggle()
bulb.toggle()
bulb.toggle()
