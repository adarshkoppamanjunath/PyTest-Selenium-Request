from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class SignIn:
    
    def __init__(self,driver,util_obj):
        self.driver=driver
        self.util_obj=util_obj
        self.locators_data=self.util_obj.get_locators_data()
        self.delay=60
        
    def input_user_name(self,username):
        self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,self.locators_data["signin_page_username"])
        self.driver.find_element("xpath",self.locators_data["signin_page_username"]).clear()
        self.driver.find_element("xpath",self.locators_data["signin_page_username"]).send_keys(username)
    
    def input_user_password(self,password):
        self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,self.locators_data["signin_page_password"])
        self.driver.find_element("xpath",self.locators_data["signin_page_password"]).clear()
        self.driver.find_element("xpath",self.locators_data["signin_page_password"]).send_keys(password)
    
    def click_signin(self):
        self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,self.locators_data["signin_page_login_button"])
        self.driver.find_element("xpath",self.locators_data["signin_page_login_button"]).send_keys(Keys.ENTER)
        
   
        
    