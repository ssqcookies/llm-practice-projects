# 项目简介
  llm-practice-projects
  本仓库为大模型 API 开发入门学习项目，主要用于学习：
  - Jupyter Notebook 交互式编程使用方法
  - OpenAI API 接口调用原理、参数结构、对话逻辑
  - 国内大模型替代方案（智谱 GLM）实战开发
  由于 OpenAI 账号存在信用卡付费、地区网络限制等问题，本项目以智谱 GLM 大模型作为替代训练与实战载体，完整复刻 OpenAI 调用逻辑，实现零基础入门大模型接口开发。

## 学习内容与核心知识点
  ### Jupyter Notebook 交互式开发学习
  掌握 AI 开发最常用的交互式记事本工具：
  - 单元格逐行运行、分段调试代码
  - 实时查看接口返回结果、快速调试参数
  - 适合 AI 模型实验、接口测试、代码学习
  - 支持文本、代码、注释、结果可视化记录
  ### OpenAI API 理论学习（核心原理）
  系统学习 OpenAI 官方接口规范，包含：
  - 大模型 Chat Completions 对话接口 原理
  - 请求体结构：model、messages、role 角色机制（user/assistant/system）
  - 温度值 temperature、最大生成长度、流式输出参数理解
  - HTTP POST 请求、JSON 数据交互逻辑
  - 大模型插件调用、Function Call 底层原理
  ### 智谱 GLM 替代实战（国内可用）
  因 OpenAI 存在境外网络限制、信用卡充值门槛、账号风控等问题，本项目全程使用智谱 GLM 大模型替代学习：
  - 完全兼容 OpenAI 调用范式，学习效果一致
  - 国内直连、无需代理、免费额度充足
  - 复刻对话接口、多轮对话、参数调试
  - 拓展：智谱插件开发、OpenAPI 规范实战

## 项目目录结构
├── notebook/                # Jupyter 交互式学习笔记
├── openai_api/              # OpenAI API 原理学习代码
├── plugin_demo/             # 大模型插件开发案例
├── langchain/               # 
├── requirements.txt         # 项目依赖
└── README.md 


```
llm-practice-projects/
├── openai_api/                      # OpenAI API 原理学习代码
│   ├── data/                 # 数据库文件
│   │   └── testSQL.db
│   ├── images/               # 图片数据
│   │   └── page.tsx          
│   ├── models.ipynb          # 大模型基础调用：模型列表、参数配置、基础对话逻辑学习
│   ├── tiktoken.ipynb        # Token 计数原理、文本切分、上下文窗口管理练习           
│   ├── function_call.ipynb   #  函数调用（Function Call）原理学习，模拟插件调用流程             
│   ├── weather.ipynb         #  函数调用实战：天气查询插件开发与调试             
│   ├── function_call.ipynb   #  函数调用（Function Call）原理学习，模拟插件调用流程             
│   ├── test.pdf              #  PDF 解析测试用文档            
│   ├── The_Old_Man_of_the_Sea.pdf   #  长篇文本解析与问答示例             
│   └── pdfplumber.ipynb             #  PDF 文档解析与大模型文本问答实战，含 `test.pdf`、`The_Old_Man_of_the_Sea.pdf` 示例文件              
├── plugin_demo/                     # 大模型插件开发案例
│   ├── add_plugin/                  # 用 ngrok 调试智谱加法插件的完整流程
│   │   ├── .well-known/    
│   │       └── ai-plugin.json      
│   │   ├── main.py    
│   │   ├── logo.png    
│   │   ├── openapi.yaml     
│   │   └── README.md
│   ├── weather_plugin/         # 天气插件
│   │   ├── .well-known/    
│   │       └── ai-plugin.json      
│   │   ├── main.py    
│   │   ├── logo.png    
│   │   ├── openapi.yaml     
│   │   └── README.md
│   ├── ngrok/
├── .gitignore
├── requirements.txt         # 项目依赖
└── README.md
```

## 环境依赖
Python 版本：3.8+

大模型开发（LangChain）标准环境
安装 Python → 建虚拟环境 → 装依赖 → 配置 OpenAI → 装 Jupyter Lab → 后台长期运行

安装 Miniconda
创建虚拟环境并激活：zxxlangchain
  ```bash
  conda create -n zxxlangchain python=3.10
  conda activate zxxlangchain
  ```
在虚拟环境中，安装项目依赖
  主要依赖：
  ```bash
  pip install -r requirements.txt
  ```

启动 Jupyter Lab
  ```bash
  jupyter lab
  ```
