from typing import Optional

from fastapi import FastAPI
from starlette_prometheus import metrics, PrometheusMiddleware

app = FastAPI()

app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics/", metrics)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/readiness")
def readiness():
    return {"ready": "OK"}

@app.get("/liveness")
def liveness():
    return {"Ready": "OKOK"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=5000,
        access_log=True,
    )
