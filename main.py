from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="BN Square API")

# 允许跨域，方便前端直接访问（部署测试用，生产可收紧到具体域名）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.get("/api/hello")
def hello(name: str = "world"):
    return {"message": f"Hello, {name}!", "from": "FastAPI"}
