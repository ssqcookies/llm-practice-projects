# main.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import os  # 导入 os 模块

app = Flask(__name__)
CORS(app)  # 允许跨域

# 获取当前脚本所在目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 加法接口


@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()  # 获取参数
    a = data.get('a', 0)
    b = data.get('b', 0)
    return jsonify({"result": a + b})

# 返回openapi.yaml，给模型提供接口文档


@app.get('/openapi.yaml')
def openapi_yaml():
    file_path = os.path.join(BASE_DIR, "openapi.yaml")
    with open(file_path, encoding="utf-8") as f:
        return f.read(), 200, {"Content-Type": "text/yaml"}


# 返回ai-plugin.json，给模型提供插件身份证
@app.get('/.well-known/ai-plugin.json')
def ai_plugin_json():
    file_path = os.path.join(BASE_DIR, ".well-known", "ai-plugin.json")
    with open(file_path, encoding="utf-8") as f:
        return f.read(), 200, {"Content-Type": "text/json"}


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5003)
