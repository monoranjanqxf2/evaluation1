'''
This class models payment object
'''
from .Base_Page import Base_Page
import conf.weather_shopper_conf as locators
from utils.Wrapit import Wrapit

class Payment_Object:
    "Page object for Payment page"
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def check_redirect_payment(self):
        result_flag = False
        payment_url = 'confirmation'
        current_url = self.get_current_url().lower()
        "Check the Payment screen is loaded on redirect"
        if payment_url in current_url:
            result_flag = True
            
        self.conditional_write(result_flag,
                positive='Landed on payment screen',
                negative='Could not land on payment screen',
                level='debug')    

        return result_flag
    
