from task import Task

class TodoList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_task(self, description, priority):
        task = Task(description, priority)
        if self.head is None:
            #List is empty
            self.head = task
        else:
            temp = self.head
            #Find the last node
            while temp.next is not None:
                temp = temp.next
            #Insert the new task after the last node
            temp.next = task
        self.size += 1

    def remove_task(self, index):
        if self.head is None:
            print("List is empty.")
            return

        if index == 0:
            #If we remove the first item in the list
            temp = self.head
            self.head = self.head.next
            temp = None
            self.size -= 1
            return

        previous = None
        current = self.head
        i = 0
        #Go to the selected index
        while current is not None and i < index:
            previous = current
            current = current.next
            i += 1

        if current is None:
            print("Index out of bounds.")
            return

        previous.next = current.next
        current = None
        self.size -= 1

    def display_tasks(self):
        temp = self.head
        i = 1
        while temp is not None:
            print(f"{i}) Description: {temp.description}, Priority: {temp.priority}")
            temp = temp.next
            i += 1

    def sort_tasks(self):
        if self.head is None:
            return

        swapped = True
        while swapped:
            swapped = False
            ptr1 = self.head

            while ptr1.next is not None:
                if ptr1.priority > ptr1.next.priority:
                    #Swap data of adjacent nodes
                    ptr1.priority, ptr1.next.priority = \
                        ptr1.next.priority, ptr1.priority
                    ptr1.description, ptr1.next.description = \
                        ptr1.next.description, ptr1.description
                    swapped = True
                ptr1 = ptr1.next
