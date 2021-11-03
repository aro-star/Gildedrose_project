# -*- coding: utf-8 -*-
import unittest
from gilded_rose import Item, GildedRose
from gilded_rose import RegularItem, AgedBrie, LegendaryItem, BackstagePasses, ConjuredItem


class GildedRoseUpdatedTest(unittest.TestCase):
    # Regular Products
    def test_regular_item_before_sell_date(self):
        items = [RegularItem("foo", 10, 4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(3, items[0].quality)

    def test_regular_item_on_sell_date(self):
        items = [RegularItem("foo", 0, 9)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(7, items[0].quality)

    def test_regular_item_after_sell_date(self):
        items = [RegularItem("foo", -10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-11, items[0].sell_in)
        self.assertEqual(8, items[0].quality)

    def test_regular_with_zero_quality(self):
        items = [RegularItem("foo", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    # Brie
    def test_brie_before_sell_date(self):
        items = [AgedBrie("Aged Brie", 2, 0)]
        item = GildedRose(items)
        item.update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(2, items[0].quality)

    def test_brie_on_sell_date(self):
        items = [AgedBrie("Aged Brie", 0, 0)]
        item = GildedRose(items)
        item.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(2, items[0].quality)

    def test_brie_after_sell_date(self):
        items = [AgedBrie("Aged Brie", -10, 0)]
        item = GildedRose(items)
        item.update_quality()
        self.assertEqual(-11, items[0].sell_in)
        self.assertEqual(2, items[0].quality)

    def test_brie_max_quality(self):
        items = [AgedBrie("Aged Brie", 2, 50)]
        item = GildedRose(items)
        item.update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_brie_over_max_quality(self):
        items = [AgedBrie("Aged Brie", 2, 52)]
        item = GildedRose(items)
        item.update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_brie_negative_quality(self):
        items = [AgedBrie("Aged Brie", 2, -5)]
        item = GildedRose(items)
        item.update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    # Sulfuras
    def test_sulfuras_on_sell_date(self):
        items = [LegendaryItem("Sulfuras, Hand of Ragnaros", 0, 80)]
        item = GildedRose(items)
        item.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_sulfuras_before_sell_date(self):
        items = [LegendaryItem("Sulfuras, Hand of Ragnaros", 10, 80)]
        item = GildedRose(items)
        item.update_quality()
        self.assertEqual(10, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_sulfuras_after_sell_date(self):
        items = [LegendaryItem("Sulfuras, Hand of Ragnaros", -1, 80)]
        item = GildedRose(items)
        item.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_sulfuras_max_quality(self):
        items = [LegendaryItem("Sulfuras, Hand of Ragnaros", 1, 82)]
        item = GildedRose(items)
        item.update_quality()
        self.assertEqual(80, items[0].quality)

    # BackStage
    def test_backstage_sell_in_15(self):
        items = [BackstagePasses("BackStage Passes to a TAFKAL80ETC concert", 15, 20)]
        item = GildedRose(items)
        item.update_quality()
        self.assertEqual(21, items[0].quality)

    def test_backstage_sell_in_10(self):
        items = [BackstagePasses("BackStage Passes to a TAFKAL80ETC concert", 10, 20)]
        item = GildedRose(items)
        item.update_quality()
        self.assertEqual(22, items[0].quality)

    def test_backstage_sell_in_7(self):
        items = [BackstagePasses("BackStage Passes to a TAFKAL80ETC concert", 7, 20)]
        item = GildedRose(items)
        item.update_quality()
        self.assertEqual(22, items[0].quality)

    def test_backstage_sell_in_5(self):
        items = [BackstagePasses("BackStage Passes to a TAFKAL80ETC concert", 5, 20)]
        item = GildedRose(items)
        item.update_quality()
        self.assertEqual(23, items[0].quality)

    def test_backstage_sell_in_4(self):
        items = [BackstagePasses("BackStage Passes to a TAFKAL80ETC concert", 4, 20)]
        item = GildedRose(items)
        item.update_quality()
        self.assertEqual(23, items[0].quality)

    def test_backstage_sell_in_0(self):
        items = [BackstagePasses("BackStage Passes to a TAFKAL80ETC concert", 0, 49)]
        item = GildedRose(items)
        item.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_backstage_after_concert(self):
        items = [BackstagePasses("BackStage Passes to a TAFKAL80ETC concert", -1, 49)]
        item = GildedRose(items)
        item.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_backstage_quality_change_50(self):
        items = [BackstagePasses("BackStage Passes to a TAFKAL80ETC concert", 10, 50)]
        item = GildedRose(items)
        item.update_quality()
        self.assertEqual(50, items[0].quality)

    # Conjured
    def test_conjured_before_sell_date(self):
        items = [ConjuredItem("Conjured Mana Cake", 3, 6)]
        item = GildedRose(items)
        item.update_quality()
        self.assertEqual(4, items[0].quality)

    def test_conjured_on_sell_date(self):
        items = [ConjuredItem("Conjured Mana Cake", 0, 6)]
        item = GildedRose(items)
        item.update_quality()
        self.assertEqual(2, items[0].quality)

    def test_conjured_after_sell_date(self):
        items = [ConjuredItem("Conjured Mana Cake", -2, 6)]
        item = GildedRose(items)
        item.update_quality()
        self.assertEqual(2, items[0].quality)

    # Other
    def test_other_products(self):
        dexterity_item = [RegularItem("+5 Dexterity Vest", 10, 20)]
        elixir_item = [RegularItem("Elixir of the Mongoose", 5, 7)]

        item_dexterity = GildedRose(dexterity_item)
        item_dexterity.update_quality()

        item_elixir = GildedRose(elixir_item)
        item_elixir.update_quality()
        self.assertEqual(19, dexterity_item[0].quality)
        self.assertEqual(6, elixir_item[0].quality)


if __name__ == '__main__':
    unittest.main()
