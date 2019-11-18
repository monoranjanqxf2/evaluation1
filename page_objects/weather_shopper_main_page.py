"""
This class models the main page of Weather shopper application
URL: its the main page so no URL mentioned
"""
from .Base_Page import Base_Page
from .weather_shopper_object  import Weather_Shopper_object
from .sunscreens_moisturizers_object import Sunscreens_Moisturizers_Object
from .payment_object import Payment_Object
from utils.Wrapit import Wrapit


class Weather_Shopper_Main_Page(Base_Page,Weather_Shopper_object,Sunscreens_Moisturizers_Object,Payment_Object):
    "Page Object for the weather shopper's main page"
    
    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = ''
        self.open(url)
