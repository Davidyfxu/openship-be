# backend (FastAPI)

最简单的 FastAPI 服务，提供两个接口：

- `GET /api/health` → `{"status": "ok"}`
- `GET /api/hello?name=xxx` → `{"message": "Hello, xxx!", "from": "FastAPI"}`

## 本地运行

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

访问 http://localhost:8000/docs 可以看到自动生成的接口文档。

## 部署

```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

建议用 systemd / supervisor / Docker 守护进程，前面加 Nginx 反代。
