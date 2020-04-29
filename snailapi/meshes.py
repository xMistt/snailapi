from .exceptions import NotFound, InvalidParameters

from typing import Any, Tuple


class CosmeticMesh:
    """Represents a Fortnite cosmetic.

    Attributes
    ----------
    raw: :class:`dict`
        Raw data from SnailAPI (can be used to reconstruct object)
    name: :class:`str`:
        Display Name of this mesh.
    id: :class:`str`:
        ID of the mesh
    meshes: :class:`list`:
        Raw mesh data.

    """
    def __init__(self, data: dict) -> None:
        self.raw = data

        self.name = data.get('name')
        self.id = data.get('id')
        self.meshes = data.get('meshes')


async def _search_parameters(**search_parameter: Any) -> Tuple[Any, Any]:
    """Function to convert dictionary to parameters."""
    if len(search_parameter) == 0 or len(search_parameter) > 1:
        raise InvalidParameters('More than/less than 1 search parameter provided.')

    for key, value in search_parameter.items():
        return key, value


class Meshes:
    def __init__(self, client) -> None:
        self.http = client.http

    async def get_all_meshes(self) -> list:
        """|coro|

        Gets a list of every mesh for skins and pickaxes.

        Returns
        -------
       :class:`list[:class`CosmeticMesh`]`:
            List of all meshes that exist in CosmeticMesh objects.
        """

        data = await self.http.request(
            method="GET",
            url="/meshes"
        )

        return [CosmeticMesh(mesh_data) for mesh_data in data]

    async def search_meshes(self, **search_parameters: dict) -> list:
        """|coro|

        Gets a list of every mesh for skins and pickaxes under a certain query.

        Parameters
        ----------
        id: Optional[:class:`str`]
            ID of a cosmetic
        name: Optional[:class:`str`]
            Name of a cosmetic

        Raises
        ------
        InvalidParameters
            If none or more than 1 parameters are provided.
        NotFound
            If no cosmetics are found matching parameters.

        Returns
        -------
        :class:`list[:class`CosmeticMesh`]`:
            List of CosmeticMesh objects containing information of meshes matching parameters.
        """

        if len(search_parameters) == 0:
            raise InvalidParameters('No search parameters provided. At least 1 is required.')

        data = await self.http.request(
            method="GET",
            url="/meshes/search",
            params=search_parameters
        )

        if len(data) == 0:
            raise NotFound(f"No cosmetics found matching parameters.")

        if 'error' in data:
            raise InvalidParameters(f"{data['error']}.")

        return [CosmeticMesh(mesh_data) for mesh_data in data]
