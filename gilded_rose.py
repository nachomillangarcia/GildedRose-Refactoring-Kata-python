# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    self.update_backstage_concert(item)
                elif item.name == "Aged Brie":
                    self.quality_add(item)
                else:
                    self.quality_remove(item)
                    
                if item.sell_in < 0:
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        item.quality = 0  # Quality drops to 0 after the concert
                    elif item.name == "Aged Brie":
                        self.quality_add(item) # "Aged Brie" actually increases in Quality the older it gets
                    else:
                        self.quality_remove(item) #Once the sell by date has passed, Quality degrades twice as fast
                    
               
    def update_backstage_concert(self, item):          
        if item.quality < 50:     #The Quality of an item is never more than 50
            item.quality = item.quality + 1
            if item.sell_in < 11:
                item.quality = item.quality + 1
            if item.sell_in < 6:
                item.quality = item.quality + 1
    
    def quality_add(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1
    
    def quality_remove(self, item):
        if item.quality > 0: 
            item.quality = item.quality - 1
        if item.name == "Conjured" and item.sell_in > 0:  #"Conjured" items degrade in Quality twice as fast as normal items
            item.quality = item.quality - 1
            
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
        
             #NAME SELL_IN QUALITY 
item1 = Item("Aged Brie", 10, 20)
item2 = Item("Sulfuras, Hand of Ragnaros", 0, 50)
item3 = Item("Backstage passes to a TAFKAL80ETC concert", 0, 40)
item4 = Item("Random item", 5, 10)
item4 = Item("Conjured", 7, 14)

items= [item1, item2, item3, item4]
output = GildedRose(items)

output.update_quality()

for item in items:
    print(item)
