import socket

class LRUCache:
    CACHE_SIZE = 3

    class Node:
        def __init__(self, url, content):
            self.url = url
            self.content = content
            self.prev = None
            self.next = None

    def __init__(self):
        #Initialize the cache
        self.head = None
        self.tail = None
        self.size = 0

    def get_content(self, url):
        #Get content associated with a URL from the cache
        current = self.head
        while current:
            if current.url == url:
                #Move the accessed node to the head
                self.move_to_head(current)
                print("Got content from cache:", current.content)
                return current.content
            current = current.next
        return ""

    def put_content(self, url, content):
        #Put a URL-content pair into the cache
        if self.size == self.CACHE_SIZE:
            #If cache is full, remove the least recently used node
            self.delete_node(self.tail)
            self.size -= 1
        new_node = self.create_node(url, content)
        self.insert_at_head(new_node)
        self.size += 1

    def create_node(self, url, content):
        #Create a new node
        print("New node created:", content)
        return self.Node(url, content)

    def insert_at_head(self, node):
        #Insert a new node at the head of the cache
        node.next = self.head
        node.prev = None
        if self.head:
            self.head.prev = node
        self.head = node
        if not self.tail:
            self.tail = node
        print("Node inserted at head:", node.content)

    def move_to_head(self, node):
        #Move a node to the head of the cache
        if node == self.head:
            return
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.prev = None
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node
        if not self.tail:
            self.tail = node
        print("Node moved to head:", node.content)

    def delete_node(self, node):
        #Delete a node from the cache
        if not node:
            return
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        print("Node deleted:", node.content)

class HttpServer:
    PORT = 8080
    MAX_REQUEST_SIZE = 1024

    def __init__(self):
        self.cache = LRUCache()

    def start(self):
        #Start the HTTP server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind(('localhost', self.PORT))
            server.listen()
            print("Server started on port", self.PORT)
            while True:
                client, _ = server.accept()
                self.handle_request(client)
                client.close()

    def handle_request(self, client):
        #Handle incoming HTTP requests
        with client:
            request = client.recv(self.MAX_REQUEST_SIZE).decode('utf-8')
            print("Received request:", request)

            parts = request.split()
            if len(parts) < 2 or parts[0] != "GET":
                print("Invalid request format.")
                return

            url = parts[1]
            content = self.cache.get_content(url)

            if not content:
                try:
                    with open(url[1:], 'r', encoding='utf-8') as file:
                        content = file.read()
                        print("Got content from file:", content)
                        self.cache.put_content(url, content)
                except FileNotFoundError:
                    print("File not found:", url[1:])
                    content = "HTTP/1.1 404 Not Found\r\n\r\n"
                except IOError:
                    print("File not found:", url[1:])
                    content = "HTTP/1.1 404 Not Found\r\n\r\n"
            else:
                print("Serving content from cache.")

            content_type = "text/plain"
            if url.endswith((".html", ".htm")):
                content_type = "text/html"

            response = f"HTTP/1.1 200 OK\r\n"
            "Content-Type: {content_type}\r\n\r\n{content}"
            
            client.sendall(response.encode('utf-8'))

def main():
    #Start the HTTP server
    server = HttpServer()
    server.start()

if __name__ == "__main__":
    main()
