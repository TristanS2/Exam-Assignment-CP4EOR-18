class Maze:
    def __init__(self):
        # Open the file:
        fh = open("maze1.txt", "r")
        content = fh.readlines()
        # maze_array is a two-dimensional array with the entire maze (integers):
        maze_array = []
        # Fill maze_array with numbers from file:
        for i in range(len(content)):
            line = str(content[i]).strip()
            linelist = []
            for element in line:
                linelist.append(int(element))
            maze_array.append(linelist)
        self.maze_array = maze_array
        # Find finish of maze, i.e. zero on the side:
        # Coordinates of this finish line. Start at (0, 0):
        row = 0
        column = 0
        width = len(maze_array[1])-1
        height = len(maze_array)-1
        success = 0
        # Check the upper row:
        for i in range(width):
            if maze_array[row][column] == 0:
                success = 1
                break
            else:
                column += 1
        # Check the lower row:
        if success == 0:
            row = height
            column = 0
            for j in range(width):
                if maze_array[row][column] == 0:
                    success = 1
                    break
                else:
                    column += 1
        # Check left side:
        if success == 0:
            row = 0
            column = 0
            for k in range(height):
                if maze_array[row][column] == 0:
                    success = 1
                    break
                else:
                    row += 1
        #Check right side:
        if success == 0:
            row = 0
            column = width
            for l in range(height):
                if maze_array[row][column] == 0:
                    success = 1
                    break
                else:
                    row += 1
        # Save finish coordinate as attribute:
        self.finish = [row, column]


