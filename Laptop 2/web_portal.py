from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace with Laptop 1's IP address and port
LAPTOP_1_IP = "http://<Laptop_1_IP>:5000"  # Replace <Laptop_1_IP> with actual IP

@app.route('/')
def index():
    # Main route to display the video feed
    return render_template('index.html', stream_url=LAPTOP_1_IP + "/video_feed")

@app.route('/get_info', methods=['GET'])
def get_info():
    # Fetch IP and location from Laptop 1
    try:
        response = requests.get(LAPTOP_1_IP + "/get_info")
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
