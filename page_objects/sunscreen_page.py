"""
This class models the sunscreens page
URL: sunscreen
"""
from .Base_Page import Base_Page
import conf.weather_shopper_conf as locators
from .sunscreens_moisturizers_object import Sunscreens_Moisturizers_Object
from .checkout_payment_object import Checkout_Payment_Object
from utils.Wrapit import Wrapit


class Sunscreen_Page(Base_Page,Sunscreens_Moisturizers_Object,Checkout_Payment_Object):
    "Page Object for the Sunscreen Page"

    #locators
    heading = locators.heading_sunscreen

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'sunscreen'
        self.open(url)
        
    ##can add a fixture
    @Wrapit._exceptionHandler    
    def check_heading(self):
        "Check if the heading exists"
        result_flag = self.check_element_present(self.heading)
        self.conditional_write(result_flag,
            positive='Correct heading present on redirect page',
            negative='Heading on redirect page is INCORRECT!!',
            level='debug')

        return result_flag