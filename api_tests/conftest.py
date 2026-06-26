"""pytest 全局配置"""

import pytest
from utils.api_client import APIClient


@pytest.fixture(scope="session")
def base_url():
    """测试环境地址：使用开源 REST API 演示"""
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def client(base_url):
    """API 客户端 fixture"""
    return APIClient(base_url)


@pytest.fixture
def new_user_data():
    """测试用户数据"""
    return {
        "name": "测试用户",
        "username": "testuser",
        "email": "testuser@example.com",
        "phone": "13800138000",
    }


@pytest.fixture
def new_post_data():
    """测试文章数据"""
    return {
        "title": "软件测试实战",
        "body": "本文记录接口自动化测试实践过程",
        "userId": 1,
    }
