import openai
import markdown
from flask import Flask, render_template, request, jsonify

# 设置 OpenAI API 密钥
# openai.api_key = 'your-api-key'

# 创建 Flask 应用
app = Flask(__name__)

# 存储对话历史
conversation_history = []

# 创建函数与 OpenAI API 进行交互
def get_ai_response(user_input):
    # 将用户消息添加到历史中
    conversation_history.append({"role": "user", "content": user_input})

    # 与 OpenAI API 交互，传递整个对话历史
    response = openai.ChatCompletion.create(
        model="gpt-4o", messages=conversation_history  # 使用 gpt-3.5-turbo 模型
    )

    # 获取 AI 回复并将其添加到历史中
    ai_message = response["choices"][0]["message"]["content"].strip()
    ai_message = ai_message.replace("| |", "|\n|").replace("\\n", "\n")
    conversation_history.append({"role": "assistant", "content": ai_message})

    # 将 AI 回复转换为 Markdown 格式
    md_message = markdown.markdown(ai_message)  # 转换为 HTML 格式

    return md_message

# 首页
@app.route("/")
def index():
    WELCOME_MSG = "欢迎使用chatOBE~ \n 我是结合了大语言模型的OBE系统，可以帮你进行选课、查询等等。需要我帮你做些什么？"
    return render_template("index.html", initial_message=WELCOME_MSG)

# 处理用户消息
@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.form["message"]
    ai_message = get_ai_response(user_message)
    return jsonify({"ai_message": ai_message})

if __name__ == "__main__":
    app.run(debug=True)
    # http://127.0.0.1:5000/
