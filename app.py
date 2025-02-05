from flask import Flask, jsonify, redirect, render_template
import os

app = Flask(__name__, static_folder="static", template_folder="templates")

# ✅ Serve index.html when user visits "/"
@app.route('/')
def home():
    return render_template("index.html")  # Serve index.html

# ✅ Redirect user to Freqtrade Web UI when clicking "Start Bot"
@app.route('/start-bot')
def start_bot():
    # 🔥 Replace this with your actual Freqtrade Web UI URL
    FREQTRADE_UI_URL = "https://your-freqtrade-instance.up.railway.app"

    return jsonify(success=True, redirect_url=FREQTRADE_UI_URL)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Railway assigns a dynamic port
    app.run(host='0.0.0.0', port=port)
