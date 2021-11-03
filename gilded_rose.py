MIN_QUALITY = 0
MAX_QUALITY = 50
LEGENDARY_MAX_QUALITY = 80
MIN_SELL_IN_VALUE = 0


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_item()


class ItemCollection:
    @staticmethod
    def create(name, sell_in, quality):
        if name == "Aged Brie":
            return AgedBrie(name, sell_in, quality)

        elif name == "BackStage Passes to a TAFKAL80ETC concert":
            return BackstagePasses(name, sell_in, quality)

        elif name == "Conjured Mana Cake":
            return ConjuredItem(name, sell_in, quality)

        elif name == "Sulfuras, Hand of Ragnaros":
            return LegendaryItem(name, sell_in, quality)
        else:
            return RegularItem(name, sell_in, quality)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class RegularItem(Item):
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

    def _update_sell_in(self) -> None:
        self.sell_in -= 1


class AgedBrie(RegularItem):
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
    def __init__(self, name, sell_in, quality):
        RegularItem.__init__(self, name, sell_in, quality)

    def _update_quality(self) -> int:
        if self.quality > LEGENDARY_MAX_QUALITY:
            return LEGENDARY_MAX_QUALITY
        else:
            return LEGENDARY_MAX_QUALITY

    def _update_sell_in(self) -> None:
        pass


class BackstagePasses(RegularItem):
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
    def __init(self, name, sell_in, quality):
        RegularItem.__init__(self, name, sell_in, quality)

    def _update_quality(self):
        if self.quality < 0:
            return MIN_QUALITY
        if self.sell_in >= 0:
            return max(self.quality - 2, MIN_QUALITY)
        else:
            return max(self.quality - 4, MIN_QUALITY)
