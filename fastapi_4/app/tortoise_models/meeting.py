from __future__ import annotations

from tortoise import Model, fields

from app.tortoise_models.base_model import BaseModel


class MeetingModel(BaseModel, Model): # type: ignore
    url_code = fields.CharField(max_length=255, unique=True)

    class Meta:
        table = "meetings"

    @classmethod
    async def create_meeting(cls, url_code: str) -> "MeetingModel": # 따옴표로 감싸기
        return await cls.create(url_code=url_code)