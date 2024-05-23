import socket
import threading
import time

#Client class representing each client connected to the server
class Client:
    def __init__(self, socket, client_id):
        self.socket = socket
        self.writer = socket.makefile('w')
        self.reader = socket.makefile('r')
        self.id = client_id

#Constants
PORT = 8080  #Port number for the server
MAX_CLIENTS = 5  #Maximum number of clients

#Server and clients
server = None
clients = [None] * MAX_CLIENTS  #List to hold clients

#Auction details
best_bid = 0  #Highest bid received
winning_client = 0  #Client ID of the highest bidder

#Timer for auction end
timer_event = threading.Event()

#Main function to start the server
def main():
    global server, timer_event

    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('localhost', PORT))
        server.listen(5)

        print("Server started. Waiting for connections...")

        #Start the timer
        timer_thread = threading.Thread(target=timer_completion_routine, 
                                        args=(20, timer_event))
        timer_thread.start()

        while not timer_event.is_set():
            try:
                #Accept a new client connection
                server.settimeout(1)
                client_socket, _ = server.accept()
                print("Client connected:", client_socket.getpeername())

                #Find an available slot for the client
                client_id = -1
                for i in range(MAX_CLIENTS):
                    if clients[i] is None:
                        client_id = i
                        clients[i] = Client(client_socket, client_id + 1)
                        print("Client no.", client_id + 1, "connected.")
                        break

                #Handle client in a separate thread
                threading.Thread(target=handle_client, args=(client_id,)).start()
            except socket.timeout:
                continue

    except Exception as ex:
        print("Server error:", ex)
    finally:
        if server:
            server.close()

#Handle client bids
def handle_client(client_id):
    global best_bid, winning_client, timer_event

    try:
        client = clients[client_id]

        while not timer_event.is_set():
            bid = client.reader.readline().strip()
            if not bid:
                #Client disconnected
                print("Client disconnected:", client.socket.getpeername())
                clients[client_id] = None
                break

            bid_amount = int(bid)
            print("Received bid", bid_amount, "from client", client.id)

            if bid_amount > best_bid:
                best_bid = bid_amount
                winning_client = client.id

                msg = "New best bid: {} (Client: {})".format(best_bid, 
                                                             winning_client)
                broadcast_message(msg)
                print(msg)

                #Reset the timer
                timer_event.set()
                timer_event = threading.Event()
                threading.Thread(target=timer_completion_routine, 
                                 args=(20, timer_event)).start()
            else:
                msg = "Received lower bid. Best bid remains at: {}".format(best_bid)
                broadcast_message(msg)
                print(msg)

    except Exception as ex:
        print("Client error:", ex)

#Broadcast message to all clients
def broadcast_message(msg):
    for client in clients:
        if client:
            try:
                client.writer.write(msg + '\n')
                client.writer.flush()
            except Exception as ex:
                print("Send failed:", ex)

#Timer completion routine when auction ends
def timer_completion_routine(duration, event):
    global best_bid, winning_client

    time.sleep(duration)
    if not event.is_set():
        print("Auction finished. Winning bid:", best_bid
              , ", winner: client no.", winning_client)

        msg = "Auction finished. Winning bid: {}, "
        "winner: client no. {}".format(best_bid, winning_client)
        try:
            broadcast_message(msg)
        except Exception as ex:
            print("Broadcast message error:", ex)

        #Exit the program
        print("Exiting program...")
        event.set()
        exit()

if __name__ == "__main__":
    main()
