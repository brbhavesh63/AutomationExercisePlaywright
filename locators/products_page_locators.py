class ProductsPageLocators:

    ALLPRODUCTS_HEADER = "[class='features_items']>h2"
    FEATURE_ITEMS = '[class="features_items"]'
    FIRST_PRODUCT = '[href="/product_details/1"]'
    SEARCH_FIELD = "[id='search_product']"
    SEARCH_BTN = "[id='submit_search']"
    TOTAL_PRODUCT_IMAGE_WRAPPER = "[class='product-image-wrapper']"
    BTN_CONTINUE_SHOPPING = "[data-dismiss='modal']"
    LINK_VIEW_CART = "[class='text-center']>[href='/view_cart']"

    @staticmethod
    def product_img_wrapper(index:int)->str:
        return f"(//*[@class='product-image-wrapper'])[{index}]"

    @staticmethod
    def overlay_btn_addtocart(index:int)->str:
        return f"//*[@class='product-overlay']//a[@data-product-id='{index}']"

    @staticmethod
    def overlay_price_product(index:int)->str:
        return f"(//*[@class='overlay-content']/h2)[{index}]"

    @staticmethod
    def overlay_name_product(index:int)->str:
        return f"(//*[@class='overlay-content']/p)[{index}]"
