from random import choice

DIRECCTION = [1, -1]
DISTANCE = [0, 1, 2, 3, 4] 


class RandomWalk:
    """A class to generate random walks"""

    def __init__(self, num_points = 5000) -> None:
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]
        self.z_values = [0]

    def get_step(self):
         direction = choice(DIRECCTION) #choice elige aleatoriamente un valor en la lista proporcionada
         distance = choice(DISTANCE)
         return distance*direction

    def next_step(self):

        while True:
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step != 0 and y_step !=0:
                return (x_step, y_step)


    def fill_walk(self):
        """Calculate all the points in the walk"""
        for i in range(self.num_points - 1):
            x_step, y_step = self.next_step()       
     


            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            z = self.z_values[-1] + 1

            self.x_values.append(x)
            self.y_values.append(y)
            self.z_values.append(z)


    