"""
This class models sunscreens, moisturizers and cart objects
"""
from .Base_Page import Base_Page
import conf.weather_shopper_conf as locators
from utils.Wrapit import Wrapit
import re
import random
import time


class Sunscreens_Moisturizers_Object:
    "Page Object for the sunscreens. moisturizers , cart page"

    #locators
    page_title = locators.page_title
    add_button = locators.add_moisturizer_sunscreen_button
    cart_count = locators.cart_count
    cart_button = locators.cart_button
    add_most_expensive = locators.add_item
    price_tag = locators.price_tag
    spf30_price=locators.spf30_price
    spf50_price=locators.spf50_price
    add_item =locators.add_item
    pay_with_card = locators.pay_with_card
    frame = locators.frame

    email = locators.email
    card_no = locators.card_no
    card_exp_date = locators.card_exp_date
    card_cvv = locators.card_cvv
    zip_code = locators.zip_code
    checkbox_click_me = locators.checkbox_click_me
    mobile_no = locators.mobile_no
    pay_button = locators.pay_button
    


    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_add_button(self):
        "Click add button"    
        result_flag = self.click_element(self.add_button)
        self.conditional_write(result_flag,
            positive='Clicked on add button',
            negative='Could not click add button',
            level='debug')    

        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_all_add_button(self):
        "Click all add buttons"
        result_flag =False
        number_of_items = self.get_elements(self.price_tag)   
        for element in number_of_items:       
            price=element.text.split('\n')[1] 
            result_flag = self.click_element(self.add_item%price)
            self.conditional_write(result_flag,
            positive='Clicked on add  button',
            negative='Could not click on add  button',
            level='debug')

        return result_flag   
        
        

    
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def check_added_count(self): 
        "Check the count of added items to the card with the number of add button. They should be same"
        result_flag =False
        number_of_items= self.get_elements(self.add_button)
        number_of_add_button = len(number_of_items)  
        cart_cnt = self.get_text(self.cart_count)
        cart_cnt = cart_cnt.decode('utf-8')
        if(int(cart_cnt[0])=='1'):
            result_flag=True
            self.conditional_write(result_flag,
            positive='One items added to the cart',
            negative='No items are not added to the cart',
            level='debug')
        elif(number_of_add_button == int(cart_cnt[0])):
            result_flag=True
            self.conditional_write(result_flag,
            positive='All items added to the cart',
            negative='Some items are not added to the cart',
            level='debug')    
        
        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_cart(self):
        "Click cart items button"
        result_flag = self.click_element(self.cart_button)
        self.conditional_write(result_flag,
            positive='Clicked on cart button',
            negative='Could not click cart button',
            level='debug')    

        return result_flag
 
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def check_redirect_cart(self):
        "Check the cart screen is loaded on redirect"
        result_flag = False
        cart_url = 'cart'
        current_url = self.get_current_url().lower()                       
        if cart_url.lower() in current_url:
            self.switch_page("cart")
            result_flag = True           
        self.conditional_write(result_flag,
            positive='Landed on cart screen',
            negative='Could not land on cart screen',
            level='debug')    

        return result_flag

    
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def get_most_expensive_sunscreens(self):
        "get the most expensive item"
        list_price_most_expensive_sunscreens=[]
        max_price =0
        self.wait(5)
        result_flag = False
        number_of_items= self.get_elements(self.price_tag)
        for element in number_of_items:
            split_price = element.text
            new_price = re.findall(r'\b\d+\b', split_price)
            new_price = int(new_price[1])
            if(new_price >= max_price):
                max_price = new_price
            list_price_most_expensive_sunscreens.append(new_price)
            result_flag = True
        self.conditional_write(result_flag,
            positive='Most expensive item array is created',
            negative='Could not create array of most expensive items',
            level='debug')    

        return list_price_most_expensive_sunscreens

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_add_expensive_sunscreens(self,list_price_most_expensive_sunscreens):
        "Click on add for expensive item"
        max_value = max(list_price_most_expensive_sunscreens) 
        max_value_str = str(max_value)
        result_flag = self.click_element(self.add_most_expensive%max_value_str)
        self.conditional_write(result_flag,
            positive='Clicked on add of most expensive sunscreen',
            negative='Could not click expensive sunscreen ',
            level='debug')

        return result_flag  
    
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def get_least_expensive_spf50(self):
        list_price_least_expensive_spf50 =[]
        min_price =10000000
        self.wait(5)
        result_flag = False
        spf50_count = self.get_elements(self.spf50_price)
        for element in spf50_count:
                split_price = element.text
                new_price = re.findall(r'\b\d+\b', split_price)
                new_price = int(new_price[0])
                if(new_price <= min_price):
                        min_price = new_price
                list_price_least_expensive_spf50.append(new_price)
                result_flag = True
                self.conditional_write(result_flag,
                positive='SPF-50 sunscreens are added to the array',
                negative='Could not create array of SPF-50 sunscreen',
                level='debug')    

        return list_price_least_expensive_spf50 

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_least_expensive_spf50(self,list_price_least_expensive_spf50):
        "Click on add for least expensive SPF-50 sunscreen"
        min_value = min(list_price_least_expensive_spf50)
        min_value_str = min_value 
        result_flag = self.click_element(self.add_item%min_value_str)
        self.conditional_write(result_flag,
                positive='Clicked on SPF-50 sunscreen add button',
                negative='Could not click on add button of SPF-50 sunscreen',
                level='debug')

        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def get_least_expensive_spf30(self):
        list_price_least_expensive_spf30 =[]
        min_price =10000000
        self.wait(5)
        result_flag = False
        spf30_count = self.get_elements(self.spf30_price)
        for element in spf30_count:
                split_price = element.text
                new_price = re.findall(r'\b\d+\b', split_price)
                new_price = int(new_price[0])
                if(new_price <= min_price):
                        min_price = new_price
                list_price_least_expensive_spf30.append(new_price)
                result_flag = True
                self.conditional_write(result_flag,
                positive='SPF-30 sunscreens are added to the array',
                negative='Could not create array of SPF-30 sunscreens',
                level='debug')    

        return list_price_least_expensive_spf30 

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_least_expensive_spf30(self,list_price_least_expensive_spf30):
        "Click on add for least expensive SPF-30 sunscreen"
        min_value = min(list_price_least_expensive_spf30)
        min_value_str = str(min_value)
        result_flag = self.click_element(self.add_item%min_value_str)
        self.conditional_write(result_flag,
                positive='Clicked on SPF-30 sunscreen add button',
                negative='Could not click on add button of SPF-30 sunscreen',
                level='debug')

        return result_flag
    
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def select_2_least_expensive_sunscreens(self):
        result_flag= False
        "select least priced SPF-50 and SPF-30 sunscreens"
        list_price_least_expensive_spf50 =self.get_least_expensive_spf50()
        list_price_least_expensive_spf30 =self.get_least_expensive_spf30()
        result_flag =self.click_least_expensive_spf50(list_price_least_expensive_spf50)  
        result_flag &= self.click_least_expensive_spf30(list_price_least_expensive_spf30)
        result_flag &=self.click_cart()
        result_flag &=self.check_redirect_cart()

        return result_flag


    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def select_expensive_sunscreen(self):
        "Add all items to the cart and verify if added successfully"
        list_price_most_expensive_sunscreens =self.get_most_expensive_sunscreens()
        result_flag =self.click_add_expensive_sunscreens(list_price_most_expensive_sunscreens) 
        result_flag &=self.click_cart()
        result_flag &=self.check_redirect_cart()

        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def add_all_items_and_verify_cart(self):
        "Add all items to the cart and verify if added successfully"
        result_flag =self.click_all_add_button()
        result_flag &=self.check_added_count()   
        result_flag &=self.click_cart() 
        result_flag &=self.check_redirect_cart()
        result_flag &=self.verify_payment()
        
        return  result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def add_all_moisturizers_verify_cart(self):
        "Add all mosturizers to the cart and verify if added successfully"
        result_flag =self.click_all_add_button()
        result_flag &=self.check_added_count()

        
        return result_flag

        
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def get_least_expensive_almond(self):
        list_price_least_expensive_almond =[]
        min_price =10000000
        self.wait(5)
        result_flag = False
        almonds_count = self.get_elements(self.almond_price)
        for element in almonds_count:
                split_price = element.text
                new_price = re.findall(r'\b\d+\b', split_price)
                new_price = int(new_price[0])
                if(new_price <= min_price):
                    min_price = new_price
                list_price_least_expensive_almond.append(new_price)
                result_flag = True
                self.conditional_write(result_flag,
                positive='Almonds are added to the array',
                negative='Could not create array of almonds',
                level='debug')    

        return list_price_least_expensive_almond 

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_least_expensive_almond(self,list_price_least_expensive_almond):
        "Click on add for least expensive almond"
        min_value = min(list_price_least_expensive_almond)
        min_value_str = str(min_value)
        result_flag = self.click_element(self.add_item%min_value_str)
        self.conditional_write(result_flag,
                positive='Clicked on almonds add button',
                negative='Could not click on add button of almonds',
                level='debug')

        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def get_least_expensive_aloe(self):
        list_price_least_expensive_aloe =[]
        min_price =10000000
        self.wait(5)
        result_flag = False
        aloe_count = self.get_elements(self.aloe_price)
        for element in aloe_count:
                split_price = element.text
                new_price = re.findall(r'\b\d+\b', split_price)
                new_price = int(new_price[0])
                if(new_price <= min_price):
                    min_price = new_price
                list_price_least_expensive_aloe.append(new_price)
                result_flag = True
                self.conditional_write(result_flag,
                positive='Aloe are added to the array',
                negative='Could not create array of aloe',
                level='debug')    

        return list_price_least_expensive_aloe 

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_least_expensive_aloe(self,list_price_least_expensive_aloe):
        "Click on add for least expensive Aloe"
        min_value = min(list_price_least_expensive_aloe)
        min_value_str = str(min_value)
        result_flag = self.click_element(self.add_item%min_value_str)
        self.conditional_write(result_flag,
                positive='Clicked on aloe add button',
                negative='Could not click on add button of aloe',
                level='debug')

        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def select_2_least_expensive_moisturizers(self):
        "select least priced almond and aloe moiturizers"
        list_price_least_expensive_almond =self.get_least_expensive_almond()
        list_price_least_expensive_aloe =self.get_least_expensive_aloe()
        result_flag =self.click_least_expensive_almond(list_price_least_expensive_almond)  
        result_flag &=self.click_least_expensive_aloe(list_price_least_expensive_aloe)
        result_flag &=self.click_cart()
        result_flag &=self.check_redirect_cart()
        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def get_most_expensive_moisturizer(self):
        "get the most expensive item"
        list_price_most_expensive_moisturizer =[]
        min_price =0
        self.wait(5)
        result_flag = False
        number_of_items= self.get_elements(self.price_tag)
        for element in number_of_items:
            split_price = element.text
            new_price = re.findall(r'\b\d+\b', split_price)
            new_price = int(new_price[0])
            if(new_price >= min_price):
                min_price = new_price
            list_price_most_expensive_moisturizer.append(min_price)
            result_flag = True
        self.conditional_write(result_flag,
            positive='Most expensive item array is created',
            negative='Could not create array of most expenvie items',
            level='debug')    

        return list_price_most_expensive_moisturizer

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_add_expensive_moisturizer(self,list_price_most_expensive_moisturizer):
        "Click on add for expensive item"
        max_value = max(list_price_most_expensive_moisturizer)
        print(max_value)
        max_value_str = str(max_value)
        result_flag = self.click_element(self.add_most_expensive%max_value_str)
        self.conditional_write(result_flag,
            positive='Clicked on add of most expensive moisturizer',
            negative='Could not click expensive moisturizer ',
            level='debug')

        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def select_expensive_moisturizer(self):
        "Add all items to the cart and verify if added successfully"
        list_price_most_expensive_moisturizer =self.get_most_expensive_moisturizer()
        result_flag =self.click_add_expensive_moisturizer(list_price_most_expensive_moisturizer)
        result_flag &=self.click_cart()
        result_flag &=self.check_redirect_cart()

        return result_flag

    ''' payment verification '''

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_payment(self):
        "Click payment button"
        result_flag = self.click_element(self.pay_with_card)
        self.conditional_write(result_flag,
            positive='Clicked on payment button',
            negative='Could not click payment button',
            level='debug')    

        return result_flag

        
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def verify_payment(self):
        result_flag= False
        "verify payment"
        
        result_flag = self.click_payment()
        result_flag &= self.switch_frame(self.frame)
        result_flag &= self.fill_customer_details()
        time.sleep(10)
        return result_flag

    
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def fill_customer_details(self):
        result_flag = False
        "Autometically fill customer details"
        mail_index=random.randint(1,100)
        email_id = 'monoranjan.mandal'+str(mail_index)+'@qxf2.com'
        card_number = '424242424242424242'
        exp_date = '12/30'
        cvv ='123'
        zipcode = '560100'
        mobile = '9211420420'
        result_flag = self.set_text(self.email,email_id)
        result_flag &= self.set_text(self.card_no,card_number)
        result_flag &= self.set_text(self.card_exp_date,exp_date)
        result_flag &= self.set_text(self.card_cvv,cvv)
        result_flag &= self.set_text(self.zip_code,zipcode)
        result_flag &= self.click_element(self.checkbox_click_me)
        result_flag &= self.set_text(self.mobile_no,mobile)
        result_flag &= self.click_element(self.pay_button)
        time.sleep(10)
        
        self.switch_page('payment')
        
        return result_flag
    

    


    


