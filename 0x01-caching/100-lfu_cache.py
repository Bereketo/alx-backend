#!/usr/bin/env python3
"""LFU with LRU caching
"""
from base_caching import BaseCaching
lru = __import__('3-lru_cache').LRUCache
import time

#lru = LRUCache()

class LFUCache(BaseCaching):
    """Defines a LRUCache class
    """
    timeStamp = {}
    counter = {}

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """assigns to the dictionary self.cache_data
           based on LRU algorithm
        """
        if key is None or item is None:
            return
        if len(self.cache_data) == 0:
            self.cache_data[key] = item
            LFUCache.counter[key] = 1 
            lru.put(self, key, item)
            return


        if key in self.cache_data.keys():
            self.cache_data[key] = item
            LFUCache.tim
            LFUCache.counter[key] += 1
            lru.put(self, key, item)
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            rep = 0
            less = list(LFUCache.counter.values())[0]
            removed_key = list(LFUCache.counter.values())[0]
            for rm_key, lst in LUFCache.counter.items():
                if lst < less:
                    less = lst
                    removed_key = rm_key
            for k1 in LFUCache.counter.keys():
                if LFUCache.counter[k1] == LFUCache.counter[removed_key]:
                    rep += 1
            if rep >= 2:
                lru.put(self, key, item)

            del self.cache_data[removed_key]
            del LFUCache.time


    def get(self, key):
        """ return the value in self.cache_data """
        if key is None or key not in self.cache_data.keys():
            return None
        LFUCache.counter[key] += 1
        return self.cache_data[key]
