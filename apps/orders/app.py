from fastapi import FastAPI

app = FastAPI(title="Orders Service", version="1.0.0")


@app.get("/health")
def health():
    return {"status": "ok", "service": "orders"}


@app.get("/orders")
def list_orders():
    return {
        "orders": [
            {"id": "ord-9001", "item_id": "sku-1002", "quantity": 1, "status": "paid"},
            {"id": "ord-9002", "item_id": "sku-1001", "quantity": 2, "status": "packed"},
        ]
    }

