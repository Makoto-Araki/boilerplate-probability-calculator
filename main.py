# This entrypoint file to be used in development. Start by reading README.md
import prob_calculator
from unittest import main

'''
hat = prob_calculator.Hat(blue=5, red=4, green=2)
probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"red": 1, "green": 2},
    num_balls_drawn=4,
    num_experiments=3000
)
print("Probability:", probability)
'''

''' __init__
hat = prob_calculator.Hat(blue=2, green=1)
'''

''' draw
hat = prob_calculator.Hat(blue=2, green=2)
hat.draw(3)
'''

''' experiment
hat = prob_calculator.Hat(blue=4, pink=4)
probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"blue": 3, "pink": 1},
    num_balls_drawn=5,
    num_experiments=10)
print("Probability:", probability)
'''

''' Original Code
prob_calculator.random.seed(95)
hat = prob_calculator.Hat(blue=4, red=2, green=6)
probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"blue": 2, "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)
'''

# Run unit tests automatically
main(module='test_module', exit=False)
