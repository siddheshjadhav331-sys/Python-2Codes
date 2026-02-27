# Base class
class Instrument:
    def play(self):
        print("Instrument is playing")

# Subclass Guitar
class Guitar(Instrument):
    def play(self):
        print("Strumming the guitar")

# Subclass Piano
class Piano(Instrument):
    def play(self):
        print("Playing the piano keys")

# Demonstrating polymorphism
instruments = [ Guitar() ,Piano()]

for i in instruments:
    i.play()
