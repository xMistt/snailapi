class FortniteAES:
    """Represents a Fortnite dynamic AES key.

    Attributes
    ----------
    aes: :class:`str`
        AES key itself.
    pak: :class:`str`:
        The pack the AES key is used for.
    guid: :class:`str`:
        AES guid.
    ids: :class:`list`:
        Cosmetics which use AES key.

    """
    def __init__(self, data: dict) -> None:
        self.raw = data

        print(data)

        self.aes = data.get('aes')
        self.pak = data.get('pak')
        self.guid = data.get('guid')
        self.ids = data.get('ids')
