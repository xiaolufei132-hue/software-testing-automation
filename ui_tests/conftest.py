"""Selenium UI 测试配置"""

import os
import pytest
import glob
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def _find_chromedriver():
    """查找本机 chromedriver.exe 的实际路径"""
    wdm_dir = os.path.expanduser(os.path.join("~", ".wdm", "drivers", "chromedriver"))
    pattern = os.path.join(wdm_dir, "**", "chromedriver.exe")
    matches = glob.glob(pattern, recursive=True)
    if matches:
        return matches[0]
    # fallback: 使用 webdriver-manager 安装（修复路径）
    from webdriver_manager.chrome import ChromeDriverManager
    p = ChromeDriverManager().install()
    if not p.endswith("chromedriver.exe"):
        base = os.path.dirname(p)
        return os.path.join(base, "chromedriver.exe")
    return p


@pytest.fixture(scope="session")
def base_url_ui():
    """UI 测试目标站：使用公开测试站"""
    return "https://www.saucedemo.com"


@pytest.fixture
def driver(base_url_ui):
    """Chrome WebDriver fixture"""
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")  # 无头模式
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    chromedriver_path = _find_chromedriver()
    print(f"[ChromeDriver] {chromedriver_path}")
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(5)
    driver.get(base_url_ui)

    yield driver

    # 失败时截图
    if hasattr(driver, "_test_failed") and driver._test_failed:
        driver.save_screenshot(f"screenshots/failure_{driver._test_name}.png")

    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """测试失败时标记 driver"""
    outcome = yield
    rep = outcome.get_result()
    if rep.failed:
        if "driver" in item.funcargs:
            driver = item.funcargs["driver"]
            driver._test_failed = True
            driver._test_name = item.nodeid.replace("::", "_")
