# Secure Chat and Backgammon Application

## Overview

This project is a secure, web-based chat application integrated with a backgammon game. It leverages encrypted communication through a series of routers to ensure message confidentiality and integrity. The application uses Flask for the backend, HTML/CSS/JavaScript for the frontend, and employs AES and RSA encryption for secure messaging. Docker and Docker Compose are used to containerize and orchestrate the different services.

## Features

- **Real-Time Chat:** Exchange messages in a secure chat room.
- **Backgammon Game:** Play backgammon within the chat interface.
- **Encrypted Communication:** Ensures secure message transmission using AES and RSA encryption.
- **Scalable Architecture:** Utilizes Docker containers and Docker Compose for easy deployment and scalability.
- **Multi-Router Setup:** Messages pass through multiple routers to enhance security.

## Technologies Used

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **Encryption:** PyCryptodome (AES, RSA)
- **Containerization:** Docker, Docker Compose
- **Networking:** Socket Programming

## Directory Structure

```
├── chat/
│   ├── templates/
│   │   └── index.html
│   ├── main.py
│   └── chat.py
├── keys/
│   ├── private_key_1.pem
│   ├── private_key_2.pem
│   ├── private_key_3.pem
│   ├── public_key_1.pem
│   ├── public_key_2.pem
│   └── public_key_3.pem
├── router.py
├── sender.py
├── server.py
├── client.py
├── Dockerfile
├── router-Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup and Installation

### Prerequisites

- [Docker](https://www.docker.com/get-started) installed on your Linux machine.
- [Docker Compose](https://docs.docker.com/compose/install/) installed.

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/secure-chat-backgammon.git
   cd secure-chat-backgammon
   ```

2. **Generate Encryption Keys**

   The project includes a script to generate RSA key pairs.

   ```bash
   python3 key.py
   ```

   This will generate `private_key_*.pem` and `public_key_*.pem` files in the `keys/` directory.

3. **Build Docker Images**

   Ensure the Dockerfile and router-Dockerfile are properly configured.

   ```bash
   docker-compose build
   ```

4. **Start the Services**

   Launch all services using Docker Compose.

   ```bash
   docker-compose up
   ```

   This will start the routers, server, and applications as defined in the `docker-compose.yml` file.

5. **Access the Application**

   Open your browser and navigate to `http://localhost:5000` to access the chat and backgammon application.

## Usage

1. **Chat Functionality**

   - Enter your message in the input box and click "Send" or press Enter.
   - Messages are displayed in real-time within the chat window.

2. **Backgammon Game**

   - Click the "Roll Dice" button to play backgammon.
   - The dice results will be displayed, and you can interact with the backgammon board.

3. **Encryption and Communication**

   - Messages are encrypted using AES before being sent through the routers.
   - Each router decrypts and re-encrypts the messages, ensuring secure transmission.

## Configuration

- **Environment Variables:**

  The `docker-compose.yml` file sets environment variables for each router service, such as `AES_NUM` and `TARGET_SERVER_ADDRESS`. Adjust these as needed to configure the network topology.

- **Ports:**

  - **Router Ports:** 2001
  - **Application Ports:** 5000, 5001

## Security Considerations

- **Encryption Keys:** Ensure that the private keys (`private_key_*.pem`) are securely stored and not exposed publicly.
- **Docker Networks:** The services communicate over the `my_network` Docker bridge network. Ensure this network is properly secured.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries or support, please contact [your-email@example.com](mailto:khadem13khadem@gmail.com).
