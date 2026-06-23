from fastapi import APIRouter
from app.services.market_overview import get_market_overview

router = APIRouter()

@router.get("/market-overview")
def market_overview():
    return get_market_overview()