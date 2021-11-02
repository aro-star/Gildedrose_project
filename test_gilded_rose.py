# -*- coding: utf-8 -*-
import unittest
from gilded_rose import Item, GildedRose



class GildedRoseUpdatedTest(unittest.TestCase):
    # Regular Products
    def test_normal_item_before_sell_date(self):
        items = [Item("foo", 10, 4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(3, items[0].quality)

    def test_normal_item_on_sell_date(self):
        items = [Item("foo", 0, 9)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(7, items[0].quality)

    def test_normal_item_after_sell_date(self):
        items = [Item("foo", -10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-11, items[0].sell_in)
        self.assertEqual(8, items[0].quality)

    def test_normal_with_zero_quality(self):
        items = [Item("foo", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    # Brie
    def test_brie_before_sell_date(self):
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(2, items[0].quality)

    def test_brie_on_sell_date(self):
        items = [Item("Aged Brie", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(2, items[0].quality)

    def test_brie_after_sell_date(self):
        items = [Item("Aged Brie", -10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-11, items[0].sell_in)
        self.assertEqual(2, items[0].quality)

    def test_brie_max_quality(self):
        items = [Item("Aged Brie", 2, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_brie_over_max_quality(self):
        items = [Item("Aged Brie", 2, 52)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_brie_negative_quality(self):
        items = [Item("Aged Brie", 2, -5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    # Sulfuras
    def test_sulfuras_on_sell_date(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_sulfuras_before_sell_date(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(10, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_sulfuras_after_sell_date(self):
        items = [Item("Sulfuras, Hand of Ragnaros", -1, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_sulfuras_max_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 82)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)

    # BackStage
    def test_backstage_sell_in_15(self):
        items = [Item("BackStage Passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)

    def test_backstage_sell_in_10(self):
        items = [Item("BackStage Passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)

    def test_backstage_sell_in_7(self):
        items = [Item("BackStage Passes to a TAFKAL80ETC concert", 7, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)

    def test_backstage_sell_in_5(self):
        items = [Item("BackStage Passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(23, items[0].quality)

    def test_backstage_sell_in_4(self):
        items = [Item("BackStage Passes to a TAFKAL80ETC concert", 4, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(23, items[0].quality)

    def test_backstage_sell_in_0(self):
        items = [Item("BackStage Passes to a TAFKAL80ETC concert", 0, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_backstage_after_concert(self):
        items = [Item("BackStage Passes to a TAFKAL80ETC concert", -1, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_backstage_quality_change_50(self):
        items = [Item("BackStage Passes to a TAFKAL80ETC concert", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    # Conjured
    def test_conjured_before_sell_date(self):
        items = [Item("Conjured Mana Cake", 3, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality)

    def test_conjured_on_sell_date(self):
        items = [Item("Conjured Mana Cake", 0, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality)

    def test_conjured_after_sell_date(self):
        items = [Item("Conjured Mana Cake", -2, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality)

    # Other
    def test_other_products(self):
        dexterity_item = [Item("Guiana Chestnut", 10, 20)]
        elixir_item = [Item("Mini money tree plant", 5, 7)]

        gilded_rose_dexterity = GildedRose(dexterity_item)
        gilded_rose_dexterity.update_quality()

        gilded_rose_elixir = GildedRose(elixir_item)
        gilded_rose_elixir.update_quality()
        self.assertEqual(19, dexterity_item[0].quality)
        self.assertEqual(6, elixir_item[0].quality)

#if __name__ == '__main__':
   # unittest.main()
