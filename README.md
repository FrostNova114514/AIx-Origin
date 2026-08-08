# AIx Origin Website

这是一份给协作者和后续接手者看的主文档。先看这里，再看 `host info.md`。

## 1. 项目概况

AIx Origin Website 是一个由 Django + MySQL + Vue/Vite 组成的网站。

核心结构：

- Django project: `aixorigin/`
- Django app: `website/`
- Vue frontend: `frontend/`
- 前端入口页: `frontend/src/App.vue`
- 前端构建产物: `frontend/dist/`

## 2. 本地开发

开始前先确认：

- `.venv` 可用
- MySQL 已启动
- `.env` 配置存在

常用启动顺序：

```bash
source .venv/bin/activate
python manage.py runserver 127.0.0.1:8000
cd frontend
npm run build
```

如果需要快速检查：

```bash
python manage.py check
```

## 3. 协作规则

- 先拉最新代码，再开始改动
- 每个协作者使用自己的分支
- 不要直接往 `main` 硬推
- 不要覆盖别人未完成的修改
- 改完先检查，再提交

建议流程：

```bash
git checkout main
git pull
git checkout -b feature/your-change
```

完成后：

```bash
python manage.py check
cd frontend
npm run build
cd ..
git status
git add .
git commit -m "Describe the change"
git push origin feature/your-change
```

## 4. Git 提交范围

建议提交：

- `aixorigin/`
- `website/`
- `frontend/src/`
- `frontend/public/`
- `requirements.txt`
- `frontend/package.json`
- `frontend/package-lock.json`
- `website/migrations/*.py`
- `README.md`
- `docs/`
- `.env.example`

不要提交：

- `.env`
- `.venv/`
- `frontend/node_modules/`
- `frontend/dist/`
- `db.sqlite3`
- `media/`
- `backups/`
- 数据库导出文件
- 真实用户或报名数据

## 5. 服务器和部署

生产环境在香港阿里云 ECS 上。

服务器操作建议：

- 用宝塔面板管理 Nginx、SSL 和服务重启
- 安装阿里云客户端
- 官方链接：<https://help.aliyun.com/zh/ecs/user-guide/overview-of-alibaba-cloud-client>

部署时常用流程：

```bash
cd /www/wwwroot/aixorigin
git pull
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
cd frontend
npm install
npm run build
```

然后重启 Django 服务，并在面板里重载 Nginx。

## 6. 环境变量

每台机器都应有自己的 `.env`。

保留 `.env.example` 的变量名和示例值，但不要放真实密码。

示例：

```bash
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,47.79.17.48,aixorigin.innoaixhku.top
CSRF_TRUSTED_ORIGINS=https://aixorigin.innoaixhku.top
MYSQL_DATABASE=aixorigin
MYSQL_USER=aixorigin
MYSQL_PASSWORD=change-me
MYSQL_SOCKET=/tmp/mysql.sock
```

## 7. 数据和安全

- `.env` 只放本机或服务器私密配置
- 参与者数据进 MySQL，不进 Git
- 备份文件放私有存储，不要提交仓库
- `.sql`、`.base` 和上传文件不要进仓库

## 8. 常见检查点

- Django 后台 `/admin/` 要能打开
- 首页 `/` 由 Django 返回前端页面
- 前端改动后要重新构建
- 数据库报错先看 MySQL 和 `.env`

