from items import Products

MIN_QUALITY = 0
MAX_QUALITY = 50
LEGENDARY_MAX_QUALITY = 80

class GildedRose(object):

    def __init__(self, items):
        """
        Args:
            items(list): List of items
        """
        self.items = items

    def update_quality(self):
        """
        Iterates through input list and updates the item
        """
        for item in self.items:
            item.update_item()


class ItemCollection:
    """
    Checks if the product is a specific (Aged Brie, BackStage Passes, Conjured or
    Sulfuras- Legendary) or a regular product and creates a product instance.

        Args:
            name (str): item name.
            sell_in (int): number of days we have left to sell the item.
            quality (int): item quality value.

        Returns:
            item object: Calls a specific product updater.
    """
    @staticmethod
    def create(name, sell_in, quality):
        if name == Products.AGED_BRIE.value:
            return AgedBrie(name, sell_in, quality)

        elif name == Products.BACKSTAGE_PASSES.value:
            return BackstagePasses(name, sell_in, quality)

        elif name == Products.CONJURED.value:
            return ConjuredItem(name, sell_in, quality)

        elif name == Products.SULFURAS.value:
            return LegendaryItem(name, sell_in, quality)
        else:
            return RegularItem(name, sell_in, quality)


class Item:
    """
    Used to describe the item properties
        Args:
            name (str): item name.
            sell_in (int): number of days we have to sell the item.
            quality (int): item quality value.
    """
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class RegularItem(Item):
    """
    Updates regular product quality. The Quality of an item is never negative.

    Regular product's quality:
        - decreases by 1 before sell by date
        - by 2 after sell by date passes.
    """
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def update_item(self):
        self._update_sell_in()
        self.quality = self._update_quality()

    def _update_quality(self):
        if self.sell_in >= 0:
            return max(self.quality - 1, MIN_QUALITY)
        else:
            return max(self.quality - 2, MIN_QUALITY)

    def _update_sell_in(self):
        """
        Decreases sell_in date
        """
        self.sell_in -= 1


class AgedBrie(RegularItem):
    """
    Increase the quality by day for Brie till sell_in value is greater or equal to 0.
    And increase by 2 after sell_in date is passed. Max quality is the value of MAX_QUALITY
    """
    def __init__(self, name, sell_in, quality):
        RegularItem.__init__(self, name, sell_in, quality)

    def _update_quality(self):
        if self.quality < 0:
            return MIN_QUALITY

        if self.sell_in >= 0 and self.quality > 0:
            return min(self.quality + 1, MAX_QUALITY)
        else:
            return min(self.quality + 2, MAX_QUALITY)


class LegendaryItem(RegularItem):
    """
        Quality of legendary item never goes down. Max quality is the value of LEGENDARY_MAX_QUALITY
        "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
    """
    def __init__(self, name, sell_in, quality):
        RegularItem.__init__(self, name, sell_in, quality)

    def _update_quality(self):
        if self.quality > LEGENDARY_MAX_QUALITY:
            return LEGENDARY_MAX_QUALITY
        else:
            return LEGENDARY_MAX_QUALITY

    def _update_sell_in(self) -> None:
        pass


class BackstagePasses(RegularItem):
    """
    "Backstage passes", like aged brie, increases in Quality as its SellIn value approaches
    Quality increases
        by 2 when there are 10 days or less
        by 3 when there are 5 days or less but
        Quality drops to 0 after the concert (after sell_in is equal to 0 or less).
    """
    def __init__(self, name, sell_in, quality):
        RegularItem.__init__(self, name, sell_in, quality)

    def _update_quality(self):
        if self.sell_in > 10:
            return min(self.quality + 1, MAX_QUALITY)
        elif self.sell_in > 5:
            return min(self.quality + 2, MAX_QUALITY)
        elif self.sell_in >= 0:
            return min(self.quality + 3, MAX_QUALITY)
        else:
            return MIN_QUALITY


class ConjuredItem(RegularItem):
    """
    "Conjured" items degrade in Quality twice as fast as regular items
    """
    def __init(self, name, sell_in, quality):
        RegularItem.__init__(self, name, sell_in, quality)

    def _update_quality(self):
        if self.quality < 0:
            return MIN_QUALITY

        if self.sell_in >= 0:
            return max(self.quality - 2, MIN_QUALITY)
        else:
            return max(self.quality - 4, MIN_QUALITY)
