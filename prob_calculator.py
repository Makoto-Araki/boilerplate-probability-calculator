import copy
import random
# Consider using the modules imported above.

class Hat:
    
    def __init__(self, **args):
        self.contents = list()
        for key, val in args.items():
            for i in range(val):
                self.contents.append(key)
    
    def draw(self, quantity):
        return_list = list()
        if quantity > len(self.contents):
            for i in range(len(self.contents)):
                return_list.append(self.contents.pop(0))
        else:
            for i in range(quantity):
                idx = random.choice(range(len(self.contents)))
                return_list.append(self.contents[idx])
                self.contents.pop(idx)
        return return_list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    //