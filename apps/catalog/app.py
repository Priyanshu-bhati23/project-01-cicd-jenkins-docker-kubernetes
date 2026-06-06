from fastapi import FastAPI

app = FastAPI(title="Catalog Service", version="1.0.0")

ITEMS = [
    {"id": "sku-1001", "name": "Terraform Handbook", "price": 499},
    {"id": "sku-1002", "name": "Kubernetes Lab Kit", "price": 999},
    {"id": "sku-1003", "name": "Docker Cheat Sheet", "price": 199},
]


@app.get("/health")
def health():
    return {"status": "ok", "service": "catalog"}


@app.get("/items")
def list_items():
    return {"items": ITEMS}

