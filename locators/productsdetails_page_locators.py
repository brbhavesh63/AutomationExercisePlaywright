class ProductsDetailsPageLocators:

    PRODUCT_NAME = '[class="product-information"]>h2'
    PRODUCT_CATEGORY = '[class="product-information"]> :nth-child(3)'
    PRODUCT_PRICE = "[class='product-information']>span>span"
    PRODUCT_AVAILABILITY = "[class='product-information'] > :nth-child(6) > b"
    PRODUCT_CONDITION = "[class='product-information'] > :nth-child(7) > b"
    PRODUCT_BRAND = "[class='product-information'] > :nth-child(8) > b"
    QTY_FIELD = "[id='quantity']"
    ADDTOCART_BTN = "//*[@type='button']"
    VIEWCART_LINK = '//li/a[@href="/view_cart"]'