# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    # -- Generic Items --
    def test_generic_quality(self):
        items = [Item("generic", 7, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].quality)
        
    def test_generic_sell_in(self):
        items = [Item("generic", 7, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].sell_in)
        
    def test_generic_quality_if_sell_in_zero(self):
        items = [Item("generic", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)       

    def test_generic_quality_above_zero(self):
        items = [Item("generic", 7, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)        

    # -- Conjured Items --
    def test_conjured_quality(self):
        items = [Item("Conjured", 7, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)
        
    def test_conjured_sell_in(self):
        items = [Item("Conjured", 7, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].sell_in)

    # -- Aged Brie Items --
    def test_aged_brie_quality(self):
        items = [Item("Aged Brie", 7, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(11, items[0].quality)
        
    def test_aged_brie_sell_in(self):
        items = [Item("Aged Brie", 7, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].sell_in)
        
    def test_aged_brie_quality_below_fifty(self):
        items = [Item("Aged Brie", 7, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)   

    # -- Backstage passes to a TAFKAL80ETC concert Items --
    def test_backstage_passes_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(11, items[0].quality)
        
    def test_backstage_passes_sell_in(self):
        items = [Item("generic", 7, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].sell_in)
        
    def test_backstage_passes_quality_double(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(12, items[0].quality)

    def test_backstage_passes_quality_triple(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(13, items[0].quality)

    def test_backstage_passes_quality_below_fifty(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 7, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)  
        
    def test_backstage_passes_quality_if_sell_in_zero(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)    

    # -- Sulfuras Items --
    def test_sulfuras_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 7, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(10, items[0].quality)
        
    def test_sulfuras_sell_in(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 7, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(7, items[0].sell_in)

if __name__ == '__main__':
    unittest.main()
