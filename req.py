import requests

url = "http://localhost:8000/tahmin/"
image_path = "inductor/4.bmp"

files = {"image": ("4.bmp.bmp", open(image_path, "rb"), "image/bmp")}

response = requests.post(url, files=files)

print(response.json())