# Python Backend + Vue Frontend Demo

## 项目结构
```
test/
├── backend/
│   ├── app.py
│   └── requirements.txt
└── frontend/
    ├── index.html
    ├── package.json
    ├── vite.config.js
    └── src/
        ├── App.vue
        └── main.js
```

## 后端启动

```bash
cd backend
pip install -r requirements.txt
python app.py
```

后端运行在：http://localhost:5000

## 前端启动

```bash
cd frontend
npm install
npm run dev
```

前端运行在：http://localhost:3000

## API接口

- GET `/` - 欢迎信息
- GET `/api/health` - 健康检查
- GET `/api/data` - 获取数据列表

## 前后端通信

前端通过Vite代理请求后端API：
- 前端访问 `/api/*` 
- 自动转发到 `http://localhost:5000/api/*`
