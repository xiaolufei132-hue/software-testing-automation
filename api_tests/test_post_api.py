"""文章/商品模块接口测试"""

import pytest


class TestPostAPI:
    """Post（文章/商品）CRUD 接口测试"""

    # ────────── 正常场景 ──────────

    def test_get_all_posts(self, client):
        """获取全部文章列表"""
        resp = client.get("/posts")
        assert resp.status_code == 200
        data = resp.json()
        assert isinstance(data, list)
        assert len(data) > 0
        assert "title" in data[0]
        assert "body" in data[0]

    def test_get_post_by_id(self, client):
        """按 ID 获取文章"""
        resp = client.get("/posts/1")
        assert resp.status_code == 200
        data = resp.json()
        assert data["id"] == 1
        assert data["title"] is not None

    def test_create_post(self, client, new_post_data):
        """创建新文章"""
        resp = client.post("/posts", json=new_post_data)
        assert resp.status_code in (200, 201)
        data = resp.json()
        assert data["title"] == new_post_data["title"]

    def test_update_post(self, client):
        """更新文章"""
        update_data = {"title": "更新后的标题", "body": "更新内容", "userId": 1}
        resp = client.put("/posts/1", json=update_data)
        assert resp.status_code == 200
        data = resp.json()
        assert data["title"] == update_data["title"]

    def test_delete_post(self, client):
        """删除文章"""
        resp = client.delete("/posts/1")
        assert resp.status_code == 200

    # ────────── 参数化测试/数据驱动 ──────────

    @pytest.mark.parametrize("post_id,expected_title", [
        (1, "sunt aut facere repellat"),
        (2, "qui est esse"),
        (3, "ea molestias quasi"),
    ])
    def test_get_post_parametrized(self, client, post_id, expected_title):
        """参数化测试：多个 ID 验证标题开头"""
        resp = client.get(f"/posts/{post_id}")
        assert resp.status_code == 200
        data = resp.json()
        assert data["id"] == post_id
        assert expected_title in data["title"]

    # ────────── 边界场景 ──────────

    def test_get_posts_with_query(self, client):
        """带查询参数的列表接口测试"""
        resp = client.get("/posts", params={"userId": 1})
        assert resp.status_code == 200
        data = resp.json()
        assert isinstance(data, list)
        for post in data:
            assert post["userId"] == 1
