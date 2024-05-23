class Point:
    def __init__(self, row=0, col=0):
        self.row = row
        self.col = col

class Stack:
    def __init__(self, capacity):
        #Initialize stack with a fixed capacity
        self.items = [None] * capacity  
        #Initialize top index
        self.top = -1  

    #Check if stack is empty
    def is_empty(self):
        return self.top == -1  
    
    #Push item onto stack
    def push(self, item):
        self.top += 1 
        self.items[self.top] = item

    #Return top item
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            exit(1) 
        item = self.items[self.top]  
        self.top -= 1
        return item 

class Maze:
    ROWS = 15
    COLS = 15

    def __init__(self):
        #Create a stack with a size equal to total cells
        self.stack = Stack(self.ROWS * self.COLS)  
        self.matrix = [
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0],
            [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0],
            [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
            [0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
            [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
        ]

    def can_move(self, row, col):
        #Check if we can move to this cell
        return (0 <= row < self.ROWS \
                and 0 <= col < self.COLS \
                    and self.matrix[row][col] == 0)

    def print_maze(self):
        #Print the maze
        for row in self.matrix:
            print(" ".join(str(cell) for cell in row))

    def solve(self, row, col):
        #Solve the maze using backtracking
        if row == self.ROWS - 1 and col == self.COLS - 1:
            #Destination reached
            self.stack.push(Point(row, col))
            return 1

        if self.can_move(row, col):
            self.stack.push(Point(row, col))
            self.matrix[row][col] = 2  #Mark as visited

            #Move right
            if self.solve(row, col + 1) == 1:
                return 1

            #Move down
            if self.solve(row + 1, col) == 1:
                return 1

            #Move left
            if self.solve(row, col - 1) == 1:
                return 1

            #Move up
            if self.solve(row - 1, col) == 1:
                return 1

            #Backtrack if no movement is possible
            self.stack.pop()
            return 0

        return 0

    def print_path(self):
        #Print the path from stack
        while not self.stack.is_empty():
            p = self.stack.pop()
            print(f"({p.row}, {p.col})", end=", ")


def main():
    maze = Maze()

    print("This is the maze:")
    maze.print_maze()

    if maze.solve(0, 0) == 1:
        print("\n\nThis is the path found:")
        maze.print_path()

        print("\n\nThis is the maze with all the points crossed:")
        maze.print_maze()
    else:
        print("No path found")


if __name__ == "__main__":
    main()
