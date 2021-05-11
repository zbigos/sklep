

class BasketUtils():
    def __init__(self):
        raise NotImplementedError

    def reload_user_database(self):
        raise NotImplementedError

    def reload_product_database(self):
        raise NotImplementedError

    def add_to_basket(
        self, 
        user_ID,
        product_ID,
        count
    ):
        raise NotImplementedError

    def remove_from_basket(
        self,
        user_ID,
        product_ID,
        count
    ):
        raise NotImplementedError

    def get_basket_rundown(
        self,
        user_ID
    ):
        raise NotImplementedError