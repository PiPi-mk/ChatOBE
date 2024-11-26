import openai
import markdown
from flask import Flask, render_template, request, jsonify
from db.db_utils import query_database  # 引入数据库工具模块
from config import OPENAI_API_KEY

# 设置 OpenAI API key
# openai.api_key = OPENAI_API_KEY

# 创建 Flask 应用
app = Flask(__name__)

PROMPT = """
你是一款课业管理助手（名叫ChatOBE），帮助用户管理选课信息、作业、成绩等内容。
你面向的用户可能是学生，也可能是老师，用户不同时你的功能会有一定的差异。
请用专业且友好的语气回答用户的问题。
如果涉及数据库查询，请根据返回的内容生成回答。
"""

# 存储对话历史
conversation_history = [{"role": "system", "content": PROMPT}]


# 创建函数与 OpenAI API 进行交互
def get_ai_response(user_input, db_results=None):
    """生成 AI 回复，支持数据库结果的上下文"""
    # 将用户消息添加到历史中
    conversation_history.append({"role": "user", "content": user_input})

    # 如果有数据库查询结果，将其附加到 prompt 中
    if db_results:
        db_context = f"数据库查询结果如下：{db_results}"
        conversation_history.append({"role": "system", "content": db_context})

    # 与 OpenAI API 交互
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo", messages=conversation_history
    )

    # 获取 AI 回复并将其添加到历史中
    ai_message = response.choices[0].message.content.strip()
    conversation_history.append({"role": "assistant", "content": ai_message})

    # 转换为 Markdown 格式
    md_message = markdown.markdown(ai_message)
    return md_message


# 首页
@app.route("/")
def index():
    WELCOME_MSG = "欢迎使用 ChatOBE！需要我帮你做些什么？"
    return render_template("index.html", initial_message=WELCOME_MSG)


# 处理用户消息
@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.form["message"]

    # 测试：根据用户输入查询数据库
    if "查询课程" in user_message:
        sql = "SELECT * FROM course WHERE cname LIKE %s"
        params = (f"%{user_message.split()[-1]}%",)
        db_results = query_database(sql, params)
    else:
        db_results = None

    ai_message = get_ai_response(user_message, db_results=db_results)
    return jsonify({"ai_message": ai_message})


if __name__ == "__main__":
    app.run(debug=True)
