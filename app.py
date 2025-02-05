from flask import Flask, jsonify, redirect
import os
import subprocess

app = Flask(__name__)

FREQTRADE_CONFIG_PATH = "/root/freqtrade/config.json"
FREQTRADE_STRATEGY_PATH = "/root/freqtrade/user_data/strategies/"

@app.route('/start-bot')
def start_bot():
    try:
        # Step 1: Install Docker if missing
        subprocess.run(["apt", "install", "-y", "docker.io"], check=True)

        # Step 2: Pull Freqtrade Docker image
        subprocess.run(["docker", "pull", "freqtradeorg/freqtrade:stable"], check=True)

        # Step 3: Run Freqtrade container with predefined settings
        container_name = "freqtrade_bot"
        subprocess.run([
            "docker", "run", "-d",
            "--name", container_name,
            "-v", f"{FREQTRADE_CONFIG_PATH}:/app/config.json",
            "-v", f"{FREQTRADE_STRATEGY_PATH}:/app/user_data/strategies/",
            "-p", "8080:8080",
            "freqtradeorg/freqtrade:stable",
            "webserver", "--config", "/app/config.json"
        ], check=True)

        # Step 4: Redirect to Freqtrade Web UI
        return jsonify(success=True, redirect_url="http://localhost:8080")

    except subprocess.CalledProcessError as e:
        return jsonify(success=False, message=str(e))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
