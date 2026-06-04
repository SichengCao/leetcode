"""
REST API 从 0 到 1 示例 - 适合面试讲解
技术栈: FastAPI + 内存存储（无数据库，便于演示）

REST 核心：用 HTTP 方法表示对「资源」的操作
- GET     -> 查询（幂等）
- POST    -> 创建
- PUT     -> 全量更新（幂等）
- PATCH   -> 部分更新
- DELETE  -> 删除（幂等）
"""

from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# ============ 1. 创建 FastAPI 应用 ============
app = FastAPI(
    title="商品 API 示例",
    description="面试用 REST API：商品的增删改查",
    version="1.0.0",
)


# ============ 2. 定义「资源」的数据模型（Pydantic）============
# 请求体：创建/更新时客户端发来的 JSON 结构
class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1, description="商品名称")
    price: float = Field(..., gt=0, description="价格，必须大于 0")
    in_stock: bool = True


# 响应体：返回给客户端的数据（比创建多一个 id）
class ItemResponse(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool


# ============ 3. 内存「数据库」（面试时可以说：实际项目换成 MySQL/PostgreSQL）============
items_db: dict[int, ItemResponse] = {}
_next_id = 1


def get_next_id() -> int:
    global _next_id
    n = _next_id
    _next_id += 1
    return n


# ============ 4. REST 端点：CRUD ============

@app.get("/")
def root():
    """根路径，可用来做健康检查或 API 介绍。"""
    return {"message": "商品 REST API", "docs": "/docs"}


# ---------- 查询列表 ----------
@app.get("/items", response_model=list[ItemResponse])
def list_items():
    """
    GET /items -> 获取所有商品
    REST：GET 表示「读取」资源集合，不修改数据，幂等。
    """
    return list(items_db.values())


# ---------- 查询单个 ----------
@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int):
    """
    GET /items/1 -> 获取 id=1 的商品
    路径参数 item_id 表示资源标识。
    不存在时返回 404，符合 REST 语义。
    """
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="商品不存在")
    return items_db[item_id]


# ---------- 创建 ----------
@app.post("/items", response_model=ItemResponse, status_code=201)
def create_item(item: ItemCreate):
    """
    POST /items -> 创建新商品
    REST：POST 表示「创建」新资源，请求体放 JSON。
    201 Created 表示创建成功，并返回创建出的资源。
    """
    new_id = get_next_id()
    new_item = ItemResponse(id=new_id, **item.model_dump())
    items_db[new_id] = new_item
    return new_item


# ---------- 全量更新 ----------
@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: ItemCreate):
    """
    PUT /items/1 -> 用请求体完整替换 id=1 的商品
    REST：PUT 全量更新，幂等（同一请求多次结果相同）。
    """
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="商品不存在")
    updated = ItemResponse(id=item_id, **item.model_dump())
    items_db[item_id] = updated
    return updated


# ---------- 删除 ----------
@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    """
    DELETE /items/1 -> 删除 id=1 的商品
    REST：DELETE 删除资源；204 No Content 表示成功且响应体无内容。
    """
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="商品不存在")
    del items_db[item_id]
    return None  # 204 不返回 body


# ============ 5. 启动方式（见 README）============
# 命令行: uvicorn main:app --reload
# 然后访问 http://127.0.0.1:8000/docs 查看自动生成的 API 文档
