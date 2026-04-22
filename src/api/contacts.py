from fastapi import APIRouter

router = APIRouter(prefix="/contacts", tags=["contacts"])


@router.get("/")
def get_contacts_placeholder() -> dict[str, str]:
    return {"message": "Contacts endpoint placeholder"}
