

class ProductDB():
    def __init__(self):
        raise NotImplementedError

    def get_product_sinfo(self, productID):
        raise NotImplementedError

    def fetch_product_page(self, productID):
        raise NotImplementedError

    def mod_product_counts(self, stock_delta, locked_delta):
        raise NotImplementedError