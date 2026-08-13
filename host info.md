# Host Info

## Daily Start

每天开始工作前先看这里，再连接云服务器。

## Server

- 云服务器公网 IP：`8.217.248.59`
- SSH 用户：`root`
- SSH 密码：`Coco3939`
- 面板地址：`https://8.217.248.59:29414/c519078d`
- 面板账号：`8pfgoano`
- 面板密码：`66830924`

## Project

- 访问域名：`aixorigin.innoai.org.cn`
- 服务器上传目录：`/www/wwwroot/aixorigin`
- Django 项目根目录：`/www/wwwroot/aixorigin`
- 前端构建目录：`/www/wwwroot/aixorigin/frontend/dist`
- 线上报名数据库：`/www/wwwroot/aixorigin/db.sqlite3`
- 当前域名 `aixorigin.innoai.org.cn` 解析到 `8.217.248.59`，后续 SSH / 部署 / 导出数据均连接这台服务器。

## Connection

优先顺序：

1. 先打开宝塔面板，确认站点和服务状态
2. 再用 SSH 进入服务器终端
3. 需要改文件时，优先在服务器目录直接修改或上传
4. 需要同步代码时，再用 Git / 文件上传

## Daily Checklist

开工前按这个顺序确认：

1. 先读本文件
2. 检查是否已经连到服务器
3. 检查站点目录是否在 `/www/wwwroot/aixorigin`
4. 检查 Django / Nginx / SQLite 是否正常
5. 再开始改网站、导数据或发版

## Notes

- 网站所有前端、后端和静态文件都上传到上述目录。
- 如果后续更换子域名或站点目录，请同步更新本文件。
- 不要把真实密码写进代码仓库里的 `.env.example`。
