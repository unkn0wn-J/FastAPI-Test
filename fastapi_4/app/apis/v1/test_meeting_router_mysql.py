import httpx
from app import app

# 1. MeetingModel 임포트 추가
from app.tortoise_models.meeting import MeetingModel
from starlette.status import HTTP_200_OK
from tortoise.contrib.test import TestCase


class TestMeetingRouter(TestCase):
    async def test_api_create_meeting_mysql(self) -> None:
        # When
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app),
            base_url="http://test",
        ) as client:
            response = await client.post(url="/v1/mysql/meetings")

        # Then: 테스트 결과를 검증
        assert response.status_code == HTTP_200_OK

        # 2. 응답 데이터에서 실제 생성된 url_code를 가져와야 검증이 가능합니다.
        # 강의 로직상 response에 url_code가 포함되어 있다고 가정합니다.
        res_data = response.json()
        url_code = res_data.get("url_code")

        # 3. DB에 실제로 저장되었는지 확인
        assert (await MeetingModel.filter(url_code=url_code).exists()) is True
