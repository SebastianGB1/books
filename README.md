# Books Application

This project contains a backend application (Flask), a frontend application (Angular), and a MySQL database, all orchestrated using Docker Compose.

## Live Demo

You can try the live demo of the application by clicking the following link:

[Live Demo](http://129.146.172.208:8080)

## Prerequisites

Before running the application, ensure that you have the following installed:

- **[Docker](https://www.docker.com/products/docker-desktop)**: You will need Docker to run the containers.
- **[Docker Compose](https://docs.docker.com/compose/install/)**: Make sure Docker Compose is installed. Docker Compose is used to define and run multi-container applications.
- **Git**: To clone the repository.

## Installation Instructions

### 1. Clone the repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/SebastianGB1/books.git
cd books
```

### 2. Build and Run the Application

Once you have cloned the repository and are inside the project directory, use Docker Compose to build and bring up the containers:

```bash
docker-compose up --build
```
This command will download the necessary images, build the containers, and start the application.

### 3. Access the Application
- Frontend (Angular): Access the user interface at http://localhost:8080.
- Backend (Flask API): The backend API will be available at http://localhost:8000.
- Database (MySQL): The MySQL database will be available on port 3306.

### Postman Collection
A Postman collection is included in the repository to test the API endpoints. You can import this collection into Postman and use it to interact with the backend API.

- The collection is located in the ./postman/ directory.
- The collection contains pre-configured requests for the most common API operations such as creating, reading, updating, and deleting books.