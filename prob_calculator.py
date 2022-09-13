import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for k, v in kwargs.items():
      self.contents += [k] * int(v)

  def draw(self, number):
    n = len(self.contents)
    if number >= n:
      return self.contents
      
    result = []
    for i in range(0, number):
      chosen_ball = random.randint(0, n - 1)
      result.append(self.contents.pop(chosen_ball))
      n -= 1

    return result
    
    


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for _ in range(0, num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls = hat_copy.draw(num_balls_drawn)
        balls_dict = dict()
        for ball in balls:
            balls_dict[ball] = balls_dict.get(ball, 0) + 1

        successful = True
        for ball, v in expected_balls.items():
            if balls_dict.get(ball, 0) < v:
                successful = False
                break

        if successful:
            count += 1

    return count / num_experiments

        

