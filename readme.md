### [myblog](https://github.com/Nicholasjl/myblog)前后端分离的后端部分，[前端部分](https://github.com/Nicholasjl/Nicholasjl.github.io)
# Readme

### [示例页面](https://blog.coooool.club/)

---

## 使用方法

### 部署

#### 需要python3.6+，依赖环境：sanic，markdown，aiofiles，gunicorn

### 一键运行

    gunicorn run:app --bind 0.0.0.0:1337 --worker-class sanic.worker.GunicornWorker

### 文件上传，先在password文件保存口令的sha256值，上传时使用markdown文件，上传同名文件会覆盖

## 保留名称

### about，intro，content，分别对应关于、主页、联系三个页面

#### 本项目主要使用了js(jquery),scss等前端js库，后端sanic仅提供了简单的数据存取
