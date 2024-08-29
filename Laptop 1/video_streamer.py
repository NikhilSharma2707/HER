from flask import Flask, render_template, Response, jsonify
import cv2
import socket
import requests

app = Flask(__name__)

# Initialize the webcam
camera = cv2.VideoCapture(0)

def generate_frames():
    while True:
        # Read the camera frame
        success, frame = camera.read()
        if not success:
            break
        else:
            # Encode frame as JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Yield frame as a byte array
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    # Main route to show the video stream
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    # Video streaming route
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_info', methods=['GET'])
def get_info():
    # Get the public IP address
    ip = requests.get('https://api.ipify.org').text
    # For location, you can use an IP-based geolocation service or a sensor, here we use a placeholder
    location = "Chennai, India"  # Replace with actual dynamic fetching logic
    return jsonify({'ip': ip, 'location': location})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
