from .exceptions import InvalidParameters, NotFound

from typing import Dict, Any, Tuple


class BRCosmetic:
    """Represents a Fortnite cosmetic.

    Attributes
    ----------
    raw: :class:`dict`
        Raw data from SnailAPI (can be used to reconstruct object)
    name: :class:`str`:
        Display Name of this cosmetic.
    description: :class:`str`:
        The displayed description of this cosmetic.
    rarity: :class:`str`:
        The displayed rarity of this cosmetic.
    backend_rarity: :class:`str`:
        The rarity of this cosmetic in the backend.
    type: :class:`str`:
        The displayed type of this cosmetic.
    backend_type: :class`str`:
        The type of this cosmetic in the backend.
    id: :class`str`:
        The id of the cosmetic.
    gameplay_tags: :class`list`:
        The gameplay tags of this cosmetic.
    set: :class`str`:
        The displayed set of this cosmetic.
    variants: :class`list`:
        The data of the cosmetics variants.
    icon: :class`str`:
        URL of the main icon.

    """
    def __init__(self, data: dict) -> None:
        self.raw = data

        self.name = data.get('name')
        self.description = data.get('description')
        self.rarity = data.get('rarity')
        self.backend_rarity = data.get('backendRarity')
        self.type = data.get('type')
        self.backend_type = data.get('backendType')
        self.id = data.get('id')
        self.gameplay_tags = data.get('gameplayTags')
        self.set = data.get('set')
        self.variants = data.get('variants')
        self.icon = data.get('icon')


async def _search_parameters(**search_parameter: Any) -> Tuple[Any, Any]:
    """Function to convert dictionary to parameters."""
    if len(search_parameter) == 0 or len(search_parameter) > 1:
        raise InvalidParameters('More than/less than 1 search parameter provided.')

    for key, value in search_parameter.items():
        return key, value


class Cosmetics:
    def __init__(self, client) -> None:
        self.http = client.http

    async def get_all_cosmetics_ids(self) -> list:
        """|coro|

        Gets a list of every cosmetics ID.

        Returns
        -------
        :class:`list`:
            List of all cosmetics IDs.
        """

        return await self.http.request(method="GET", url="/cosmeticids")

    async def search_cosmetics(self, **search_parameters: dict) -> list:
        """|coro|

        Gets a list of every cosmetic that falls under a certain query.

        Parameters
        ----------
        description: Optional[:class:`str`]
            Description of a cosmetic.
        id: Optional[:class:`str`]
            ID of a cosmetic.
        name: Optional[:class:`str`]
            Name of a cosmetic.
        rarity: Optional[:class:`str`]
            Rarity of a cosmetic.
        set: Optional[:class:`str`]
            Set of cosmetic.
        type: Optional[:class:`str`]
            Type of a cosmetic.

        Raises
        ------
        InvalidParameters
            If none or more than 1 parameters are provided.
        NotFound
            If no cosmetics are found matching parameters.

        Returns
        -------
        List[:class:`BRCosmetic`]:
            List of BRCosmetic objects containing information of cosmetics matching parameters.
        """

        parameters = await _search_parameters(**search_parameters)
        data = await self.http.request(
            method="GET",
            url="/cosmetics/search",
            params={parameters[0]: parameters[1]}
        )

        if len(data) == 0:
            raise NotFound(f"No cosmetics found matching parameters.")

        return [BRCosmetic(cosmetic_data) for cosmetic_data in data]

    async def get_all_cosmetics(self) -> list:
        """|coro|

        Gets a list of every single battle royale cosmetic.

        Returns
        -------
        :class:`list[:class`BRCosmetic`]`:
            List of all cosmetics that exist in BRCosmetic objects.
        """

        data = await self.http.request(
            method="GET",
            url="/cosmetics"
        )

        return [BRCosmetic(cosmetic_data) for cosmetic_data in data]
