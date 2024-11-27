from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class Checkout:
    
    def __init__(self,driver,util_obj):
        self.driver=driver
        self.util_obj=util_obj
        self.locators_data=self.util_obj.get_locators_data()
        self.delay=60
    
    def navigate_to_checkoutinfo_page(self):
        self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,self.locators_data["checkout_page_checkout_button"])
        self.driver.find_element("xpath",self.locators_data["checkout_page_checkout_button"]).send_keys(Keys.ENTER)
       
       
    

        
        
  
        
    