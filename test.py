matrix = []
for row in range(2):
    a = []
    for column in range(2):
        a.append('a')
    matrix.append(a)

for row in range(2):
    for column in range(2):
        print(matrix[row][column], end=' ')
    print()

def create_none_matrix(rows, cols):
  
  matrix = []
  for i in range(rows):
    row = [None] * cols
    matrix.append(row)
  return matrix

# Example usage:
matrix = create_none_matrix(3, 4)
print(matrix)