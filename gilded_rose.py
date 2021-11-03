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


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class NormalItem(Item):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def update_item(self):
        self._update_sell_in()
        self._update_quality()

    def _update_quality(self):
        if self.sell_in >= 0:
            return max(self.quality - 1, MIN_QUALITY)
        else:
            return max(self.quality - 2, MIN_QUALITY)

    def _update_sell_in(self) -> None:
        self.sell_in -= 1


class AgedItem(NormalItem):
    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    def _update_quality(self):
        if self.quality < 0:
            return MIN_QUALITY

        if sell_in >= 0 and self.quality > 0:
            return min(self.quality + 1, MAX_QUALITY)
        else:
            return min(self.quality + 2, MAX_QUALITY)


class LegendaryItem(NormalItem):
    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    def _update_quality(self) -> int:
        if self.quality > LEGENDARY_MAX_QUALITY:
            return LEGENDARY_MAX_QUALITY
        else:
            return LEGENDARY_MAX_QUALITY

    def _update_sell_in(self) -> None:
        pass


class TicketItem(NormalItem):
    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    def _update_quality(self):
        if sell_in > 10:
            return min(self.quality + 1, MAX_QUALITY)
        elif sell_in > 5:
            return min(self.quality + 2, MAX_QUALITY)
        elif sell_in >= 0:
            return min(self.quality + 3, MAX_QUALITY)
        else:
            return MIN_QUALITY


class ConjuredItem(NormalItem):
    def __init(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    def _update_quality(self):
        if self.quality < 0:
            return MIN_QUALITY
        if self.sell_in >= 0:
            return max(self.quality - 2, MIN_QUALITY)
        else:
            return max(self.quality - 4, MIN_QUALITY)
