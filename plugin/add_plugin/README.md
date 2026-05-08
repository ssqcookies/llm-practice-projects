
## 流程
1. 启动本地服务 python main.py
2. 用 ngrok 映射公网
  配置 Token 到你的本地
  ./ngrok config add-authtoken 你的Token
  ./ngrok http 5003
  运行成功后，你会看到终端里出现类似这样的地址：
  Forwarding  https://abc123.ngrok.io -> http://localhost:5003
3. 修改配置里的地址
4. 去智谱后台导入插件
