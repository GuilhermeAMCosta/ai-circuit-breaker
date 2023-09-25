from fastapi import APIRouter, status

from app.version import __version__

router = APIRouter(tags=["Helpers"])


@router.get(
    path="/health",
    summary="Check health of application",
    status_code=status.HTTP_200_OK,
)
def health_check():
    return {"message": "OK", "version": __version__}
