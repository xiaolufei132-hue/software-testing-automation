"""购物车页面 Page Object"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """购物车及结算页面"""

    def __init__(self, driver):
        self.driver = driver
        self.cart_list = (By.CLASS_NAME, "cart_list")
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.checkout_button = (By.ID, "checkout")
        self.continue_shopping = (By.ID, "continue-shopping")
        self.remove_buttons = (By.CSS_SELECTOR, ".cart_button")

    def is_on_cart_page(self):
        """是否在购物车页面"""
        try:
            WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(self.cart_list)
            )
            return True
        except Exception:
            return False

    def get_cart_item_count(self):
        """获取购物车商品数量"""
        return len(self.driver.find_elements(*self.cart_items))

    def remove_item(self, index=0):
        """移除购物车中的商品"""
        buttons = self.driver.find_elements(*self.remove_buttons)
        if buttons and index < len(buttons):
            buttons[index].click()

    def proceed_to_checkout(self):
        """进入结算页面"""
        self.driver.find_element(*self.checkout_button).click()
