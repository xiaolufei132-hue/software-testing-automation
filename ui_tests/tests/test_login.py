"""登录功能 UI 自动化测试"""

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestLogin:
    """登录功能 UI 测试用例"""

    @pytest.mark.smoke
    def test_login_success(self, driver):
        """正常登录 - 标准用户"""
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        assert login_page.is_login_success(), "标准用户登录失败"

    def test_login_locked_user(self, driver):
        """锁定用户登录 - 应提示错误"""
        login_page = LoginPage(driver)
        login_page.login("locked_out_user", "secret_sauce")
        error_msg = login_page.get_error_message()
        assert "locked" in error_msg.lower(), "锁定用户未提示正确错误信息"

    def test_login_empty_username(self, driver):
        """空用户名登录 - 应提示错误"""
        login_page = LoginPage(driver)
        login_page.login("", "secret_sauce")
        error_msg = login_page.get_error_message()
        assert "username" in error_msg.lower(), "空用户名未提示正确错误信息"

    def test_login_empty_password(self, driver):
        """空密码登录 - 应提示错误"""
        login_page = LoginPage(driver)
        login_page.login("standard_user", "")
        error_msg = login_page.get_error_message()
        assert "password" in error_msg.lower(), "空密码未提示正确错误信息"

    def test_login_wrong_password(self, driver):
        """错误密码登录 - 应提示错误"""
        login_page = LoginPage(driver)
        login_page.login("standard_user", "wrong_password_123")
        error_msg = login_page.get_error_message()
        assert "match" in error_msg.lower(), "错误密码未提示正确错误信息"
