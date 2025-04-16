class CartPageLocators:

    NUMBER_OF_ROWS = 'tbody > tr'
    QTY = '[class="disabled"]'

    @staticmethod
    def product_name(index:int)->str:
        return f'(//*[@class="cart_description"]/h4/a)[{index}]'

    @staticmethod
    def product_price(index:int)->str:
        return f'(//*[@class="cart_price"]/p)[{index}]'
