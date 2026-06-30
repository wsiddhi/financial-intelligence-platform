from fastapi import FastAPI

from app.api.market import router as market_router
from app.api.market_overview import router as overview_router
from app.api.company import router as company_router

app = FastAPI(
    title="Financial Intelligence Platform",
    version="1.0.0",
    description="An API platform for retrieving financial market data, overviews, and company analysis."
)

app.include_router(
    market_router,
    prefix="/api",
    tags=["Market"]
)

app.include_router(
    overview_router,
    prefix="/api",
    tags=["Market Overview"]
)

app.include_router(
    company_router,
    prefix="/api",
    tags=["Company Search"]
)

@app.get("/")
def root():
    return {
        "message": "Financial Intelligence Platform API Running"
    }
