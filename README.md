# My Web App

A simple FastAPI web application with a full CRUD REST API.

## Project Structure

```
webapp/
├── app/
│   ├── main.py          # App entry point, middleware, route mounting
│   └── routers/
│       └── items.py     # Items CRUD endpoints
├── tests/
│   └── test_items.py    # Pytest test suite
├── requirements.txt
└── README.md
```

## Setup

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the development server
uvicorn app.main:app --reload
```

The app will be live at **http://localhost:8000**.  
Interactive API docs: **http://localhost:8000/docs**

## Endpoints

| Method | Path          | Description        |
|--------|---------------|--------------------|
| GET    | /             | Welcome message    |
| GET    | /health       | Health check       |
| GET    | /items/       | List all items     |
| POST   | /items/       | Create an item     |
| GET    | /items/{id}   | Get one item       |
| PUT    | /items/{id}   | Update an item     |
| DELETE | /items/{id}   | Delete an item     |

## Running Tests

```bash
pytest tests/ -v
```

## Next Steps

- Swap the in-memory store in `routers/items.py` for a real database (SQLite via SQLModel, or PostgreSQL via asyncpg)
- Add authentication with `fastapi-users` or a custom JWT middleware
- Add a `.env` file and load config with `pydantic-settings`
