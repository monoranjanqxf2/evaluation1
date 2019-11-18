"""
This class models the payment page
URL: confirmation
"""
from .Base_Page import Base_Page
from .payment_object import Payment_Object
from .sunscreens_moisturizers_object import Sunscreens_Moisturizers_Object
from utils.Wrapit import Wrapit
import conf.weather_shopper_conf as locators

class Payment_Page(Base_Page,Sunscreens_Moisturizers_Object,Payment_Object):
    "Page Object for the Payment Page"
    heading = locators.heading_payment

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'confirmation'
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

   