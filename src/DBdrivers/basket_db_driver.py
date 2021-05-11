

class BasketDbDriver():
    def __init__(self):
        raise NotImplementedError

    def reload_user_database(self):
        raise NotImplementedError

    def reload_product_database(self):
        raise NotImplementedError

    def modify_basket(
        self, 
        basket_ID,
        product_ID,
        count
    ):
        raise NotImplementedError

    def fetch_basket_contents(
        self,
        basket_ID
    ):
        raise NotImplementedError