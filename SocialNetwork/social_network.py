class FriendNode:
    def __init__(self, name):
        self.name = name
        self.next = None

class User:
    def __init__(self, name):
        self.name = name
        self.friends = None

class MyQueue:
    class QueueNode:
        def __init__(self, user_index):
            self.user_index = user_index
            self.next = None

    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, user_index):
        new_node = self.QueueNode(user_index)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return -1

        user_index = self.front.user_index
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return user_index

class Graph:
    MAX_USERS = 100

    def __init__(self):
        self.users = [None] * self.MAX_USERS
        self.num_users = 0

    def add_user(self, name):
        if self.num_users >= self.MAX_USERS:
            print("Max user limit reached!")
            return

        self.users[self.num_users] = User(name)
        self.num_users += 1

    def add_connection(self, src, dest):
        if src < 0 or src >= self.num_users \
            or dest < 0 or dest >= self.num_users:
            print("Invalid user index!")
            return

        #Add bidirectional connection
        new_friend_src = FriendNode(self.users[dest].name)
        new_friend_src.next = self.users[src].friends
        self.users[src].friends = new_friend_src

        new_friend_dest = FriendNode(self.users[src].name)
        new_friend_dest.next = self.users[dest].friends
        self.users[dest].friends = new_friend_dest

    def recommend_friends(self, user_index):
        print(f"Recommended friends for {self.users[user_index].name}:")

        #Store the indexes of the user’s friends
        queue = MyQueue()
        #Store the persons that we have already visited
        visited = [False] * self.MAX_USERS

        visited[user_index] = True
        #Enqueue the starting user
        queue.enqueue(user_index)

        while not queue.is_empty():
            current_user_index = queue.dequeue()
            current = self.users[current_user_index].friends

            #Traverse the user's friends
            while current is not None:
                friend_index = -1
                #Find the friend's index
                for i in range(self.num_users):
                    if current.name == self.users[i].name:
                        friend_index = i
                        break

                #Check if the friend is already visited
                if friend_index != -1 and not visited[friend_index]:
                    print(f"- {current.name}")
                    #Add friend to visited list
                    visited[friend_index] = True
                    #Enqueue friend
                    queue.enqueue(friend_index)

                #Move to the next friend
                current = current.next

if __name__ == "__main__":
    graph = Graph()
    graph.add_user("User A")
    graph.add_user("User B")
    graph.add_user("User C")
    graph.add_user("User D")
    graph.add_user("User E")
    graph.add_user("User F")
    graph.add_user("User G")
    graph.add_user("User H")

    graph.add_connection(0, 1)
    graph.add_connection(1, 2)
    graph.add_connection(2, 3)
    graph.add_connection(4, 5)
    graph.add_connection(5, 7)
    graph.add_connection(3, 6)

    graph.recommend_friends(0)
    graph.recommend_friends(1)
    graph.recommend_friends(7)
