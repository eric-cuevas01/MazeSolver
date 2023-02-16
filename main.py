# Eric Cuevas, Andrew Molina
# February 18, 2023
# A program that allows the user to solve a maze that is read in from a file. The user will begin at a starting point of the maze and will be able to move up, down, left, or right to move through the maze. When the user reaches the finish, they have solved the maze.

import check_input


def read_maze(maze):
  """Reads in the contents of the maze file and returns the maze as a 2D list."""
  layout = open("maze.txt", "r")
  maze = []
  for line in layout:
    list = []
    for char in line:
      list += char
    maze.append(list)
  return maze


def find_start(maze):
  """Finds the starting position of the maze and returns it as a 1D list of [row, column]."""
  for i in range(len(maze)):
    for j in range(len(maze[i])):
      if maze[i][j] == 's':
        return [i, j]


def display_maze(maze, loc):
  """Displays the maze with an 'X' at the user's starting and current location after every input."""
  print("-Maze Solver-")
  for i in range(len(maze)):
    for j in range(len(maze[i])):
      if i == loc[0] and j == loc[1]:
        print('X', end=' ')
      else:
        print(maze[i][j], end=' ')
    print()


def main():
  """Takes the user's input and moves the X depending on the input. The X moves one unit up, down, left, or right. Only integers are accepted as an input. Players are not allowed to move in the direction of where an asterisk (*) is. The game ends once the player reaches the finish (f)."""
  maze = read_maze('maze.txt')
  loc = find_start(maze)
  finished = False

  while not finished:
    display_maze(maze, loc)
    direction = check_input.get_int_range(
      'Which direction would you like to move?\n1. Go North\n2. Go South\n3. Go West\n4. Go East\nEnter choice: ',
      1, 4)

    if direction == 1:  # Moving up
      next_loc = [loc[0] - 1, loc[1]]
    elif direction == 2:  # Moving down
      next_loc = [loc[0] + 1, loc[1]]
    elif direction == 3:  # Moving left
      next_loc = [loc[0], loc[1] - 1]
    elif direction == 4:  # Moving right
      next_loc = [loc[0], loc[1] + 1]
    else:
      print('Invalid direction. Your choice should be between 1 and 4.')
      continue

    if maze[next_loc[0]][next_loc[1]] == '*':
      print("There's a wall! You cannot move there.")
    elif maze[next_loc[0]][next_loc[1]] == 'f':
      print('Congratulations, you solved the maze!')
      finished = True
    else:
      loc = next_loc


if __name__ == '__main__':
  main()
