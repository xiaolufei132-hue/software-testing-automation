"""登录页面 Page Object"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """SauceDemo 登录页面"""

    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CSS_SELECTOR, "[data-test='error']")
        self.app_logo = (By.CLASS_NAME, "app_logo")

    def login(self, username, password):
        """执行登录操作"""
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        """获取错误提示信息"""
        try:
            return WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(self.error_message)
            ).text
        except Exception:
            return ""

    def is_login_success(self):
        """判断登录是否成功（进入首页）"""
        try:
            WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(self.app_logo)
            )
            return True
        except Exception:
            return False
