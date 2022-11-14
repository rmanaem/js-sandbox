from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def company_name():
    return {"name": "Some Company, LLC"}


@router.get("/employees")
async def number_of_employees():
    return 77
