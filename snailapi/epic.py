class EpicEndpoints:
    def __init__(self, client) -> None:
        self.http = client.http

    async def get_catalog(self) -> list:
        """|coro|

        Gets the catalog data from epic servers.

        Returns
        -------
        :class:`dict`:
            Raw catalog response of Epic Games API.
        """

        return await self.http.request(method="GET", url="/catalog")

    async def get_cloudstorage(self, file_param: str = None) -> dict:
        """|coro|

        Gets the cloudstorage JSON or returns a certain file if specified.

        Returns
        -------
        :class:`dict`:
            Raw cloudstorage response of Epic Games API.
        """

        return await self.http.request(
            method="GET",
            url="/cloudstorage",
            params={} if file_param is None else {"file": file_param}
        )

    async def get_keychain(self) -> list:
        """|coro|

        Gets the keychain data from epic servers.

        Returns
        -------
        :class:`list`:
            Raw keychain response of Epic Games API.
        """

        return await self.http.request(
            method="GET",
            url="/keychain"
        )

    async def get_timeline(self) -> dict:
        """|coro|

        Gets the timeline/eventflag data from epic servers.

        Returns
        -------
        :class:`dict`:
            Raw timeline response of Epic Games API.
        """

        return await self.http.request(
            method="GET",
            url="/timeline"
        )
