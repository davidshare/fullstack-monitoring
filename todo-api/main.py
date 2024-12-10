from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from prometheus_fastapi_instrumentator import Instrumentator
from app.core.config import settings
from app.core.database import engine
from app.core.database import Base
from app.endpoints.v1 import v1_router

load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION
)
origins = [
    settings.FRONTEND_ORIGIN,  # Allow your frontend's origin
    # Add other origins if needed
]

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Adjust for your frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the Prometheus Instrumentator
instrumentator = Instrumentator()
instrumentator.instrument(app)
instrumentator.add(self=app)

Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}


@app.get("/api", status_code=200)
def api():
    return {
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat(),
        "message": "welcome to todos api"
    }


@app.get("/health", status_code=200)
def health():
    return {
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat()
    }


# Include API router
app.include_router(v1_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
