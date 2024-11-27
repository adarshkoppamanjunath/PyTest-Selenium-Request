from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
class Inventory:
    
    def __init__(self,driver,util_obj):
        self.driver=driver
        self.util_obj=util_obj
        self.locators_data=self.util_obj.get_locators_data()
        self.delay=60
        
    def get_all_products(self):
        self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,self.locators_data["inventory_page_add_to_cart"])
        inventories=self.driver.find_elements("xpath",self.locators_data["inventory_page_add_to_cart"])
        return inventories
    
    def click_add_to_cart(self,item):
        item.send_keys(Keys.ENTER)
       
       
    def navigate_to_cart_page(self):
        self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,self.locators_data["inventory_page_shopping_cart_badge"])
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element("xpath",self.locators_data["inventory_page_shopping_cart_badge"])).perform()
        self.driver.find_element("xpath",self.locators_data["inventory_page_shopping_cart_badge"]).click()
       
