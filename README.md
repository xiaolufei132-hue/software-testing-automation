# 🧪 电商系统接口与 UI 自动化测试 Demo

> 软件测试实习简历项目 | Python + pytest + Selenium + Postman + Allure

## 项目概述

基于开源 REST API 实现的完整软件测试 Demo，覆盖测试全流程：测试计划 → 用例设计 → 接口自动化 → UI 自动化 → 缺陷跟踪 → 测试报告。

## 项目结构

```
software-testing-demo/
├── api_tests/              # 接口自动化测试
│   ├── conftest.py         # pytest 全局配置、fixture
│   ├── test_user_api.py    # 用户模块接口测试
│   ├── test_product_api.py # 商品模块接口测试
│   ├── test_order_api.py   # 订单模块接口测试
│   ├── data/               # 测试数据
│   │   └── test_data.json  # DDT 数据驱动文件
│   └── utils/              # 工具模块
│       └── api_client.py   # 封装 HTTP 请求客户端
├── ui_tests/               # UI 自动化测试
│   ├── conftest.py         # Selenium driver fixture
│   ├── pages/              # Page Object 页面对象
│   │   ├── login_page.py
│   │   ├── inventory_page.py
│   │   └── cart_page.py
│   ├── tests/              # UI 测试用例
│   │   ├── test_login.py
│   │   ├── test_shopping.py
│   │   └── test_checkout.py
│   └── screenshots/        # 失败截图
├── test_cases/             # 功能测试用例文档
│   └── 测试用例_电商系统.md
├── requirements.txt
└── README.md
```

## 快速开始

```bash
# 克隆项目
git clone <your-repo-url>
cd software-testing-demo

# 安装依赖
pip install -r requirements.txt

# 运行接口测试
pytest api_tests/ -v --alluredir=./allure-results

# 运行 UI 测试（需要 Chrome）
pytest ui_tests/ -v --alluredir=./allure-results

# 查看 Allure 报告
allure serve ./allure-results
```

## 测试覆盖范围

### 接口测试（20 条）
| 模块 | 测试点 | 用例数 |
|------|--------|--------|
| 用户模块 | 注册、登录、获取用户信息、更新资料 | 6 |
| 商品模块 | 商品列表、搜索、详情查询、分类 | 6 |
| 订单模块 | 创建订单、查询订单、取消订单、订单列表 | 8 |

### UI 测试（6 条）
| 业务流程 | 覆盖场景 |
|----------|----------|
| 用户登录 | 正常登录、错误密码、空输入 |
| 商品浏览 → 加购 | 搜索商品、加入购物车 |
| 购物车 → 结算 | 修改数量、删除商品、提交订单 |
| 订单查看 | 查看订单详情、取消订单 |

## 测试报告示例

运行后 Allure 报告包含：
- 测试通过率统计
- 失败用例执行日志及截图
- 测试执行趋势
- 用例分类统计
