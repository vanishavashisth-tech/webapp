from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import items

app = FastAPI(
    title="My Web App",
    description="A simple FastAPI web application",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(items.router, prefix="/items", tags=["items"])


@app.get("/")
def root():
    return {"message": "Welcome to My Web App!", "docs": "/docs"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
