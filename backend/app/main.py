import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.users_routes import router as user_router
from app.core.config import settings, MEDIA_DIR
from app.core.database import async_engine
from sqlmodel import SQLModel
from app.core.logging import logging
from alembic.config import Config
from alembic import command


app = FastAPI(title="Hostel Application", docs_url="/api_v1/docs", redoc_url="/api_v1/redoc")

# Mount media files directory
app.mount("/media", StaticFiles(directory=MEDIA_DIR), name="media")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, prefix="/users", tags=["Users"])


@app.on_event("startup")
async def on_startup():
    async with async_engine.begin() as conn:
        # Dynamically create or update tables
        await conn.run_sync(SQLModel.metadata.create_all)

@app.on_event("shutdown")
async def shutdown_event():
    logging.info("Shutting down application...")

@app.get("/")
async def root():
    return {"message": "Hostel Management API"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


@app.get("/health")
async def health_check():
    return {"status": "ok"}
