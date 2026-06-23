from fastapi import APIRouter, Query
from app.services.company_service import search_companies

router = APIRouter()

@router.get("/company-search")
def company_search(
    query: str = Query(..., min_length=1)
):
    return search_companies(query)