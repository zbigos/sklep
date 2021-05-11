from typing import List

class ShopStructureDriver:
    def __init__(self):
        raise NotImplementedError

    def reload_database(self):
        raise NotImplementedError

    def get_adj_dirs(self, dirpath : List[str]):
        raise NotImplementedError

    def get_local_products(self, dirpath : List[str]):
        raise NotImplementedError