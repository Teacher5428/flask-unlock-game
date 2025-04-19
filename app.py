from flask import Flask, request, render_template

app = Flask(__name__)

# 密碼對應提示（之後可以擴充成多關）
password_to_hint = {
    "code101": "🎉 恭喜通關第一關！請準備迎接 if 判斷式！",
    "loopmaster": "✅ 你掌握了迴圈魔法，下一關：清單挑戰！"
}

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        code = request.form["code"]
        message = password_to_hint.get(code, "❌ 密碼錯誤，請再試一次！")
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
