class ShopItem:
    """Represents a store item.

    Attributes
    ----------
    raw: :class:`dict`
        Raw data from SnailAPI (can be used to reconstruct object)
    name: :class:`str`:
        Display Name of this shop item.
    description: :class:`str`:
        The displayed description of this shop item.
    rarity: :class:`str`:
        The displayed rarity of this shop item.
    icon: :class`str`:
        URL of the main icon.
    featured_icon: :class:`str`:
        URL of the featured icon.
    other_items: :class:`list`:
        Any other items which are included in this shop item. (not bundle)
    price: :class`str`:
        V-Buck price of this shop item.
    offer_id: :class`str`:
        Offer ID for this shop item.
    panel: :class`str`:
        The panel the shop item is displayed in.
    is_giftable: :class`bool`:
        Whether or not this shop item is giftable.
    is_refundable: :class`bool`:
        Whether or not this shop item is giftable.
    price_without_discount: :class`int`:
        Shop item price without any sort of discounts.
    items: :class`list`:
        Shop item items, None if the shop item is not a bundle.
    details_icon: :class`str`:
        URL of the details icon, None if shop item is not a bundle.

    """
    def __init__(self, data: dict) -> None:
        self.raw = data

        self.name = data.get('name')
        self.description = data.get('name')
        self.rarity = data.get('rarity')
        self.icon = data.get('icon')
        self.featured_icon = data.get('featuredIcon')
        self.other_items = data.get('otherItems')
        self.price = data.get('price')
        self.offer_id = data.get('offerid')
        self.panel = data.get('panel')
        self.is_giftable = data.get('bIsGiftable')
        self.is_refundable = data.get('bIsRefundable')
        self.price_without_discount = data.get('priceWithoutDiscount')
        self.items = data.get('items', None)
        self.details_icon = data.get('detailsIcon', None)


class BRShop:
    """Represents a Battle Royale shop.

    Attributes
    ----------
    raw: :class:`dict`
        Raw data from SnailAPI (can be used to reconstruct object)
    featured: :class:`list[:class`ShopItem`]`:
        List containing all featured items as ShopItem objects.
    daily: :class:`list[:class`ShopItem`]`:
        List containing all daily items as ShopItem objects.
    special_featured: :class:`list[:class`ShopItem`]`:
        List containing all special featured items as ShopItem objects.
    special_daily: :class:`list[:class`ShopItem`]`:
        List containing all special daily items as ShopItem objects.

    """
    def __init__(self, data: dict) -> None:
        self.raw = data

        self.featured = [ShopItem(featured_item) for featured_item in data.get('featured')]
        self.daily = [ShopItem(daily_item) for daily_item in data.get('daily')]
        self.special_featured = [ShopItem(special_f_item) for special_f_item in data.get('specialFeatured')]
        self.special_daily = [ShopItem(special_d_item) for special_d_item in data.get('specialDaily')]