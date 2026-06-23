from fastapi import APIRouter
from app.services.market_service import get_stock_data

router = APIRouter()

@router.get("/stock/{symbol}")
def stock_details(symbol: str):
    return get_stock_data(symbol)