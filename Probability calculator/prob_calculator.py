import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = list()
        for (colour,nball) in kwargs.items():
            for i in range(nball):   
                self.contents.append(colour)
    
    def draw(self, nb_drawn):
        if nb_drawn <= len(self.contents):
            extracted = list()
            extracted = random.choices(self.contents, k=nb_drawn)
            for item in extracted:
                self.contents.pop(extracted.index(item))
            return extracted
        else:
            return self.contents
        
            
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    c_hat = copy.deepcopy(hat.contents)
    for i in range(num_experiments):
        prob = copy.deepcopy(expected_balls)
        extr = hat.draw(num_balls_drawn)
        hat.contents = copy.deepcopy(c_hat)
        for ball in extr:
            if ball in prob:
                prob[ball] -=1
        if all(ball <=0 for ball in prob.values()):
            m += 1
    return m / num_experiments






