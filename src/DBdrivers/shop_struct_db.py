from typing import List

class ShopStructureDriver:
    def __init__(self):
        raise NotImplementedError

    def reload_database(self):
        raise NotImplementedError

    def fetch_adj_dirs(self, dirpath : List[str]):
        raise NotImplementedError

    def fetch_local_products(self, dirpath : List[str]):
        raise NotImplementedError