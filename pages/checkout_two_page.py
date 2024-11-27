from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class CheckoutTwo:
    
    def __init__(self,driver,util_obj):
        self.driver=driver
        self.util_obj=util_obj
        self.locators_data=self.util_obj.get_locators_data()
        self.delay=60
    
    def click_finish(self):
        self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,self.locators_data["checkout_two_page_finish_button"])
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element("xpath",self.locators_data["checkout_two_page_finish_button"])).perform()
        self.driver.find_element("xpath",self.locators_data["checkout_two_page_finish_button"]).send_keys(Keys.ENTER)        
   
        
    