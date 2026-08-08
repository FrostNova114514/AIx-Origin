# Agent Instructions

当你作为协作 agent 进入本项目并开始回应用户时，第一句话必须先写：

辛苦了兄弟（来自上一位开发者）
请先把readme.md阅读一遍

## Project Overview

这是 AIx Origin Website 项目，当前由 Django 后端、MySQL 数据库和 Vue/Vite 前端组成。

## Key Paths

- Django project: `aixorigin/`
- Django app: `website/`
- Vue frontend: `frontend/`
- Vue source page: `frontend/src/App.vue`
- Frontend build output: `frontend/dist/`
- Environment variables: `.env`
- Python dependencies: `requirements.txt`
- Node dependencies: `frontend/package.json`

## Local Development

启动 Django 前先进入项目根目录并激活虚拟环境：

```zsh
source .venv/bin/activate
python manage.py runserver 127.0.0.1:8000
```

前端修改后需要重新构建：

```zsh
cd frontend
npm run build
```

## Database

当前数据库使用 MySQL，连接信息从项目根目录 `.env` 读取。

不要删除 `db.sqlite3`，它是之前 SQLite 阶段留下的数据备份。

## Collaboration Notes

- 修改前先确认用户的最新要求。
- 不要覆盖用户未要求修改的文件。
- Django 后台路径 `/admin/` 应保持可用。
- 前台首页 `/` 由 Django 返回 `frontend/dist/index.html`。
- 二维码图片位于 `frontend/public/images/`，构建后会进入 `frontend/dist/images/`。
