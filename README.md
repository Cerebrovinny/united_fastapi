## United Fastapi
A FastAPI in Python to get employeer data from the United Healthcare price transparency page,
The API is writen with Typed Python and FastAPI

### How to run
1. Clone the repository
2. Run ```docker-compose up```
3. Go to http://localhost:8000/docs

### Endpoints
#### /employeer
Get all employeers

#### /employeer/{employeer_name}
Get employeer by name

#### /employeer/{employeer_id}
Get employeer by id

### Stack
- Python 3.8
- FastAPI
- Docker
- Docker Compose
- Pydantic
- Uvicorn