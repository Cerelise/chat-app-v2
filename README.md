# chat-app-v2

这是毕业设计的开发版本



## 前端

### 启动项目

```javascript
// 安装依赖
yarn install

// 运行项目
yarn install
```

注意：Node版本需要14及以上



## 后端

### 准备虚拟环境

在`chat-server` 目录下创建虚拟环境

```python
python -m venv [venv_name]
```

进入虚拟环境

```python
[venv_name]\Scripts\activate
```

退出虚拟环境

```python
deactivate
```

所需包版本

在`chat_websocket`目录下的`requirements.txt`文件夹内



### 启动项目前的准备

```python
# 在chat_websocket目录下执行：
mkdir upload  # (windows建立文件夹upload)
# 重新覆写数据库
python manage.py makemigrations

python manage.py migrate

# 创建超级用户
python manage.py createsuperuser

```



### 启动项目

在`chat-server` 项目文件夹下运行此命令：

```python
# 启动后端
python manage.py runserver <指定端口号>
```

