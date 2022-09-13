import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for k, v in kwargs.items():
            self.contents += [k] * int(v)

    def draw(self, number):
        if number >= len(self.contents):
            return self.contents
      
        result = []
        for i in range(0, number):
            chosen_ball = random.randint(0, n - 1)
            result.append(self.contents.pop(chosen_ball))
            n -= 1

        return result


# def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
