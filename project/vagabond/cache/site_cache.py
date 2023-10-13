"""
TODO: This needs to map recently visited sites to their HTML bodies. currenly only tracks recently visited sites.
"""
from collections import deque

class SiteCache:
    """
    Cache for storing hyperlinks.
    """
    def __init__(self, max_entries):
        self.max_entries = max_entries
        self.cache = set()
        self.link_order = deque()

    def add_link(self, url):
        """
        Adds a link to the cache. If the maximum capacity of the cache is exceeded, then the least recently written hyperlink is overwritten.
        """
        if len(self.link_order) >= self.max_entries:
            self.cache.discard(self.link_order.popleft())
        self.cache.add(url)
        self.link_order.append(url)

    # def get_link(self, key):
    #     """
    #     Return the link corresponding to key.
    #     """
    #     return self.cache.get(key)

    def __len__(self):
        return len(self.cache)

    def __str__(self):
        return str(self.cache)