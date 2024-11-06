import requests

def upload_file(file_path, url):
    files = {'file': open(file_path, 'rb')}
    print(files)
    response = requests.post(url, files=files)
    if response.status_code == 200:
        print("File uploaded successfully!")
    else:
        print("Upload failed:", response.text)


file_path = "file.txt"
server_url = "http://10.91.142.237:5000/upload"
upload_file(file_path, server_url)