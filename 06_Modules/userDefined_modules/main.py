import utility
import shopping.shopping_cart as shop
from shopping.more_shopping import shoppinggg
if __name__ == '__main__':
    print(utility.multiply(2,3))
    print(shop.addToCart('apples'))
    shop.addToCart('banananana')
    print(shop.addToCart('strawberry'))

    shoppinggg.shoppingSpree()
