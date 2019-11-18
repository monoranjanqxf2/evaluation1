"""
This class models the weather shopper's main page objects
"""
from .Base_Page import Base_Page
import conf.weather_shopper_conf as locators
from utils.Wrapit import Wrapit
import random


class Weather_Shopper_object:
    "Page Object for the weather shopper's main page"
    
    #locators
    temperature_field = locators.temperature_field
    click_buy_moisturizers = locators.click_moisturizers 
    click_buy_sunscreens = locators.click_sunscreens 
    heading_text = locators.heading_text
    heading_sunscreen =locators.heading_sunscreen
    price_tag =locators.price_tag
    pay_with_card = locators.pay_with_card

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def get_temperature(self):
        "get the temperature value from the page"
        result_flag = False
        temp_text = self.get_text(self.temperature_field)
        temp_text = temp_text.decode('utf-8')
        if temp_text !='':
            result_flag = True 
        self.conditional_write(result_flag,
            positive='The temperature is %s'%temp_text,
            negative='Could not get the temperature',
            level='debug')    

        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_moisturizer(self):
        "Click on the buy moisturizer button"
        result_flag = self.click_element(self.click_buy_moisturizers)
        self.conditional_write(result_flag,
            positive='Clicked on Buy moisturizers',
            negative='Could not click buy moisturizers button',
            level='debug')    

        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_sunscreen(self):
        "Click on the buy sunscreen button"
        result_flag = self.click_element(self.click_buy_sunscreens)
        self.conditional_write(result_flag,
            positive='Clicked on Buy sunscreen',
            negative='Could not click buy moisturizers button',
            level='debug')    

        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def check_temp_and_click_product_category(self):
        "check the temperature, if its less than 19 then clcik moisturizer and if above 34 click sunscreen  "
        result_flag = False
        temp_element = self.get_element(self.temperature_field).text
        temp_element = temp_element[:-2]
        if int(temp_element) <=19:
            print("Select moisturiser as temperature is %s"%temp_element) 
            result_flag = self.click_moisturizer()
            result_flag &=self.check_redirect_moisturizers()
        elif int(temp_element) >= 34:
            print("Select sunscreen as temperature is %s"%temp_element)
            result_flag = self.click_sunscreen()
            result_flag &= self.check_redirect_sunscreen()
        else :
            print("Stay on the homepage  as temperature is %s"%temp_element)
            result_flag = True

        return result_flag


    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def check_redirect_moisturizers(self):
        "Check the moisturizer screen is loaded on redirect"
        result_flag = False
        heading_moisturizers = self.get_page_heading("Moisturizer")
        current_url=self.get_current_url()+'s'#added s
        if heading_moisturizers.lower() in current_url.lower(): #self.driver.title():
            result_flag = True
            print(result_flag)
            self.switch_page("Moisturizers")
        self.conditional_write(result_flag,
            positive='Landed on Moisturizer screen',
            negative='Could not land on Moisturizer screen',
            level='debug')    

        return result_flag 

    
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def check_redirect_sunscreen(self):
        "Check on sunscreen screen is loaded on redirect"
        result_flag = False
        url_landed = self.get_current_url()+'s'
        heading_sunscreens = self.get_page_heading("Sunscreen")
              
        if heading_sunscreens.lower() in url_landed.lower()+'s':
            result_flag = True
            self.switch_page("Sunscreens")
        self.conditional_write(result_flag,
            positive='Landed on Sunscreen screen',
            negative='Could not land on Sunscreen screen',
            level='debug')    

        return result_flag 

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def get_page_heading(self,page_heading):
        "get the page heading"
        self.wait(5)
        result_flag = False
        heading_text = self.get_text(self.heading_text%page_heading)
        heading_text = heading_text.decode('utf-8')
        if heading_text !='':
            result_flag = True  
        self.conditional_write(result_flag,
            positive='The heading of the page is %s'%page_heading,
            negative='Could not get the page heading',
            level='debug')    

        return heading_text

    


    



 