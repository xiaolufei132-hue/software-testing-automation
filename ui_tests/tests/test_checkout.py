"""结算流程 UI 自动化测试"""

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


class TestCheckout:
    """结算流程 UI 测试用例"""

    @pytest.fixture(autouse=True)
    def setup_login_and_add_item(self, driver):
        """前置：登录并添加商品"""
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        assert login_page.is_login_success()

        inventory = InventoryPage(driver)
        inventory.add_item_to_cart(0)
        assert inventory.get_cart_count() == 1

    def test_go_to_cart_and_checkout(self, driver):
        """从商品页到购物车再到结算"""
        inventory = InventoryPage(driver)
        inventory.go_to_cart()

        cart = CartPage(driver)
        assert cart.is_on_cart_page(), "未正确跳转到购物车页面"
        assert cart.get_cart_item_count() == 1, "购物车商品数量不正确"

    def test_remove_item_from_cart(self, driver):
        """从购物车中移除商品"""
        inventory = InventoryPage(driver)
        inventory.go_to_cart()

        cart = CartPage(driver)
        assert cart.get_cart_item_count() == 1
        cart.remove_item(0)
        assert cart.get_cart_item_count() == 0, "移除商品后购物车未清空"
