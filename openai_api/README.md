# 项目名称
OpenAI API 理论学习（核心原理）

## 项目简介
  系统学习 OpenAI 官方接口规范，包含：
  - 大模型 Chat Completions 对话接口 原理
  - 请求体结构：model、messages、role 角色机制（user/assistant/system）
  - 温度值 temperature、最大生成长度、流式输出参数理解
  - HTTP POST 请求、JSON 数据交互逻辑
  - 大模型插件调用、Function Call 底层原理

## 项目目录结构

openai_api/                      # OpenAI API 原理学习代码
├── data/                 # 数据库文件
│   └── testSQL.db
├── images/               # 图片数据
│   └── page.tsx          
├── models.ipynb          # 大模型基础调用：模型列表、参数配置、基础对话逻辑学习
├── tiktoken.ipynb        # Token 计数原理、文本切分、上下文窗口管理练习           
├── function_call.ipynb   #  函数调用（Function Call）原理学习，模拟插件调用流程             
├── weather.ipynb         #  函数调用实战：天气查询插件开发与调试             
├── function_call.ipynb   #  函数调用（Function Call）原理学习，模拟插件调用流程             
├── test.pdf              #  PDF 解析测试用文档            
├── The_Old_Man_of_the_Sea.pdf   #  长篇文本解析与问答示例             
├── pdfplumber.ipynb             #  PDF 文档解析与大模型文本问答实战，含 `test.pdf`、`The_Old_Man_of_the_Sea.pdf` 示例文件    
├── gpt4v.ipynb                  #  图生文
└──