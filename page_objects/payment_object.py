'''
This class models payment object
'''
from .Base_Page import Base_Page
import .conf_weather_shopper_conf as locator
from util.Wrape import Wrape
import re
import random

class Payment_Object:
    "Page object for Payment page"
    
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def check_payment_success(self):
        "Check the Payment screen is loaded on redirect"
        result_flag = False
        payment_url = 'confirmation'
        current_url = self.get_current_url().lower()                       
        if payment_url in current_url:
            #self.switch_page('confirmation')
            result_flag = True            
        self.conditional_write(result_flag,
            positive='Landed on payment screen',
            negative='Could not land on payment screen',
            level='debug')    

        return result_flag
    