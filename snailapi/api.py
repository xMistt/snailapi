from .http import HTTPClient
from .cosmetics import Cosmetics
from .epic import EpicEndpoints
from .meshes import Meshes
from .shop import BRShop
from .aes import FortniteAES

from typing import Any


class APIClient:
    def __init__(self) -> None:
        self.http = HTTPClient()

        self.cosmetics = Cosmetics(self)
        self.epic = EpicEndpoints(self)
        self.meshes = Meshes(self)

    async def get_shop(self) -> BRShop:
        """|coro|

        Gets a parsed version of the current battle royale shop (updates every day at UTC 0:00).

        Returns
        -------
       :class`BRShop`:
            BRShop object containing featured, daily, specialFeatured and specialDaily.
        """

        data = await self.http.request(
            method="GET",
            url="/shop/br"
        )

        return BRShop(data)

    async def get_dynamic_aes_keys(self) -> list:
        """|coro|

        Gets all current dynamic AES keys. Returns None if there is no dynamic aes keys.

        Returns
        -------
        :class:`list[:class`FortniteAES`]`:
            List containing FortniteAES objects containing dynamic key information.
        """

        data = await self.http.request(
            method="GET",
            url="/aes/dynamic"
        )

        return [FortniteAES(dynamic_key) for dynamic_key in data] if len(data) is not 0 else None

    async def get_main_aes_key(self) -> str:
        """|coro|

        Gets the main AES key in its 32 byte hex form. Updates within a few seconds of a update.

        Returns
        -------
        :class:`str`:
            Main aes key in 32 byte hex form.
        """

        return await self.http.request(method="GET", url="/aes/main")

