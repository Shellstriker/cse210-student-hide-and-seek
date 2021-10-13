import random

# TODO: Define the Hider class here
class hider:
    def __init__(self):
        self.location = random.randint(1,100)
        self.distance = [0]
    
    def get_hint(self):
        hint = "Maybe I'll take a nap."
        if self.distance[-1] == 0:
            hint = "You found me!"
        elif self.distance[-1] > self.distance[-2]:
            hint = "Getting colder!"
        elif self.distance[-1] < self.distance[-2]:
            hint = "Getting warmer!"
        return hint
    
    def watch(self, location):
        distance = abs(self.location - location)
        self.distance.append(distance)
