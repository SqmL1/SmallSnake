  
#what parts does a snake need?
#a body:
#   The body needs to be able to grow, how?
#       when the head touches an apple increment body size
#   How do we represent the body?
#       Print to the console O's for the body, adding @ each consumption event
#



class game:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def board_matrix(self):
        matrix = []
        matrix += [['+'] + ['-'] * (self.width) + ['+']]
        for i in range(self.height):
            row = ['|'] + [" "] * self.width + ['|']
            matrix.append(row)
        matrix += [['+'] + ['-'] * (self.width) + ['+']]
        return matrix

    
    def render(self):
        matrix = self.board_matrix()
        for row in matrix:
            for cell in row:
                print(cell, end=' ')
            print()                

class snake:
    def __init__(self, init_body, init_direction):
        self.body = init_body
        self.direction = init_direction
        pass

    def take_step(self, position):
        self.body = self.body[1:] + [position]
        pass

    def set_direction(self, direction):
        self.direction = direction

    def head(self):
        return self.body[-1]



game(10,20).render()
