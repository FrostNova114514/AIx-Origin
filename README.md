# AIx Origin Website

## Reopen Checklist

在重新打开项目、准备继续编辑之前，先确认下面几件事：

1. 本机 MySQL 已启动
2. `.venv` 虚拟环境可用
3. Django 服务器已启动
4. 浏览器访问的是 `http://127.0.0.1:8000/`

## Start Order

### 1. 启动 MySQL

如果 MySQL 还没运行，先启动它：

```bash
brew services start mysql
```

如果已经启动，但网站打不开，可以重启一次：

```bash
brew services restart mysql
```

### 2. 确认数据库配置

项目默认读取 `.env`：

- `MYSQL_DATABASE=aixorigin`
- `MYSQL_USER=aixorigin`
- `MYSQL_PASSWORD=AixOriginMysql666`
- `MYSQL_HOST=127.0.0.1`
- `MYSQL_PORT=3306`

当前 Django 实际使用本机 MySQL socket 连接，无需手动改动 `.env`。

### 3. 进入虚拟环境

```bash
source .venv/bin/activate
```

### 4. 启动 Django

```bash
python manage.py runserver 127.0.0.1:8000
```

### 5. 打开网站

浏览器访问：

```text
http://127.0.0.1:8000/
```

## Troubleshooting

- 如果 `http://127.0.0.1:8000/` 无法打开，先检查 Django 是否在运行
- 如果 Django 启动时报数据库错误，先确认 MySQL 已启动
- 如果你直接打开 `frontend/dist/index.html`，页面可能无法正常工作，因为它依赖 Django 提供的路由和资源

## Useful Commands

```bash
source .venv/bin/activate
python manage.py check
python manage.py runserver 127.0.0.1:8000
brew services restart mysql
```
