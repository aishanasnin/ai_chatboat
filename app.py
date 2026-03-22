from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"].lower()

    if "hello" in user_message:
        reply = "Hi Aisha 😊 I'm your AI Mentor! Tell me your goal."

    elif "sad" in user_message or "tired" in user_message or "stressed" in user_message:
        reply = "I'm here for you 💙 It's okay to feel this way. Take a small break and don't be too hard on yourself."

    elif "happy" in user_message or "excited" in user_message:
        reply = "That's amazing 😄 Keep going! You're doing great!"

    elif "ai" in user_message:
        reply = "Great choice! 🚀 To become an AI Engineer, start with Python, Machine Learning, and build projects."

    elif "data science" in user_message:
        reply = "Data Science is amazing 📊 Learn Python, statistics, and tools like Pandas and Matplotlib."

    elif "confused" in user_message:
        reply = "No worries 💙 Tell me your interests, and I will guide you step by step."

    elif "goal" in user_message:
        reply = "Set a clear goal 🎯 Then break it into small daily tasks. I can help you plan!"

    else:
        reply = "That's interesting 😊 Tell me more about your goal or interests."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)