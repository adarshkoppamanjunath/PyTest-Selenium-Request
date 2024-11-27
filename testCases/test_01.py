import pytest
from faker import Faker
from pages.signin_page import SignIn
from pages.inventory_page import Inventory
from pages.checkout_page import Checkout
from pages.checkoutinfo_page import CheckoutInfo
from pages.checkout_two_page import CheckoutTwo
fake = Faker()


@pytest.mark.usefixtures("setup")
class Test_01_UI:
    home_page_url="https://www.saucedemo.com/"
    def test_checkout_functionality(self):
        self.driver.get(self.home_page_url)
        sign_obj=SignIn(self.driver,self.util_obj)
        inventory_obj=Inventory(self.driver,self.util_obj)
        checkout_obj=Checkout(self.driver,self.util_obj)
        checkoutinfo_obj=CheckoutInfo(self.driver,self.util_obj)
        check_two_obj=CheckoutTwo(self.driver,self.util_obj)
        sign_obj.input_user_name("standard_user")
        sign_obj.input_user_password("secret_sauce")
        sign_obj.click_signin()
        elements=inventory_obj.get_all_products()
        inventory_obj.click_add_to_cart(elements[2])
        inventory_obj.navigate_to_cart_page()
        checkout_obj.navigate_to_checkoutinfo_page()
        checkoutinfo_obj.input_first_name(fake.first_name())
        checkoutinfo_obj.input_last_name(fake.last_name())
        checkoutinfo_obj.input_postal_code(fake.postcode())
        checkoutinfo_obj.click_continue()
        check_two_obj.click_finish()
        if "Thank you for your order!" not in self.driver.page_source:
               assert False, "Checkout Failed"


        
        
        
        