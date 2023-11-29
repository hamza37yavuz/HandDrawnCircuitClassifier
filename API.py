from fastapi import FastAPI, File, UploadFile
from PIL import Image
from io import BytesIO
import numpy as np
import joblib
import skimage as ski
from skimage.feature import hog
import uvicorn

app = FastAPI()

# Eğitilmiş KNN modeli PKL dosyasından yükleme
knn_model = joblib.load("knn_model.pkl")

@app.post("/tahmin/")
async def tahmin_et(image: UploadFile):
    # Yüklenen görüntüyü okuyun ve işleyin
    image_bytes = await image.read()
    pil_image = Image.open(BytesIO(image_bytes))
    image_data = np.array(pil_image)
    image_data = hog(image_data, pixels_per_cell=(8, 8))

    # KNN modelini kullanarak tahmin yapalim
    try:
        tahmin = knn_model.predict([image_data])[0]
    except Exception as e:
        return {"HATA": e}
    
    return {"tahmin_edilen_sınıf": tahmin}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
