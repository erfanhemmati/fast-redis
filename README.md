
# FastAPI Redis Example

This is a simple FastAPI application that demonstrates basic CRUD operations using Redis as the backend database. The application is containerized using Docker and managed with Docker Compose.

## Features

- **Store data**: Save key-value pairs in Redis.
- **Retrieve data**: Fetch stored values using their keys.
- **CORS support**: Configured to allow cross-origin requests for development.

## Requirements

- Docker and Docker Compose
- Python 3.12
- Redis

## Setup and Installation

### Clone the Repository

```bash
git clone https://github.com/erfanhemmati/fast-redis.git
cd fast-redis
```

### Build and Run with Docker Compose

1. **Build the Docker containers:**

   ```bash
   docker compose build
   ```

2. **Run the Docker containers:**

   ```bash
   docker compose up
   ```

3. The FastAPI server will be running on `http://127.0.0.1:8080`. The Redis service is accessible only within the Docker network.

### Endpoints

- **Health Check:**
  - `GET /` - Returns a simple "Hello World!" message.

- **Store Data:**
  - `POST /api/v1/store`
  - Request body:
    ```json
    {
      "key": "exampleKey",
      "value": "exampleValue"
    }
    ```
  - Responses:
    - 200: Item successfully stored.
    - 409: Item already exists.

- **Retrieve Data:**
  - `GET /api/v1/show/{key}`
  - Responses:
    - 200: Returns the stored value.
    - 404: Item not found.

### Configuration

- The application uses the `REDIS_HOST` environment variable to connect to Redis. By default, it is set to `redis` (as configured in `docker-compose.yml`).

### Requirements

The project dependencies are specified in `requirements.txt`:

```
fastapi==0.111.0
uvicorn==0.30.1
requests==2.32.3
redis==5.0.7
```

### Running Locally Without Docker

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the FastAPI app:**

   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

3. The app will be available at `http://127.0.0.1:8000`.

## Development

To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/) - A modern, fast (high-performance) web framework for building APIs with Python 3.6+.
- [Redis](https://redis.io/) - An open-source, in-memory key-value data structure store.

## Contact

For any questions or comments, please open an issue or reach out via [email](mailto:e.hemmati.19@gmail.com).
