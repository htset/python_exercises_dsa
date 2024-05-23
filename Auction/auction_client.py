import socket
import threading

#Constants
PORT = 8080  #Port number to connect to the server
SERVER_IP = "127.0.0.1"  #Server IP address

client = None
is_running = True
receive_thread = None

#Main function to start the client
def main():
    global client, receive_thread, is_running

    #Connect to the server
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((SERVER_IP, PORT))
        print("Connected to server.")
    except Exception as ex:
        print("Connect failed:", ex)
        return

    #Start receive handler thread
    receive_thread = threading.Thread(target=receive_handler)
    receive_thread.start()

    #Send bids until the user quits
    try:
        while is_running:
            bid = input("\nEnter your bid (or 'q' to quit): ")
            if bid.lower() == 'q':
                is_running = False
                client.close()
                receive_thread.join()  #Wait for the receive thread to finish
                break

            try:
                client.sendall((bid + '\n').encode('utf-8'))
            except Exception as ex:
                print("Send failed:", ex)
                return
    except Exception as e:
        print("Error:", e)
    finally:
        #Ensure client is closed
        if client:
            client.close()

#Handle incoming messages from the server
def receive_handler():
    global is_running
    try:
        while is_running:
            message = client.recv(1024).decode('utf-8')
            if not message:
                print("\nServer disconnected.")
                is_running = False
                break

            print("\nServer:", message)

            if message.startswith("Auction"):
                print("Auction ended. Exiting program.")
                is_running = False
                break
    except Exception as ex:
        if is_running:
            print("Receive failed:", ex)

if __name__ == "__main__":
    main()
