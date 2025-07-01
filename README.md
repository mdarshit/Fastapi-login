# FastAPI Login API

A secure and efficient authentication API built with FastAPI and PostgreSQL. This API provides user registration, login functionality with JWT token authentication, and user profile retrieval.

## Features

- User registration with secure password hashing
- JWT-based authentication
- User login and token generation
- Protected routes with OAuth2 authentication
- User profile retrieval
- PostgreSQL database integration
- CORS middleware support

## Tech Stack

- **FastAPI**: High-performance web framework for building APIs
- **SQLAlchemy**: SQL toolkit and ORM
- **Pydantic**: Data validation and settings management
- **Passlib**: Password hashing (Argon2 and Bcrypt)
- **PyJWT**: JSON Web Token implementation
- **PostgreSQL**: Relational database
- **Python-dotenv**: Environment variable management

## Installation

### Prerequisites

- Python 3.13+
- PostgreSQL

### Setup

1. Clone the repository

2. Create a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -e .
   ```

4. Configure environment variables
   
   Create a `.env` file in the root directory with the following variables:
   ```
   DATABASE_URL=postgresql://username:password@localhost:5432/database_name
   SECRET_KEY=your_secret_key
   ```

5. Run the application
   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints

### Root
- `GET /`: Welcome message

### Authentication
- `POST /auth/register`: Register a new user
- `POST /auth/token`: Login and get access token
- `GET /auth/user/me`: Get current user details (requires authentication)

## API Documentation

After starting the application, you can access the interactive API documentation at:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Development

### Testing

Run tests using pytest:
```bash
pip install -e ".[dev]"
pytest
```

### Code Formatting

This project uses Ruff for code formatting and linting:
```bash
ruff check .
ruff format .
```

## Security Features

- Password hashing with Argon2 (with Bcrypt fallback)
- JWT token authentication
- Token expiration
- Protected routes with OAuth2

## License

MIT