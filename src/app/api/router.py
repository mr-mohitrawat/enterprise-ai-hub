from fastapi import APIRouter
from app.api.routes.v1.chat import router as chat_router
from app.api.routes.v1.auth import router as auth_router
router = APIRouter()

router.include_router(chat_router, prefix="/v1", tags = ["chat"])
router.include_router(auth_router, prefix="/v1", tags= ["auth"])