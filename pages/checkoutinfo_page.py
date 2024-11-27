from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class CheckoutInfo:
    def __init__(self,driver,util_obj):
        self.driver=driver
        self.util_obj=util_obj
        self.locators_data=self.util_obj.get_locators_data()
        self.delay=60
        
    def input_first_name(self,firstname):
        self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,self.locators_data["checkout_info_page_firstname"])
        self.driver.find_element("xpath",self.locators_data["checkout_info_page_firstname"]).clear()
        self.driver.find_element("xpath",self.locators_data["checkout_info_page_firstname"]).send_keys(firstname)
    
    def input_last_name(self,lastname):
        self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,self.locators_data["checkout_info_page_lastname"])
        self.driver.find_element("xpath",self.locators_data["checkout_info_page_lastname"]).clear()
        self.driver.find_element("xpath",self.locators_data["checkout_info_page_lastname"]).send_keys(lastname)
    
    def input_postal_code(self,postalcode):
        self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,self.locators_data["checkout_info_page_postalcode"])
        self.driver.find_element("xpath",self.locators_data["checkout_info_page_postalcode"]).clear()
        self.driver.find_element("xpath",self.locators_data["checkout_info_page_postalcode"]).send_keys(postalcode)
    
    def click_continue(self):
        self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,self.locators_data["checkout_info_page_continue_button"])
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element("xpath",self.locators_data["checkout_info_page_continue_button"])).perform()
        self.driver.find_element("xpath",self.locators_data["checkout_info_page_continue_button"]).send_keys(Keys.ENTER)
        
        
   
        
    