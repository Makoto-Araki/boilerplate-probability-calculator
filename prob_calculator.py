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
    count = 0
    for i in range(num_experiments):
        experiment_hat = copy.copy(hat)
        extracted_list = experiment_hat.draw(num_balls_drawn)
        expected_list = list()
        for key, val in expected_balls.items():
            for i in range(val):
                expected_list.append(key)
        print(extracted_list)
        print(expected_list)  # ['blue', 'blue', 'red']
        flg = True
        for item in expected_list:
            if item in extracted_list:
                idx = extracted_list.index(item)
                extracted_list.pop(idx)
            else:
                flg = False
                break
        if flg:
            print('OK')
            count += 1
        else:
            print('NG')
    return count / num_experiments