"""购物流程 UI 自动化测试"""

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestShopping:
    """购物车功能 UI 测试用例"""

    @pytest.fixture(autouse=True)
    def setup_login(self, driver):
        """前置：登录"""
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        assert login_page.is_login_success()

    def test_add_single_item_to_cart(self, driver):
        """添加单个商品到购物车"""
        inventory = InventoryPage(driver)
        inventory.add_item_to_cart(0)
        assert inventory.get_cart_count() == 1, "添加1个商品后购物车角标不为1"

    def test_add_multiple_items_to_cart(self, driver):
        """添加多个商品到购物车"""
        inventory = InventoryPage(driver)
        inventory.add_item_to_cart(0)
        inventory.add_item_to_cart(1)
        assert inventory.get_cart_count() == 2, "添加2个商品后购物车角标不为2"

    def test_inventory_page_loads(self, driver):
        """商品列表页加载正常"""
        inventory = InventoryPage(driver)
        assert inventory.is_on_inventory(), "商品列表页未正确加载"
