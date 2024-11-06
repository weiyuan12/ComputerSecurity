from flask import Flask, request
import os

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part in the request', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    upload_folder = os.path.join(os.getcwd(), "uploads")
    os.makedirs(upload_folder, exist_ok=True)

    file_path = os.path.join(upload_folder, "stolen_" + file.filename)
    file.save(file_path)
    return f"File uploaded successfully as {file_path}", 200
if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=5000)