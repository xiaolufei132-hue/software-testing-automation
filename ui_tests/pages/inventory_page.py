"""商品列表页面 Page Object"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class InventoryPage:
    """SauceDemo 商品页面"""

    def __init__(self, driver):
        self.driver = driver
        self.inventory_container = (By.ID, "inventory_container")
        self.inventory_items = (By.CLASS_NAME, "inventory_item")
        self.add_to_cart_buttons = (By.CSS_SELECTOR, ".btn_inventory")
        self.shopping_cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")
        self.sort_dropdown = (By.CLASS_NAME, "product_sort_container")

    def add_item_to_cart(self, index=0):
        """将第 index 个商品加入购物车"""
        buttons = self.driver.find_elements(*self.add_to_cart_buttons)
        if buttons:
            buttons[index].click()

    def get_cart_count(self):
        """获取购物车角标数量"""
        try:
            badge = self.driver.find_element(*self.shopping_cart_badge)
            return int(badge.text)
        except Exception:
            return 0

    def go_to_cart(self):
        """跳转到购物车页面"""
        self.driver.find_element(*self.cart_link).click()

    def is_on_inventory(self):
        """是否在商品列表页面"""
        try:
            WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(self.inventory_container)
            )
            return True
        except Exception:
            return False

    def sort_by(self, option_value):
        """按指定规则排序"""
        select = Select(self.driver.find_element(*self.sort_dropdown))
        select.select_by_value(option_value)
