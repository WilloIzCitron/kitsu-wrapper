import aiohttp

from .errors import *
from .models import *


class Client:
    def __init__(self):
        self._models = {"anime": Anime, "manga": Manga}
        self._base_url = 'https://kitsu.io/api/edge'
        self.__headers = {
            "Accept": "application/vnd.api+json",
            "Content-Type": "application/vnd.api+json"
        }

    async def search(self, type_: str, query: str, limit: int = 10):
        model = self._models.get(type_)
        if model is None:
            raise InvalidType('You gave me an invalid type! Supported types: '
                              + ', '.join(self._models.keys()))

        async with aiohttp.ClientSession(headers=self.__headers) as session:
            async with session.get(self._base_url + f'/{type_}?filter[text]={query}&page[limit]={limit}') as resp:
                if resp.status != 200:
                    raise ResponseError(f'Response returned with code {resp.status}')

                json = await resp.json()

                return [model(type_, data) for data in json['data']]
