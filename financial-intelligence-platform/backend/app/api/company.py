from fastapi import APIRouter, Query
from app.services.company_service import (
    search_companies,
    get_company_details
)

router = APIRouter()


@router.get("/company-search")
def company_search(
    query: str = Query(..., min_length=1)
):
    return search_companies(query)


@router.get("/company-details")
def company_details(
    symbol: str = Query(..., min_length=1)
):
    return get_company_details(symbol)