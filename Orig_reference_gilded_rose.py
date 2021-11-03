# -*- coding: utf-8 -*-
"""
This is original version of gilded_rose.py.
Added comments to understand the code and refer for improving the implementation
Do not change Item Class and its properties.
"""
class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            """
            If the item is not Aged Brie or Backstage, quality does not increase but it decrease by 1.
            for Sulfuras quality never changes
            """
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                """
                quality of Aged Brie, backstage passes increases by 1, if item quality is less than 50 and sell_in is greater than or equal to 0.
                Max quality of an item needs to be 50.
                """
                if item.quality < 50:
                    item.quality = item.quality + 1
                    """
                    quality of backstage passes increases by 2, if sell_in is less than 11.
                    And it increases by 3 if less than 6.
                    """
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            """
            Sell_in value for all the items decreases by 1. Dont change sell_in value for Sulfuras. Sulfuras is not a sell item
            """
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                """
                The quality of the item becomes 0 after sell_in date, if the item is not Aged brie, backstage passes and Sulfuras.
                """
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    """
                    Else the item quality increases by 1 for the items like Aged Brie, Sulfuras and backstage passes.
                    The quality of aged brie increases by 2  if sell_in is less than 0 (2 if-else conditions adding 1 to quality).
                    """
                    if item.quality < 50:
                        item.quality = item.quality + 1

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
