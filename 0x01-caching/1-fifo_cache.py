#!/usr/bin/env python3
""" fifo cache module
"""

from base_caching import BaseCaching
from dataclasses import dataclass
from typing import List, Any


@dataclass
class FIFOCache(BaseCaching):

    """ Fifo cache class
    """
    # KEYS: List[str] = []

    def __post_init__(self):
        super().__init__()
        self._keys = []  # just for the class dsa

    def put(self, key, item) -> None:
        keys = self._keys
        if key or item is None:
            pass
        # if key in self.cache_data:
        #     self.cache_data[key] = item
        if len(self.cache_data) >= FIFOCache.MAX_ITEMS\
                and key not in self.cache_data:
            discarded = self.cache_data.pop(keys[0])
            print(f"DISCARD: {keys[0]}")
            keys.pop(0)
        keys.append(key)
        self.cache_data[key] = item

    def get(self, key: str) -> Any:
        """ get item by key method for the cache storage

        Args:
            key (str): item key

        Returns:
            Any: item
        """
        if key is None:
            return None
        if key not in self.cache_data:
            return None

        return self.cache_data[key]
