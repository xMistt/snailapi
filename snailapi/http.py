import aiohttp
import json
from typing import Any, Dict, Union


async def json_or_text(response: aiohttp.ClientResponse) -> Union[str, dict]:
    text = await response.text(encoding='utf-8')
    if 'application/json' in response.headers.get('content-type', ''):
        return json.loads(text)
    return text


class HTTPClient:
    def __init__(self, connector=None, base: str = 'https://snail-api.com/v1') -> None:
        self.connector = connector
        self.base = base

    async def request(self, url: str, method: str = 'GET', params: Dict[Any, Any] = None, **kwargs) -> Dict[Any, Any]:
        async with aiohttp.ClientSession() as session:
            async with session.request(method=method, url=f'{self.base}{url}', params=params, **kwargs) as request:
                return await json_or_text(request)
