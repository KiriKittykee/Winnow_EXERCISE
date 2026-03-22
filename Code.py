from flask import Flask, app, jsonify, request
import os
import threading

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VIDEO_FOLDER = os.path.join(BASE_DIR, "Video_Files")
current_status = "IDLE"

def reset_status():
    global current_status
    threading.Timer(15.0, reset_status).start()  # Reset status every 20 seconds
    current_status = "IDLE"
    print("Status reset to IDLE")


@app.route('/play', methods=['POST'])
def run_video():
    global current_status

    if current_status == "PLAYING":
        return jsonify({
            'error': "A video is already playing. Please wait.",
            'status': current_status
        }), 409
    data = request.get_json()
    if not data or 'video' not in data:
        return jsonify({'error': "Missing 'Video' parameter"}), 400
    
    video_name = data['video']
    video_path = os.path.join(VIDEO_FOLDER, video_name)
    
    if not os.path.exists(video_path):
        return jsonify({'error': f"Video '{video_name}' not found"}), 404
    
    try:
        os.startfile(video_path)
        reset_status()  ## The status will reset every 10 second after playing a video
        current_status = "PLAYING"
        return jsonify({
            "status": current_status,
            "message": f"Playing {video_name}",
            "path": video_path
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500





@app.route('/status', methods=['GET'])
def get_status():
    global current_status
    return jsonify({
        "status": current_status
    }), 200




if __name__ == "__main__":
    if not os.path.exists(VIDEO_FOLDER):
        os.makedirs(VIDEO_FOLDER)

    print("API is running on port 5000.... (http://localhost:5000)")
    app.run(host='0.0.0.0', port=5000, debug=True)