# This entrypoint file to be used in development. Start by reading README.md
import prob_calculator
from unittest import main

''' __init__
hat = prob_calculator.Hat(blue=2, green=1)
'''

''' draw
hat = prob_calculator.Hat(blue=2, green=2)
hat.draw(3)
'''

''' experiment
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
#main(module='test_module', exit=False)
