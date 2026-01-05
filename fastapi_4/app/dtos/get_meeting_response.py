from pydantic import BaseModel

from fastapi_4.app.dtos.frozen_config import FROZEN_CONFIG


class GetMeetingResponse(BaseModel):
    model_config = FROZEN_CONFIG

    url_code: str
