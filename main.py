  
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
        for i in range(self.height):
            row = [None] * self.width
            matrix.append(row)
        return matrix

    
    def render(self):
        matrix = self.board_matrix()
        for row in matrix:
            for cell in row:
                print(cell, end=' ')
            print()                



game(10,10).render()
