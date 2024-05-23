class Stack:
    def __init__(self):
        self.items = []  #Initialize an empty list to store stack items

    def push(self, c):
        self.items.append(c)  #Append the character to the stack

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            exit(1)  #Exit if the stack is empty
        return self.items.pop()  #Pop and return the top item

    def is_empty(self):
        return len(self.items) == 0  #Return True if the stack is empty


class SyntaxChecker:
    @staticmethod
    def check_balanced(filename):
        try:
            with open(filename, 'r') as file:
                stack = Stack()

                while True:
                    #Read one character at a time
                    c = file.read(1)  
                    if not c:  # End of file
                        break

                    if c in '([{':  
                        #If the character is an opening bracket
                        stack.push(c)
                    elif c in ')]}':  
                        #If the character is a closing bracket
                        if stack.is_empty():
                            return 0

                        opening_char = stack.pop()

                        #Check if the closing bracket matches the opening bracket
                        if (c == ')' and opening_char != '(') or \
                           (c == ']' and opening_char != '[') or \
                           (c == '}' and opening_char != '{'):
                            return 0

                #Return 1 if balanced, 0 otherwise
                return 1 if stack.is_empty() else 0  
        except IOError as e:
            print(e)
            return 0

    @staticmethod
    def main():
        try:
            filename = input("Path to the source file: ")

            if SyntaxChecker.check_balanced(filename) == 1:
                print("The input file is balanced.")
            else:
                print("The input file is not balanced.")
        except IOError as e:
            print(e)


if __name__ == "__main__":
    SyntaxChecker.main()
