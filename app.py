""" This module is the entry point of the application 
        - app: This is the FastAPI instance
        - root: This function returns the root route
        - status: This function returns the status route
"""

from fastapi import FastAPI
from router.user import router as user_router
from config.database import Base, engine
from fastapi.responses import JSONResponse
from fastapi import Request
import uvicorn

app = FastAPI(
    title="User Management API",
    description="This is a simple User Management API",
    version="0.1.0",
)

app.include_router(user_router)

Base.metadata.create_all(bind=engine)


@app.exception_handler(500)
async def handles_internal_server_error(request: Request, exc: str) -> JSONResponse:
    """This handles the 500 Internal Server Error"""
    return JSONResponse(
        status_code=500,
        content={
            "message": "There is an issue with the server try again later",
            "error": str(exc),
        },
    )


@app.exception_handler(404)
async def handles_not_found(request: Request, exc: str) -> JSONResponse:
    """This handles the 404 Not Found Error"""
    return JSONResponse(
        status_code=404,
        content={"message": f"Resource not found", "error": str(exc)},
    )


@app.get("/", tags=["Root"])
async def root():
    """This function returns the root route"""
    return {
        "title": "Welcome to the User Management API",
        "description": "This is a simple User Management API",
        "version": "0.1.0",
        "documentation": "/api/v1/docs",
    }


@app.get("/status", tags=["Status"])
async def status():
    """ " This function returns the status route"""
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
