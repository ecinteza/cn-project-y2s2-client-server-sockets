# Client-Server Socket Project

This project demonstrates a basic **client-server** architecture using **sockets**. It consists of two components: a server that listens for incoming connections and handles requests, and a client that connects to the server to send and receive data. This setup is useful for building networked applications such as chat systems, multiplayer games, or file transfer services.

## Features

- **Bidirectional communication** between client and server.
- **Multi-threaded server** capable of handling multiple client connections simultaneously.
- Basic error handling and logging.
- Platform independent (works on Linux, Windows, and macOS).

## Getting Started

These instructions will help you set up and run the client and server components on your local machine.

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.x
- Basic understanding of networking and sockets

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/ecinteza/cn-project-y2s2-client-server-sockets.git
   cd cn-project-y2s2-client-server-sockets
   ```

2. **Install required dependencies** (if any):

   This project doesn’t require any external libraries beyond Python's built-in `socket` library.

### Running the Server

To start the server, run the following command:

```bash
python server.py
```

- The server will listen on a specific port (by default, it is set to **PORT** in the `server.py` file).
- The server waits for incoming client connections and starts a new thread for each client.

### Running the Client

To connect to the server as a client, run:

```bash
python client.py
```

- The client will attempt to connect to the server's IP address and port (configured in `client.py`).
- Once connected, the client can send messages to the server, and the server will respond accordingly.

### Configuration

You can modify the following settings:

- **Server IP Address**: Set the server IP in the `client.py` file.
- **Port**: Both `server.py` and `client.py` use a default port for communication. You can change this port if needed.
- **Number of Connections**: In `server.py`, you can specify the maximum number of client connections.

### Example Interaction

1. Run the server:

   ```bash
   python server.py
   ```

   Output:

   ```bash
   Server started on port 12345...
   Waiting for connections...
   ```

2. Run the client:

   ```bash
   python client.py
   ```

   Output:

   ```bash
   Connected to server at 127.0.0.1:12345
   ```

   Now, you can start sending messages from the client, and the server will respond accordingly.

### How It Works

- The **server** creates a socket and binds it to a specific address and port, then listens for incoming connections.
- Each client that connects gets a dedicated thread to handle communication, allowing multiple clients to interact with the server concurrently.
- The **client** initiates a connection by providing the server's IP address and port. Once connected, it can send messages, and the server processes and responds to these messages.

### Future Improvements

- **Authentication**: Add a basic authentication layer for secure client-server communication.
- **Data Encryption**: Use SSL/TLS for secure data transmission.
- **GUI**: Implement a graphical user interface (GUI) for ease of use.

### Troubleshooting

- **Connection refused**: Make sure the server is running and the client is using the correct IP address and port.
- **Port already in use**: Ensure the port is not occupied by another application or modify the port in the code.
- **Firewall issues**: Ensure that your firewall allows traffic on the specified port.

### Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
