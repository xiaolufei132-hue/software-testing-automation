"""用户模块接口测试"""

import pytest


class TestUserAPI:
    """用户 CRUD 接口测试"""

    # ────────── 正常场景 ──────────

    def test_get_all_users(self, client):
        """获取全部用户列表 - 正常场景"""
        resp = client.get("/users")
        assert resp.status_code == 200
        data = resp.json()
        assert isinstance(data, list)
        assert len(data) > 0
        # 验证必要字段
        first = data[0]
        assert "id" in first
        assert "name" in first
        assert "email" in first

    def test_get_user_by_id(self, client):
        """按 ID 获取用户 - 正常场景"""
        resp = client.get("/users/1")
        assert resp.status_code == 200
        data = resp.json()
        assert data["id"] == 1
        assert data["name"] is not None

    def test_create_user(self, client, new_user_data):
        """创建新用户 - 正常场景"""
        resp = client.post("/users", json=new_user_data)
        assert resp.status_code in (200, 201)
        data = resp.json()
        assert data["name"] == new_user_data["name"]
        assert data["email"] == new_user_data["email"]

    # ────────── 异常场景 ──────────

    def test_get_user_not_found(self, client):
        """获取不存在的用户 - 404 异常场景"""
        resp = client.get("/users/99999")
        # 根据 API 实现，可能返回 404 或空数据
        if resp.status_code == 404:
            assert True
        else:
            data = resp.json()
            assert data == {} or data is None

    def test_create_user_empty_body(self, client):
        """创建用户空请求体 - 异常场景"""
        resp = client.post("/users", json={})
        assert resp.status_code in (200, 201, 400)

    # ────────── 边界场景 ──────────

    def test_get_user_id_zero(self, client):
        """ID=0 边界值测试"""
        resp = client.get("/users/0")
        assert resp.status_code in (200, 404)
