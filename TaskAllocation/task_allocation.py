import heapq  #for priority queue
from typing import List
import sys

class Task:
    def __init__(self, description: str, duration: int):
        self.description = description
        self.duration = duration

class Worker:
    def __init__(self, worker_id: int, workload: int):
        self.id = worker_id
        self.workload = workload

    def __lt__(self, other):
        #Used to compare (less-than <) Worker objects,
        return self.workload < other.workload

class TaskAllocation:
    def __init__(self):
        self.tasks = []
        self.worker_queue = []
        
    def main(self):
        num_workers = int(input("Enter the number of workers: "))

        #Initialize workers with ID and 0 workload
        for i in range(num_workers):
            heapq.heappush(self.worker_queue, Worker(i, 0))
        
        while True:
            print("\nMenu:")
            print("1. Add Task")
            print("2. Display Tasks")
            print("3. Print Workers Queue")
            print("4. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.add_task()
            elif choice == 2:
                self.display_tasks()
            elif choice == 3:
                self.print_workers_queue()
            elif choice == 4:
                print("Exiting program...")
                break
            else:
                print("Invalid choice! Please try again.")
  
    #Method to add a task and allocate it to a worker
    def add_task(self):
        description = input("Enter task description: ")
        duration = int(input("Enter task duration (in minutes): "))

        if len(self.worker_queue) == 0:
            print("No workers available! Task cannot be assigned.")
            return

        #Dequeue the worker with the shortest workload
        worker = heapq.heappop(self.worker_queue)

        #Assign the task to the worker and update workload
        self.tasks.append(Task(description, duration))
        print(f"Task added successfully and allocated to Worker {worker.id}!")

        #Update workload
        worker.workload += duration

        #Store updated worker back to queue
        heapq.heappush(self.worker_queue, worker)

    #Method to display all tasks
    def display_tasks(self):
        print("Task List:")
        for task in self.tasks:
            print(f"Task description: {task.description}, "
                  "Duration: {task.duration} minutes")

    #Method to print the workers queue
    def print_workers_queue(self):
        print("Workers Queue:")
        #heapq does not support direct iteration, we need to copy the heap to display
        temp_queue = list(self.worker_queue)
        heapq.heapify(temp_queue)
        while temp_queue:
            worker = heapq.heappop(temp_queue)
            print(f"Worker ID: {worker.id}, Workload: {worker.workload} minutes")


if __name__ == "__main__":
    TaskAllocation().main()
