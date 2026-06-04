# REST API 从 0 到 1 示例（面试向）

## 一、快速运行

```bash
cd rest_api_demo
pip install -r requirements.txt
uvicorn main:app --reload
```

浏览器打开：**http://127.0.0.1:8000/docs**  
可交互调试所有接口（Swagger UI）。

---

## 二、项目结构

```
rest_api_demo/
├── main.py          # 所有 API 逻辑
├── requirements.txt # 依赖
└── README.md        # 本说明
```

---

## 三、API 一览（资源：商品 Item）

| 方法   | 路径           | 含义     | 说明           |
|--------|----------------|----------|----------------|
| GET    | /items         | 列表     | 获取所有商品   |
| GET    | /items/{id}    | 详情     | 获取单个商品   |
| POST   | /items         | 创建     | 请求体 JSON    |
| PUT    | /items/{id}    | 全量更新 | 请求体完整替换 |
| DELETE | /items/{id}    | 删除     | 返回 204       |

**示例请求（创建商品）：**

```bash
curl -X POST "http://127.0.0.1:8000/items" \
  -H "Content-Type: application/json" \
  -d "{\"name\":\"苹果\",\"price\":5.5,\"in_stock\":true}"
```

---

## 四、面试可讲要点

1. **REST 是什么**  
   用 URL 表示资源，用 HTTP 方法表示操作（GET 查、POST 增、PUT 改、DELETE 删），无状态、易缓存。

2. **状态码**  
   - 200 OK：成功返回内容  
   - 201 Created：创建成功（POST）  
   - 204 No Content：成功无内容（如 DELETE）  
   - 404 Not Found：资源不存在  

3. **为什么用 FastAPI**  
   异步支持、自动校验（Pydantic）、自动生成 OpenAPI 文档（/docs），类型提示友好。

4. **扩展方向**  
   本示例用内存 `dict` 存数据；实际项目可接数据库（如 SQLAlchemy + MySQL）、加认证（JWT）、分页、过滤等。

---

## 五、从 0 到 1 的步骤回顾

1. 安装依赖：`pip install fastapi uvicorn`
2. 创建 `FastAPI()` 应用
3. 用 Pydantic 定义请求/响应模型（`BaseModel`）
4. 选一种存储（这里用内存 dict）
5. 按资源设计 URL（如 `/items`、`/items/{id}`）
6. 为每个操作写对应 HTTP 方法的端点（GET/POST/PUT/DELETE）
7. 用 `uvicorn main:app --reload` 启动，用 `/docs` 测试

祝你面试顺利。
