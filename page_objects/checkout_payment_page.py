"""
This class models the cart page of weather shopper.
URL: cart
"""
from .Base_Page import Base_Page
from page_objects.checkout_payment_object import Checkout_Payment_Object
from page_objects.sunscreens_moisturizers_object import Sunscreens_Moisturizers_Object
from utils.Wrapit import Wrapit


class Checkout_Payment_Page(Base_Page,Sunscreens_Moisturizers_Object,Checkout_Payment_Object):
    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'cart'
        self.open(url)
